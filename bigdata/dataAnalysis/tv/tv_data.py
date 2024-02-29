# TV 방송 프로그램 성별/연령별/지역별 시청 여부 데이터 전처리한 csv 파일 서버에 넣는 코드
# 연령별 TV이용 시간대 데이터 전처리한 csv 파일 서버에 넣는 코드
import pandas as pd
import mysql.connector

# csv에서 파일 가져오는 코드
data_age = pd.read_csv('../csv/tvAge.csv', encoding='cp949', low_memory=False)
# print(data_age)  # [161 rows x 4 columns]
data_area = pd.read_csv('../csv/tvArea.csv', encoding='cp949', low_memory=False)
# print(data_area)  # [161 rows x 4 columns]
data_gender = pd.read_csv('../csv/tvGender.csv', encoding='cp949', low_memory=False)
# print(data_gender)  # [46 rows x 4 columns]
data_timeline = pd.read_csv('../csv/tvTimeline.csv', encoding='cp949', low_memory=False)
print(data_timeline)  # [336 rows x 4 columns]

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

# TV 시청-성별 테이블에 데이터 삽입
for _, item in data_gender.iterrows():
    rounded_total = round(item['total'], 0)
    insert_query = "INSERT INTO tvGender (gender, genre, is_free, total) VALUES (%s, %s, %s, %s)"
    cursor.execute(insert_query, (item['gender'], item['genre'], item['is_free'], rounded_total))
    conn.commit()

# TV 시청-연령 테이블에 데이터 삽입
for _, item in data_age.iterrows():
    rounded_total = round(item['total'], 0)
    insert_query = "INSERT INTO tvAge (age, genre, is_free, total) VALUES (%s, %s, %s, %s)"
    cursor.execute(insert_query, (item['age'], item['genre'], item['is_free'], rounded_total))
    conn.commit()

# TV 시청-지역 테이블에 데이터 삽입
for _, item in data_area.iterrows():
    rounded_total = round(item['total'], 0)
    insert_query = "INSERT INTO tvArea (area, genre, is_free, total) VALUES (%s, %s, %s, %s)"
    cursor.execute(insert_query, (item['area'], item['genre'], item['is_free'], rounded_total))
    conn.commit()

# TV 이용 시간대 테이블에 데이터 삽입
for _, item in data_timeline.iterrows():
    rounded_total = round(item['total'], 0)
    time_value = int(item['time'].split(':')[0])
    insert_query = "INSERT INTO tvTime (age, is_weekday, time, total) VALUES (%s, %s, %s, %s)"
    cursor.execute(insert_query, (item['age'], item['is_weekday'], time_value, rounded_total))
    conn.commit()

conn.commit()

# 커서와 연결 종료
cursor.close()
conn.close()
