# 카드 소비 데이터 성별/연령대 데이터 전처리
import pandas as pd
import mysql.connector

# csv에서 파일 가져오는 코드
data = pd.read_csv('./csv/card-data_201909.csv', encoding='cp949', low_memory=False)
# print(data) # [16138860 rows x 14 columns]

new_data = data[['성별', '연령', '가맹점_시도명', '가맹점_시군구명', '가맹점_읍면동명', '가맹점업종코드']] # 열을 추출할 때는 대괄호를 한번 더 감싸야함

# '성별' 열의 내용을 수정
new_data.loc[:, '성별'] = new_data['성별'].replace({'1.남성': '1', '2.여성': '0', '3.기업': '2'})
new_data.loc[:, '연령'] = new_data['연령'].replace({'0.기타': '0', '1.10대': '10', '2.20대': '20', '3.30대': '30',
                                                '4.40대': '40', '5.50대': '50', '6.60대': '60', '7.70대이상': '70'})

# DB에 넣는 코드
# ------- 시도명, 시군구명, 읍면동 테이블
large = new_data['가맹점_시도명'].drop_duplicates()
small = new_data[['가맹점_시도명', '가맹점_시군구명', '가맹점_읍면동명']].drop_duplicates()

# local db 연결
# conn = mysql.connector.connect(host="localhost", user="c107", password="ssafy", database="adrec")
# cursor = conn.cursor()  # 커서 생성

# server db 연결
# MySQL 연결 정보 설정
db_config = {
    "host": "j9c107.p.ssafy.io",
    "user": "c107",
    "password": "c107adrec",
    "database": "adrec",
    "auth_plugin": "mysql_native_password"  # MySQL 8.0 이상일 경우에 필요한 옵션
}

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()  # 커서 생성

# 시도명 테이블에 데이터 삽입
for item in large:
    insert_query = "INSERT INTO sido (name) VALUES (%s)"
    cursor.execute(insert_query, (item,))
    conn.commit()

# 읍면동명이 맨끝에 "구"인 항목 삭제
medium = small[(small['가맹점_시군구명'] != '수원시') & (small['가맹점_시군구명'] != '안산시')
               & (small['가맹점_시군구명'] != '용인시') & (small['가맹점_시군구명'] != '창원시')
               & (small['가맹점_시군구명'] != '천안시') & (small['가맹점_시군구명'] != '전주시')]

# 시군구명 테이블에 데이터 삽입
for _, item in medium.iterrows():
    # '가맹점_시도명' 열의 NaN 값을 '세종'으로 대체
    if pd.isna(item['가맹점_시군구명']):
        item['가맹점_시군구명'] = '세종'
        print(item)

    # 대분류명을 기반으로 대분류 인덱스 검색
    select_query = "SELECT id FROM sido WHERE name = %s"
    cursor.execute(select_query, (item['가맹점_시도명'],))
    result = cursor.fetchone()

    if result:
        large_id = result[0]

        # 중분류명을 기반으로 중분류 테이블에 중복 데이터가 있는지 확인
        check_query = "SELECT id FROM sigungu WHERE name = %s AND sido_id = %s"
        cursor.execute(check_query, (item['가맹점_시군구명'], large_id))
        result = cursor.fetchone()

        # 중복 데이터가 없으면 중분류 테이블에 삽입
        if not result:
            insert_query = "INSERT INTO sigungu (sido_id, name) VALUES (%s, %s)"
            cursor.execute(insert_query, (large_id, item['가맹점_시군구명']))
            conn.commit()

# 중분류 테이블에 데이터 삽입 후 결과를 모두 소비
cursor.fetchall()

# 읍면동명이 맨끝에 "구"인 항목 삭제
medium = small[(small['가맹점_시군구명'] != '수원시') & (small['가맹점_시군구명'] != '안산시')
               & (small['가맹점_시군구명'] != '용인시') & (small['가맹점_시군구명'] != '창원시')
               & (small['가맹점_시군구명'] != '천안시') & (small['가맹점_시군구명'] != '전주시')]

# 읍면동 테이블에 데이터 삽입
for _, item in medium.iterrows():
    # '가맹점_시도명' 열의 NaN 값을 '세종'으로 대체
    if pd.isna(item['가맹점_시군구명']):
        item['가맹점_시군구명'] = '세종'

    # 대분류명을 기반으로 대분류 인덱스 검색
    select_query = "SELECT id FROM sido WHERE name = %s"
    cursor.execute(select_query, (item['가맹점_시도명'],))
    result = cursor.fetchone()

    if result:
        large_id = result[0]

        # 중분류명을 기반으로 중분류 테이블에 중복 데이터가 있는지 확인
        check_query = "SELECT id FROM sigungu WHERE name = %s AND sido_id = %s"
        cursor.execute(check_query, (item['가맹점_시군구명'], large_id))
        result = cursor.fetchone()

        # 중복 데이터가 없으면 중분류 테이블에 삽입
        if result:
            medium_id = result[0]

            # 중분류 인덱스와 소분류명을 기반으로 소분류 테이블에 중복 데이터가 있는지 확인
            check_query = "SELECT id FROM dong WHERE name = %s AND sigungu_id = %s"
            cursor.execute(check_query, (item['가맹점_읍면동명'], medium_id))
            result = cursor.fetchone()

            # 중복 데이터가 없으면 소분류 테이블에 삽입
            if not result:
                insert_query = "INSERT INTO dong (sigungu_id, name) VALUES (%s, %s)"
                cursor.execute(insert_query, (medium_id, item['가맹점_읍면동명']))
                conn.commit()

conn.commit()

# 커서와 연결 종료
cursor.close()
conn.close()

# 

