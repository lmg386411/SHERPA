# 전처리한 커뮤니티 csv 파일 서버에 넣기
import pandas as pd
import mysql.connector

# csv에서 파일 가져오기
data_category_result = pd.read_csv('./csv/category_result.csv', encoding='utf-8-sig', low_memory=False)
data_category_result = data_category_result.dropna()
print(data_category_result)

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
for _, item in data_category_result.iterrows():
    print(item)
    insert_query = "INSERT INTO communityTheme (theme, theme_sub, title_post, text, name_author, url, img) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(insert_query, (item['category'], item['category_sub'], item['title_post'], item['text'], item['name_author'], item['author_href'], item['img_author_src']))

conn.commit()

# csv에서 파일 가져오기
allProductSmall_category = pd.read_csv('./csv/allProductSmall_category.csv', encoding='cp949', low_memory=False)
print(allProductSmall_category)

allProductSmall_category.columns = ['name', 'category']

allProductSmall_category["name"] = allProductSmall_category["name"].str.replace(pat=r'[^\w]', repl=r'', regex=True)
print(allProductSmall_category)

print(allProductSmall_category.columns)
# 커뮤니티-성별 테이블에 데이터 삽입
for _, item in allProductSmall_category.iterrows():
    print(item)
    insert_query = "INSERT INTO productSmallCategory (small, category) VALUES (%s, %s)"
    cursor.execute(insert_query, (item['name'], item['category']))

conn.commit()

# 커서와 연결 종료
cursor.close()
conn.close()
