# 매체 추천 알고리즘
from sklearn.decomposition import TruncatedSVD
from scipy.sparse.linalg import svds

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import warnings
import mysql.connector

warnings.filterwarnings("ignore")

db_config = {
    "host": "j9c107.p.ssafy.io",
    "user": "c107",
    "password": "c107adrec",
    "database": "adrec",
    "auth_plugin": "mysql_native_password"  # MySQL 8.0 이상일 경우에 필요한 옵션
}

# MySQL에 연결
conn = mysql.connector.connect(**db_config)
# SQL 쿼리 실행 및 결과를 데이터프레임으로 변환
query = "SELECT * FROM productMedia"
productMedia = pd.read_sql(query, conn)

query = "SELECT productSmall.id, large, `medium`, small, code FROM productSmall, productMedium, productLarge WHERE productSmall.productMedium_id = productMedium.id AND productMedium.productLarge_id = productLarge.id"
productLargeMediumSmall = pd.read_sql(query, conn)

# 연결 종료
conn.close()

# 데이터프레임 출력 또는 활용
# print(productMedia)  # [270 rows x 5 columns]
for index, item in productMedia.iterrows():
    # 'mediaSub_id' 열의 NaN 값을 '0'으로 대체
    if pd.isna(item['mediaSub_id']):
        productMedia.at[index, 'mediaSub_id'] = 0
print(productMedia)  # [270 rows x 5 columns]
# productMedia_total = productMedia.pivot_table(
#     index=["mediaType_id", "mediaSub_id"],
#     columns=["productSmall_id"],
#     values=["like_per"]).fillna(0)
# print(productMedia_total)  # [6 rows x 64 columns]

# csv에서 파일 가져오는 코드
print(productLargeMediumSmall)

# 전처리
productMedia.drop('id', axis=1, inplace=True)
productMedia.drop('total', axis=1, inplace=True)
# productMedia.drop('mediaSub_id', axis=1, inplace=True)
# productMedia.drop('mediaType_id', axis=1, inplace=True)
print(productMedia)  # [270 rows x 4 columns]

productLargeMediumSmall['combined_feature'] = productLargeMediumSmall['large'] + ' ' + productLargeMediumSmall['medium'] + ' ' + productLargeMediumSmall['small'] + ' ' + productLargeMediumSmall['code'].astype(str)
productLargeMediumSmall.drop('large', axis=1, inplace=True)
productLargeMediumSmall.drop('medium', axis=1, inplace=True)
productLargeMediumSmall.drop('small', axis=1, inplace=True)
productLargeMediumSmall.drop('code', axis=1, inplace=True)
print(productLargeMediumSmall)

product_media_data = pd.merge(productMedia, productLargeMediumSmall, left_on='productSmall_id', right_on='id', how='right')
print(product_media_data)  # [462 rows x 7 columns]

product_media_rating = product_media_data.pivot_table('like_per', index=['mediaType_id', 'mediaSub_id', 'productSmall_id'], columns='combined_feature').fillna(0)
print(product_media_rating)  # [270 rows x 64 columns]

media_product_rating = product_media_rating.values.T
print(media_product_rating.shape)  # (64, 270)
print(type(media_product_rating))  # <class 'numpy.ndarray'>

# SVD
SVD = TruncatedSVD(n_components=12)  # 12개의 차원으로 축소
matrix = SVD.fit_transform(media_product_rating)
print(matrix.shape)  # (64, 12)
print(matrix[0])

corr = np.corrcoef(matrix)
print(corr.shape)  # (64, 64)
corr2 = corr[:16, :16]
print(corr2.shape)  # (16, 16)

plt.figure(figsize=(16, 10))
# sns.heatmap(corr2)

# 특정 품목 (대분류,중분류,소분류,code)와 상관이 높은 매체 유형과 업종품목 번호 뽑아줌
# movie_title = media_product_rating.columns
# movie_title_list = list(movie_title)
# coffey_hands = movie_title_list.index("기타 기타")
# corr_coffey_hands = corr[coffey_hands]
# print(list(movie_title[(corr_coffey_hands >= 0.9)])[:50])


######
# 개인 추천을 해주기
# 사용자 맞춤 협업 필터링 행렬 분해
#######
# MySQL에 연결
conn = mysql.connector.connect(**db_config)
# SQL 쿼리 실행 및 결과를 데이터프레임으로 변환
query = "SELECT * FROM productMedia"
productMedia = pd.read_sql(query, conn)

query = "SELECT productSmall.id, large, `medium`, small, code FROM productSmall, productMedium, productLarge WHERE productSmall.productMedium_id = productMedium.id AND productMedium.productLarge_id = productLarge.id"
productLargeMediumSmall = pd.read_sql(query, conn)

