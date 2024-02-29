import pymysql
from datetime import datetime
import random

# 연결 설정
connection = pymysql.connect(
    host='j9c107.p.ssafy.io',
    user='c107',
    password='c107adrec',
    database='adrec'
)

# 커서 생성
cursor = connection.cursor()

# # member INSERT 쿼리 작성
# member_insert_query = "INSERT INTO member (email, name, pwd, productSmall_id) VALUES (%s,%s, %s, %s);"
# for i in range(2, 258):
#     print(i)
#     for j in range(100):
#         name = "dummy"+str(i)+"id"+str(j)
#         email = name+"@ssafy.com"
#         data_to_insert = (email, name, "1234", i)
#         cursor.execute(member_insert_query, data_to_insert)

keyword_data = {}
member_data = {}
youtubeKeyword_data = []


# youtubeKeyword SELECT 쿼리 실행
youtubeKeyword_selsect_query = "SELECT * FROM youtubeKeyword;"
cursor.execute(youtubeKeyword_selsect_query)
# 결과 가져오기
keywords_sql_data = cursor.fetchall()
for row in keywords_sql_data:
    youtubeKeyword_data.append(row[1])


# member SELECT 쿼리 실행
member_selsect_query = "SELECT * FROM member;"
cursor.execute(member_selsect_query)
# 결과 가져오기
members_sql_data = cursor.fetchall()
for row in members_sql_data:
    if row[5] == None:
        continue
    if row[5] in member_data:
        member_data[row[5]].append(row[0])
    else:
        member_data[row[5]] = []
        member_data[row[5]].append(row[0])
        keyword_data[row[5]] = youtubeKeyword_data


# adKeyword SELECT 쿼리 실행
adKeyword_selsect_query = "SELECT * FROM adKeyword;"
cursor.execute(adKeyword_selsect_query)
# 결과 가져오기
adKeywords_sql_data = cursor.fetchall()
for row in adKeywords_sql_data:
    if row[3] in keyword_data:
        keyword_data[row[3]].append(row[1])
    else:
        keyword_data[row[3]] = youtubeKeyword_data
        keyword_data[row[3]].append(row[1])


rec_date = ["2023-10-01", "2023-9-30", "2023-9-29", "2023-9-28", "2023-9-27", "2023-9-26",
            "2023-9-25", "2023-9-24", "2023-9-23", "2023-9-22", "2023-9-21", "2023-9-20"]
# # keywordRec INSERT 쿼리 작성
# keywordRec_insert_query = "INSERT INTO keywordRec (productSmall_id, member_id, recDate) VALUES (%s, %s, %s);"
# for k, v in member_data.items():
#     for m in v:
#         for d in rec_date:
#             data_to_insert = (k, m, d)
#             cursor.execute(keywordRec_insert_query, data_to_insert)

keywordRec_data = {}
# keywordRec SELECT 쿼리 실행

productSmall_id_value = 25
# SELECT 쿼리로 productSmall_id를 플레이스홀더로 대체
keywordRec_selsect_query = "SELECT * FROM keywordRec WHERE productSmall_id = %s;"
cursor.execute(keywordRec_selsect_query, (productSmall_id_value,))
# keywordRec_selsect_query = "SELECT * FROM keywordRec WHERE productSmall_id = 187 and member_id = 53;"
# cursor.execute(keywordRec_selsect_query)
# 결과 가져오기
keywordRec_sql_data = cursor.fetchall()
for row in keywordRec_sql_data:

    if row[2] in keywordRec_data:
        keywordRec_data[row[2]].append(row[0])
    else:
        keywordRec_data[row[2]] = []
        keywordRec_data[row[2]].append(row[0])


# keywordLike INSERT 쿼리 작성
keywordLike_insert_query = "INSERT INTO keywordLike (keywordRec_id, keyword) VALUES (%s,%s);"
for k, rec_id_list in keywordRec_data.items():
    size = len(rec_id_list)
    random_keyword = random.sample(keyword_data[productSmall_id_value], size*5)
    random_keyword_idx = 0
    for id in rec_id_list:
        for j in range(5):
            data_to_insert = (id, random_keyword[random_keyword_idx])
            cursor.execute(keywordLike_insert_query, data_to_insert)
            random_keyword_idx += 1


# 변경사항을 커밋
connection.commit()

# 커서 닫기
cursor.close()

# 연결 닫기
connection.close()
