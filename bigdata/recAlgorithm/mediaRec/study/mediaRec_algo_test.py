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

productMedia_total = productMedia.pivot_table(
    index=["mediaType_id", "mediaSub_id"],
    columns=["productSmall_id"],
    values=["like_per"]).fillna(0)
# print(productMedia_total)  # [6 rows x 64 columns]

productMedia_total.to_csv('./csv/productMedia_total.csv')

# csv에서 파일 가져오는 코드
# print(productLargeMediumSmall)
productLargeMediumSmall.to_csv('./csv/product.csv')

# 하나의 품목에 대해 비슷한 품목을 추천

# SVD 사용 12개의 컴포넌트로 차원을 축소
SVD = TruncatedSVD(n_components=12)
matrix = SVD.fit_transform(productMedia_total)
# matrix.shape
# print(matrix[0])

# 피어슨 상관 계수 구하기
corr = np.corrcoef(matrix)
# corr.shape

corr2 = corr[:200, :200]
# corr2.shape

plt.figure(figsize=(16, 10))
sns.heatmap(corr2)

product_media = productMedia_total.columns
product_media_list = list(product_media)
print(product_media_list)

# coffey_hands = product_media_list.index('like_per')
# corr_coffey_hands  = corr[coffey_hands]
# list(movie_title[(corr_coffey_hands >= 0.9)])[:50]

# 한 매체에 품목 추천?