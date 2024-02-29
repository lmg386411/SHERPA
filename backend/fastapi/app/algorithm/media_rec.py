# 협업 필터링 알고리즘을 이용한 매체 추천 알고리즘 함수
import pandas as pd

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
