# 성별 / 연령별 라디오 유형별 시청률 데이터 전처리한 csv 파일 서버에 넣는 코드
# 연령별 라디오 시청 시간 데이터 전처리한 csv 파일 서버에 넣는 코드
import pandas as pd
import mysql.connector

# csv에서 파일 가져오는 코드
data_age = pd.read_csv('../csv/radioAge.csv', encoding='cp949', low_memory=False)
# print(data_age)  # [54 rows x 3 columns]
data_area = pd.read_csv('../csv/radioArea.csv', encoding='cp949', low_memory=False)
# print(data_area)  # [72 rows x 3 columns]
data_gender = pd.read_csv('../csv/radioGender.csv', encoding='cp949', low_memory=False)
# print(data_gender)  # [17 rows x 3 columns]
data_timeline = pd.read_csv('../csv/radioTimeline.csv', encoding='cp949', low_memory=False)
# print(data_timeline)  # [336 rows x 4 columns]

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

# 라디오-성별 테이블에 데이터 삽입
# for _, item in data_gender.iterrows():
#     rounded_total = round(item['total'], 0)
#     insert_query = "INSERT INTO radioGender (gender, total, genre) VALUES (%s, %s, %s)"
#     cursor.execute(insert_query, (item['gender'], rounded_total, item['genre']))
#     conn.commit()

# 라디오-연령 테이블에 데이터 삽입
for _, item in data_age.iterrows():
    rounded_total = round(item['total'], 0)
    insert_query = "INSERT INTO radioAge (age, total, genre) VALUES (%s, %s, %s)"
    cursor.execute(insert_query, (item['age'], rounded_total, item['genere']))
    conn.commit()

# 라디오-지역 테이블에 데이터 삽입
for _, item in data_area.iterrows():
    rounded_total = round(item['total'], 0)
    insert_query = "INSERT INTO radioArea (area, total, genre) VALUES (%s, %s, %s)"
    cursor.execute(insert_query, (item['area'], rounded_total, item['genre']))
    conn.commit()

# 라디오 시간대 테이블에 데이터 삽입
for _, item in data_timeline.iterrows():
    rounded_total = round(item['total'], 0)
    time_value = int(item['time'].split(':')[0])
    insert_query = "INSERT INTO radioTime (age, is_weekday, time, total) VALUES (%s, %s, %s, %s)"
    cursor.execute(insert_query, (item['age'], item['is_weekday'], time_value, rounded_total))
    conn.commit()

conn.commit()

# 커서와 연결 종료
cursor.close()
conn.close()
