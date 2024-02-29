# 카드 소비 데이터 성별/연령대 데이터 전처리
import pandas as pd
import mysql.connector
import os

# 여러 CSV 파일을 순회하면서 데이터를 가져오고 합치는 작업
csv_files = ['card-data_201909.csv', 'card-data_201910.csv', 'card-data_201911.csv', 'card-data_201912.csv']
merged_data = pd.DataFrame()  # 빈 데이터프레임을 생성하여 데이터를 계속 추가할 것입니다.

for csv_file in csv_files:
    file_path = os.path.join('../csv', csv_file)
    data = pd.read_csv(file_path, encoding='cp949', low_memory=False)

    # 1. 데이터 전처리 코드
    new_data = data[['성별', '연령', '가맹점_시도명', '가맹점_시군구명', '가맹점_읍면동명', '가맹점업종코드']]  # 열을 추출할 때는 대괄호를 한번 더 감싸야함

    # 1-1. '성별' 열의 내용을 수정
    new_data.loc[:, '성별'] = new_data['성별'].replace({'1.남성': 1, '2.여성': 0, '3.기업': 2, '0.기타': 3})
    new_data.loc[:, '연령'] = new_data['연령'].replace({'0.기타': '0', '1.10대': '10', '2.20대': '20', '3.30대': '30',
                                                    '4.40대': '40', '5.50대': '50', '6.60대': '60', '7.70대이상': '70'})

    # 1-2. 읍면동명이 맨끝에 "구"인 항목 삭제
    new_data = new_data[(new_data['가맹점_시군구명'] != '수원시') & (new_data['가맹점_시군구명'] != '안산시')
                        & (new_data['가맹점_시군구명'] != '용인시') & (new_data['가맹점_시군구명'] != '창원시')
                        & (new_data['가맹점_시군구명'] != '천안시') & (new_data['가맹점_시군구명'] != '전주시')]

    for idx, item in new_data.iterrows():
        print(idx)
        # '가맹점_시도명' 열의 NaN 값을 '세종'으로 대체
        if pd.isna(item['가맹점_시군구명']):
            new_data.at[idx, '가맹점_시군구명'] = '세종'

    # 2. 데이터를 merged_data에 추가
    merged_data = pd.concat([merged_data, new_data])

print(merged_data)

# 3. 데이터 합치기: 'total' 값 추출
# 성별, 연령, 가맹점 업종코드, 가맹점 위치(지역)가 모두 같은 항목들을 그룹화하고 각 그룹의 크기를 계산하여 'total' 열에 저장
merged_data['total'] = merged_data.groupby(['성별', '연령', '가맹점업종코드', '가맹점_시도명', '가맹점_시군구명', '가맹점_읍면동명'])['성별'].transform('count')
merged_data = merged_data[['성별', '연령', '가맹점업종코드', '가맹점_시도명', '가맹점_시군구명', '가맹점_읍면동명', 'total']].drop_duplicates()
print(merged_data)

# 4. DB에 넣는 코드 - target 테이블
# # local db 연결
# conn = mysql.connector.connect(host="localhost", user="root", password="ssafy", database="adrec")
# cursor = conn.cursor()  # 커서 생성

# server db 연결
db_config = {
    "host": "j9c107.p.ssafy.io",
    "user": "c107",
    "password": "c107adrec",
    "database": "adrec",
    "auth_plugin": "mysql_native_password"  # MySQL 8.0 이상일 경우에 필요한 옵션
}

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()  # 커서 생성

# 읍면동 아이디 가져오기
for _, item in merged_data.iterrows():
    print(_)

    # '가맹점_시도명' 열의 NaN 값을 '세종'으로 대체
    # if pd.isna(item['가맹점_시군구명']):
    #     item['가맹점_시군구명'] = '세종'

    # 성별 - 기타는 제거
    if pd.isna(item['성별']) or item['성별'] >= 2:
        continue

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
            if result:
                dong_id = result[0]

                # 업종코드
                # 중분류 인덱스와 소분류명을 기반으로 소분류 테이블에 중복 데이터가 있는지 확인
                check_query = "SELECT id FROM productSmall WHERE code = %s"
                cursor.execute(check_query, (item['가맹점업종코드'],))

                productsmall_id = cursor.fetchone()[0]

                # nan 값 처리
                if pd.isna(item['성별']) or pd.isna(item['연령']) or pd.isna(item['total']) or pd.isna(productsmall_id) or pd.isna(dong_id):
                    print(item)
                    continue

                insert_query = "INSERT INTO target (gender, age, productSmall_id, dong_id, total) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(insert_query, (item['성별'], item['연령'], productsmall_id, dong_id, item['total'],))
                conn.commit()

conn.commit()

# 커서와 연결 종료
cursor.close()
conn.close()

