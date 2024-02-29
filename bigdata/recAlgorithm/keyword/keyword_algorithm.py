import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# 사용자 데이터 정의 (영화를 본 경우 1, 안 본 경우 0)
data = {
    "user1": ["단어3", "단어5", "단어6"],
    "user2": ["단어1", "단어2", "단어4"],
    "user3": ["단어2", "단어4", "단어6"],
    "user4": ["단어1", "단어3", "단어5"],
    "user5": ["단어1", "단어2", "단어3"],
    "user6": ["단어4", "단어5", "단어6"],
    "target": ["단어1", "단어2"],
}

# Target 사용자 데이터 정의
target = ["단어1", "단어2"]

# 모든 영화 목록 가져오기
movies = list(set([movie for user_movies in data.values()
              for movie in user_movies]))
movies.sort()
# 각 사용자의 영화 관람 여부를 이진 벡터로 변환
binary_vectors = []
for user_movies in data.values():
    binary_vector = [1 if movie in user_movies else 0 for movie in movies]
    binary_vectors.append(binary_vector)

# Target 사용자의 영화 관람 여부를 이진 벡터로 변환
target_vector = [1 if movie in target else 0 for movie in movies]

# 데이터를 행렬 형태로 변환
movie_matrix = np.array(binary_vectors)
print(movie_matrix)

# Target 사용자의 유사도 계산
target_similarity = cosine_similarity([target_vector], movie_matrix)[0]

# 유사도가 높은 순으로 영화 추천
user_similarities = list(zip(data.keys(), target_similarity))
user_similarities.sort(key=lambda x: x[1], reverse=True)
print(user_similarities)
recommendations = {}

for value in user_similarities:
    for keyword in data[value[0]]:
        if keyword in recommendations:
            recommendations[keyword] += value[1]
        else:
            recommendations[keyword] = value[1]

# 값을 기준으로 딕셔너리 정렬
sorted_recommendations = dict(
    sorted(recommendations.items(), key=lambda item: item[1], reverse=True))
idx = 1
for key, value in sorted_recommendations.items():
    if key in target:
        continue
    print(f"{idx}위 : {key}")
    idx += 1


# import numpy as np
# import pymysql

# from sklearn.metrics.pairwise import cosine_similarity

# memberName = "name"
# productSmallId = 2

# # DB 연결
# db_config = {
#     "host": "j9c107.p.ssafy.io",
#     "user": "c107",
#     "password": "c107adrec",
#     "database": "adrec"
# }

# conn = pymysql.connect(**db_config)
# cursor = conn.cursor()

# member_select_query = "SELECT * FROM member WHERE name = %s"
# cursor.execute(member_select_query, (memberName))
# member_query_result = cursor.fetchall()

# member_id = member_query_result[0][0]

# keywordRec_select_query = "SELECT * FROM keywordRec WHERE productSmall_id = %s"
# cursor.execute(keywordRec_select_query, (productSmallId))
# keywordRec_query_result = cursor.fetchall()

# data = {}

# keywordLike_select_query = "SELECT * FROM keywordLike WHERE keywordRec_id = %s"

# for row in keywordRec_query_result:
#     if row[2]== member_id:
#         continue
#     if row[2] in data:
#         cursor.execute(keywordLike_select_query, (row[0]))
#         keywordLike_query_result = cursor.fetchall()
#         for r in keywordLike_query_result:
#             data[row[2]].append(r[1])
#     else:
#         data[row[2]]=[]
#         cursor.execute(keywordLike_select_query, (row[0]))
#         keywordLike_query_result = cursor.fetchall()
#         for r in keywordLike_query_result:
#             data[row[2]].append(r[1])

# target= []
# target_keywordRec_select_query = "SELECT * FROM keywordRec WHERE member_id = %s"
# cursor.execute(target_keywordRec_select_query, (member_id))
# target_keywordRec_select_query = cursor.fetchall()

# for row in target_keywordRec_select_query:
#     cursor.execute(keywordLike_select_query, (row[0]))
#     target_keywordLike_query_result = cursor.fetchall()
#     for r in target_keywordLike_query_result:
#         target.append(r[1])


# # 모든 키워드 목록 가져오기
# keywords = list(set([keyword for user_keywords in data.values() for keyword in user_keywords]))
# keywords.extend(target)
# keywords = list(set(keywords))
# keywords.sort()
# # 각 사용자의 키워드 좋아요 여부를 이진 벡터로 변환
# binary_vectors = []
# for user_keywords in data.values():
#     binary_vector = [1 if keyword in user_keywords else 0 for keyword in keywords]
#     binary_vectors.append(binary_vector)

# # Target 사용자의 키워드 좋아요 여부를 이진 벡터로 변환
# target_vector = [1 if keyword in target else 0 for keyword in keywords]

# # 데이터를 행렬 형태로 변환
# keyword_matrix = np.array(binary_vectors)

# # Target 사용자의 유사도 계산
# target_similarity = cosine_similarity([target_vector], keyword_matrix)[0]

# user_similarities = list(zip(data.keys(), target_similarity))
# user_similarities.sort(key=lambda x: x[1], reverse=True)

# recommendations={}

# for value in user_similarities:
#     for keyword in data[value[0]]:
#         if keyword in recommendations:
#             recommendations[keyword] +=value[1]
#         else:
#             recommendations[keyword] =value[1]

# # 값을 기준으로 딕셔너리 정렬
# sorted_recommendations = dict(sorted(recommendations.items(), key=lambda item: item[1], reverse=True))

# idx =0
# for key, value in sorted_recommendations.items():
#     if idx == 5:
#         break
#     if key in target:
#         continue
#     print(f"{idx + 1}위 :{key}")
#     idx+=1
