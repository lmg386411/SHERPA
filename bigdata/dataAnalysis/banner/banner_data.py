import pandas as pd
import mysql.connector

banner_east = pd.read_csv('./csv/동구.csv', encoding='cp949', low_memory=False)
banner_west = pd.read_csv('./csv/서구.csv', encoding='cp949', low_memory=False)
banner_south = pd.read_csv('./csv/남구.csv', encoding='cp949', low_memory=False)
banner_north = pd.read_csv('./csv/북구.csv', encoding='cp949', low_memory=False)
banner_gwangsan = pd.read_csv('./csv/광산구.csv', encoding='cp949', low_memory=False)

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

query = """SELECT dong.id,dong.name, sigungu.name
            FROM dong
            JOIN sigungu ON dong.sigungu_id = sigungu.id
            WHERE dong.sigungu_id in (112,113,114,115,116);"""

cursor.execute(query)

address_data = {}

# 결과 가져오기
address = cursor.fetchall()
for row in address:
    if row[2] in address_data:
        address_data[row[2]][row[1]] = row[0]
    else:
        address_data[row[2]] = {}
        address_data[row[2]][row[1]] = row[0]


# 동 아이디 연결

dong_id = []
for row_num, row in banner_north.iterrows():
    gu = row['구']
    dong = row['동']
    dong_id.append(address_data[gu][dong])

dong_id_df = pd.DataFrame(dong_id)

result = pd.concat([banner_north, dong_id_df], axis=1, ignore_index=True)
result.columns=['name', 'address', 'dong', 'gu', 'id']

# 테이블에 데이터 삽입
for _, item in result.iterrows():
    insert_query = "INSERT INTO banner (dong_id, name, address) VALUES (%s, %s, %s)"
    cursor.execute(insert_query, (item['id'], item['name'], item['address']))

conn.commit();
