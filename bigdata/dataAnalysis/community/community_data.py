# 전처리한 커뮤니티 csv 파일 서버에 넣기
import pandas as pd
import mysql.connector

# csv에서 파일 가져오기
data_gender = pd.read_csv('./csv/커뮤니티-성별.csv', encoding='cp949', low_memory=False)
# print(data_gender)  # [16 rows x 5 columns]
data_age = pd.read_csv('./csv/커뮤니티-연령.csv', encoding='cp949', low_memory=False)
# print(data_age)  # [40 rows x 5 columns]
data_area = pd.read_csv('./csv/커뮤니티-지역.csv', encoding='cp949', low_memory=False)
print(data_area)  # [56 rows x 5 columns]

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

# 커뮤니티-성별 테이블에 데이터 삽입
for _, item in data_gender.iterrows():
    print(item)
    insert_query = "INSERT INTO communityGender (gender, name, total, year) VALUES (%s, %s, %s, %s)"
    cursor.execute(insert_query, (item['gender'], item['name'], item['total'], item['year']))
    conn.commit()

# 커뮤니티-연령 테이블에 데이터 삽입
for _, item in data_age.iterrows():
    insert_query = "INSERT INTO communityAge (age, name, total, year) VALUES (%s, %s, %s, %s)"
    cursor.execute(insert_query, (item['age'], item['name'], item['total'], item['year']))
    conn.commit()


# 커뮤니티-지역 테이블에 데이터 삽입
for _, item in data_area.iterrows():
    insert_query = "INSERT INTO communityArea (area, name, total, year) VALUES (%s, %s, %s, %s)"
    cursor.execute(insert_query, (item['area'], item['name'], item['total'], item['year']))
    conn.commit()

conn.commit()

# 커서와 연결 종료
cursor.close()
conn.close()
