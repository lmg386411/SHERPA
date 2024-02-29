import pandas as pd
import mysql.connector

# 전처리
subway_csv = pd.read_csv("./csv/subway.csv", thousands = ',')

# 시간대 열만 추출
time_columns = subway_csv.columns[4:-1]
print(time_columns)
subway_csv[time_columns] = subway_csv[time_columns].apply(pd.to_numeric)

# 시간대 총합 구하기
subway_sum = subway_csv[time_columns].sum(axis=1)
print(subway_sum)
subway_csv.loc[:, '총합'] = subway_sum
print(subway_csv)

# 시간대 데이터 삭제
subway_data = subway_csv.drop(subway_csv.columns[4:23], axis=1)

# 역번호, 역명 추출
station_info = subway_data[['역번호', '역명']]
station_info = station_info.drop_duplicates(subset='역번호').reset_index(drop=True)

# 역번호 별로 승하차 수 총합
subway_data_group = subway_data.groupby('역번호')['총합'].sum().reset_index()

# 역번호, 역명, 총합 모음
result_df = pd.concat([subway_data_group, station_info], axis=1)
final_result = result_df.iloc[:, 1:4]

# 컬럼 순서 변경
final_result = final_result[['역번호', '역명', '총합']]

# 총합 순으로 정렬
final_result_sorted = final_result.sort_values(by='총합', ascending=False)

print(final_result_sorted)

# DB에 넣기

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

# subway 테이블에 삽입
for _, item in final_result_sorted.iterrows():
    print(item)
    insert_query = "INSERT INTO subway (name, total) VALUES (%s, %s)"
    cursor.execute(insert_query, (item['역명'], item['총합']))

conn.commit()
