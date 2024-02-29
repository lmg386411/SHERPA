import pandas as pd
import pymysql


# 연결 설정
connection = pymysql.connect(
    host='j9c107.p.ssafy.io',
    user='c107',
    password='c107adrec',
    database='adrec'
)

# 커서 생성
cursor = connection.cursor()

# 폴더 경로 설정
file_path = 'data/newsTheme/신문__분야별.xlsx'

data = {
    '정치': {},
    '사회': {},
    '경제': {},
    '문화': {},
    '스포츠 및 연예': {},
    '기타': {},
}
df = pd.read_excel(file_path)
total_data = 0
for row_num, row in df.iterrows():
    total_data += 1
    key = row['행정구역별(1)']
    data['정치'][key] = round(row['정치'])
    data['사회'][key] = round(row['사회'])
    data['경제'][key] = round(row['경제'])
    data['문화'][key] = round(row['문화'])
    data['스포츠 및 연예'][key] = round(row['스포츠 및 연예'])
    data['기타'][key] = round(row['기타'])

sql_data_gender = {
    'gender': [],
    'name': [],
    'total': [],
}
sql_data_age = {
    'age': [],
    'name': [],
    'total': [],
}
sql_data_area = {
    'area': [],
    'name': [],
    'total': [],
}


idx_gender = 0
idx_area = 0
idx_age = 0

per_int = 10

for key, value in data.items():
    for k, v in value.items():

        if type(k) == str:
            idx_area += 1
            sql_data_area['name'].append(key)
            sql_data_area['area'].append(k)
            sql_data_area['total'].append(v*per_int)

        else:
            if k == 0 or k == 1:
                idx_gender += 1
                sql_data_gender['name'].append(key)
                sql_data_gender['gender'].append(k)
                sql_data_gender['total'].append(v*per_int)
            else:
                idx_age += 1
                sql_data_age['name'].append(key)
                sql_data_age['age'].append(k)
                sql_data_age['total'].append(v*per_int)


# print('total_data : ', total_data)
# print('idx_gender : ', idx_gender)
# print('idx_age : ', idx_age)
# print('idx_area : ', idx_area)

# INSERT 쿼리 작성
insert_query_gender = "INSERT INTO newsThemeGender (gender, theme, total) VALUES (%s,%s, %s)"
for i in range(idx_gender):
    data_to_insert = (
        sql_data_gender['gender'][i], sql_data_gender['name'][i], sql_data_gender['total'][i])
    cursor.execute(insert_query_gender, data_to_insert)

# INSERT 쿼리 작성
insert_query_age = "INSERT INTO newsThemeAge (age, theme, total) VALUES (%s,%s, %s)"
for i in range(idx_age):
    data_to_insert = (
        sql_data_age['age'][i], sql_data_age['name'][i], sql_data_age['total'][i])
    cursor.execute(insert_query_age, data_to_insert)

# INSERT 쿼리 작성
insert_query_area = "INSERT INTO newsThemeArea (area, theme, total) VALUES (%s, %s, %s)"
for i in range(idx_area):
    data_to_insert = (
        sql_data_area['area'][i], sql_data_area['name'][i], sql_data_area['total'][i])
    cursor.execute(insert_query_area, data_to_insert)


# 변경사항을 커밋
connection.commit()

# 커서 닫기
cursor.close()

# 연결 닫기
connection.close()
