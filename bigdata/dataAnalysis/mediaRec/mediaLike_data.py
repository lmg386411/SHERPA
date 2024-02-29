# 매체 호감 데이터 전처리한 csv 파일 서버에 넣는 코드
import pandas as pd
import mysql.connector

# csv에서 파일 가져오는 코드
data_gender = pd.read_csv('../csv/매체호감-성별.CSV', encoding='cp949', low_memory=False)
# print(data_gender)  # [16 rows x 5 columns]
data_age = pd.read_csv('../csv/매체호감-연령.CSV', encoding='cp949', low_memory=False)
# print(data_age)  # [40 rows x 5 columns]
data_area = pd.read_csv('../csv/매체호감-지역.CSV', encoding='cp949', low_memory=False)
print(data_area)  # [56 rows x 5 columns]

# local db 연결
# conn = mysql.connector.connect(host="localhost", user="root", password="ssafy", database="adrec")

# server db 연결
# MySQL 연결 정보 설정
db_config = {
    "host": "j9c107.p.ssafy.io",
    "user": "c107",
    "password": "c107adrec",
    "database": "adrec",
    "auth_plugin": "mysql_native_password"  # MySQL 8.0 이상일 경우에 필요한 옵션
}

# MySQL에 연결
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()  # 커서 생성

# 매체-호감-성별 테이블에 데이터 삽입
for _, item in data_gender.iterrows():
    # print(item['id'])
    if item['mediaType_id'] < 6:
        insert_query = "INSERT INTO mediaLikeGender (gender, total, mediaType_id) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (item['gender'], item['total'], item['mediaType_id']))
        conn.commit()
    else:
        insert_query = "INSERT INTO mediaLikeGender (gender, total, mediaType_id, mediaSub_id) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert_query, (item['gender'], item['total'], item['mediaType_id'], item['mediaSub_id']))
        conn.commit()

# 매체-호감-연령 테이블에 데이터 삽입
for _, item in data_age.iterrows():
    # print(item['id'])
    if item['mediaType_id'] < 6:
        insert_query = "INSERT INTO mediaLikeAge (age, total, mediaType_id) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (item['age'], item['total'], item['mediaType_id']))
        conn.commit()
    else:
        insert_query = "INSERT INTO mediaLikeAge (age, total, mediaType_id, mediaSub_id) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert_query, (item['age'], item['total'], item['mediaType_id'], item['mediaSub_id']))
        conn.commit()

# 매체-호감-지역 테이블에 데이터 삽입
for _, item in data_area.iterrows():
    # print(item['id'])
    if item['mediaType_id'] < 6:
        insert_query = "INSERT INTO mediaLikeArea (area, total, mediaType_id) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (item['area'], item['total'], item['mediaType_id']))
        conn.commit()
    else:
        insert_query = "INSERT INTO mediaLikeArea (area, total, mediaType_id, mediaSub_id) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert_query, (item['area'], item['total'], item['mediaType_id'], item['mediaSub_id']))
        conn.commit()

conn.commit()

# 커서와 연결 종료
cursor.close()
conn.close()
