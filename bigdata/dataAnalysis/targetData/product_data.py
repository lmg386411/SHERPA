# 가맹점_업종분류표 데이터를 토대로 업종명 대분류, 업종명 중분류, 업종명 소분류 데이터를 전처리
import pandas as pd
import mysql.connector

# csv에서 파일 가져오는 코드
data = pd.read_csv('../csv/가맹점_업종분류표.csv', encoding='cp949', low_memory=False)
# print(data)  # [255 rows x 4 columns]

large = data['대분류'].drop_duplicates()
medium = data[['대분류', '중분류']].drop_duplicates()
small = data[['중분류', '소분류', '코드']].drop_duplicates()
print(large)
print(medium)
print(small)

# local db 연결
# conn = mysql.connector.connect(host="c107", user="root", password="ssafy", database="adrec")

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

# 대분류 테이블에 데이터 삽입
for item in large:
    insert_query = "INSERT INTO productLarge (large) VALUES (%s)"
    cursor.execute(insert_query, (item,))
    conn.commit()

# 중분류 테이블에 데이터 삽입
for _, item in medium.iterrows():
    # 대분류명을 기반으로 대분류 인덱스 검색
    select_query = "SELECT id FROM productLarge WHERE large = %s"
    cursor.execute(select_query, (item['대분류'],))
    result = cursor.fetchone()

    if result:
        large_id = result[0]

        # 중분류명을 기반으로 중분류 테이블에 중복 데이터가 있는지 확인
        check_query = "SELECT id FROM productMedium WHERE medium = %s AND productLarge_id = %s"
        cursor.execute(check_query, (item['중분류'], large_id))
        result = cursor.fetchone()

        # 중복 데이터가 없으면 중분류 테이블에 삽입
        if not result:
            insert_query = "INSERT INTO productMedium (productLarge_id, medium) VALUES (%s, %s)"
            cursor.execute(insert_query, (large_id, item['중분류']))
            conn.commit()


# 소분류 테이블에 데이터 삽입
for item in small.iterrows():
    # 중분류명을 기반으로 중분류 인덱스 검색
    select_query = "SELECT id FROM productMedium WHERE medium = %s"
    cursor.execute(select_query, (item[1]['중분류'],))
    result = cursor.fetchone()

    if result:
        medium_id = result[0]

        # 중분류 인덱스와 소분류명을 기반으로 소분류 테이블에 중복 데이터가 있는지 확인
        check_query = "SELECT id FROM productSmall WHERE small = %s AND productMedium_id = %s"
        cursor.execute(check_query, (item[1]['소분류'], medium_id))
        result = cursor.fetchone()

        # 중복 데이터가 없으면 소분류 테이블에 삽입
        if not result:
            insert_query = "INSERT INTO productSmall (productMedium_id, small, code) VALUES (%s, %s, %s)"
            cursor.execute(insert_query, (medium_id, item[1]['소분류'], item[1]['코드']))
            conn.commit()

conn.commit()

# 커서와 연결 종료
cursor.close()
conn.close()