# 연결 종료
conn.close()

df_ratings = productMedia
df_product = productLargeMediumSmall

df_media_product = df_ratings.pivot(
    index='id',
    columns='productSmall_id',
    values='like_per',
).fillna(0)
print(df_media_product)  # [270 rows x 64 columns]

# matrix는 pivot_table 값을 numpy matrix로 만든 것
matrix = df_media_product.values

# user_ratings_mean은 사용자의 평균 평점
media_ratings_mean = np.mean(matrix, axis=1)

# R_user_mean : 사용자-영화에 대해 사용자 평균 평점을 뺀 것.
matrix_media_mean = matrix - media_ratings_mean.reshape(-1, 1)
print(matrix)
print(type(matrix))  # <class 'numpy.ndarray'>
print(matrix.shape)  # (270, 64)
print(media_ratings_mean.shape)  # (270,)
print(matrix_media_mean.shape)  # (270, 64)
pd.DataFrame(matrix_media_mean, columns=df_media_product.columns).head()
print(pd.DataFrame(matrix_media_mean, columns=df_media_product.columns).head())  # [5 rows x 64 columns]

# spicy 이용한 Truncated SVD
# scipy에서 제공해주는 svd.
# U 행렬, sigma 행렬, V 전치 행렬을 반환.

U, sigma, Vt = svds(matrix_media_mean, k = 12)
print(U.shape)
print(sigma.shape)
print(Vt.shape)
# (270, 12)
# (12,)
# (12, 64)

sigma = np.diag(sigma)
print(sigma.shape)  # (12, 12)
print(sigma[0])
print(sigma[1])
# 대칭행렬
# [35.04283094  0.          0.          0.          0.          0.
#   0.          0.          0.          0.          0.          0.        ]
# [ 0.         35.04283094  0.          0.          0.          0.
#   0.          0.          0.          0.          0.          0.        ]

# U, Sigma, Vt의 내적을 수행하면, 다시 원본 행렬로 복원이 된다.
# 거기에 + 사용자 평균 rating을 적용한다.
svd_user_predicted_ratings = np.dot(np.dot(U, sigma), Vt) + media_ratings_mean.reshape(-1, 1)
df_svd_preds = pd.DataFrame(svd_user_predicted_ratings, columns=df_media_product.columns)
print(df_svd_preds)
print(df_svd_preds.shape)  # (270, 64)


def recommend_medias(df_svd_preds, user_id, ori_movies_df, ori_ratings_df, num_recommendations=5):
    # 현재는 index로 적용이 되어있으므로 user_id - 1을 해야함.
    user_row_number = user_id - 1

    # 최종적으로 만든 pred_df에서 사용자 index에 따라 영화 데이터 정렬 -> 영화 평점이 높은 순으로 정렬 됌
    sorted_user_predictions = df_svd_preds.iloc[user_row_number].sort_values(ascending=False)

    # 원본 평점 데이터에서 user id에 해당하는 데이터를 뽑아낸다.
    user_data = ori_ratings_df[ori_ratings_df.id == user_id]
    print(user_data)
    # 위에서 뽑은 user_data와 원본 영화 데이터를 합친다. - 원본 영화 데이터 -> 품목 데이터
    # pd.merge(productMedia, productLargeMediumSmall, left_on='productSmall_id', right_on='id', how='right')
    # user_history = user_data.merge(ori_movies_df, on='productSmall_id').sort_values(['like_per'], ascending=False)
    user_history = user_data.merge(ori_movies_df, left_on='productSmall_id', right_on='id', how='right').sort_values(['like_per'], ascending=False)
    print(user_history)
    print("=---")

    # 원본 영화 데이터에서 사용자가 본 영화 데이터를 제외한 데이터를 추출
    # recommendations = ori_movies_df[~ori_movies_df['productSmall_id'].isin(user_history['productSmall_id'])]
    # 사용자의 영화 평점이 높은 순으로 정렬된 데이터와 위 recommendations을 합친다.
    # print(pd.DataFrame(sorted_user_predictions).reset_index())
    # print("--")
    # print(ori_movies_df)
    recommendations = pd.DataFrame(sorted_user_predictions).reset_index()
    # 컬럼 이름 바꾸고 정렬해서 return
    recommendations = recommendations.rename(columns={user_row_number: 'Predictions'}).sort_values(
        'Predictions',
        ascending=False).iloc[:num_recommendations, :]

    return user_history, recommendations


already_rated, predictions = recommend_medias(df_svd_preds, 6, df_product, df_ratings, 10)

print(already_rated.head(10))
print(predictions)


