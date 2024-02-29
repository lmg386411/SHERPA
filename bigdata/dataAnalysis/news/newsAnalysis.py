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
file_path = 'data/news/신문 데이터.xlsx'

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


df = pd.read_excel(file_path)
# print("=====================\n")

total_data = 0
idx_gender = 0
idx_area = 0
idx_age = 0

per_int = 10

for row_num, row in df.iterrows():
    total_data += 1
    name = row["신문사"]

    if name == '사례수':
        pass
    else:

        idx_gender += 2
        idx_age += 6
        idx_area += 8

        sql_data_gender['name'].append(name)
        sql_data_gender['gender'].append(0)
        sql_data_gender['total'].append(round(row['여성']*per_int))

        sql_data_gender['name'].append(name)
        sql_data_gender['gender'].append(1)
        sql_data_gender['total'].append(round(row['남성']*per_int))

        sql_data_age['name'].append(name)
        sql_data_age['age'].append(20)
        sql_data_age['total'].append(round(row['20대']*per_int))

        sql_data_age['name'].append(name)
        sql_data_age['age'].append(30)
        sql_data_age['total'].append(round(row['30대']*per_int))

        sql_data_age['name'].append(name)
        sql_data_age['age'].append(40)
        sql_data_age['total'].append(round(row['40대']*per_int))

        sql_data_age['name'].append(name)
        sql_data_age['age'].append(50)
        sql_data_age['total'].append(round(row['50대']*per_int))

        sql_data_age['name'].append(name)
        sql_data_age['age'].append(60)
        sql_data_age['total'].append(round(row['60대']*per_int))

        sql_data_age['name'].append(name)
        sql_data_age['age'].append(70)
        sql_data_age['total'].append(round(row['70대']*per_int))

        sql_data_area['name'].append(name)
        sql_data_area['area'].append('서울')
        sql_data_area['total'].append(round(row['서울']*per_int))

        sql_data_area['name'].append(name)
        sql_data_area['area'].append('인천/경기')
        sql_data_area['total'].append(round(row['인천/경기']*per_int))

        sql_data_area['name'].append(name)
        sql_data_area['area'].append('대전/세종/충청')
        sql_data_area['total'].append(round(row['대전/세종/충청']*per_int))

        sql_data_area['name'].append(name)
        sql_data_area['area'].append('광주/전라')
        sql_data_area['total'].append(round(row['광주/전라']*per_int))

        sql_data_area['name'].append(name)
        sql_data_area['area'].append('대구/경북')
        sql_data_area['total'].append(round(row['대구/경북']*per_int))

        sql_data_area['name'].append(name)
        sql_data_area['area'].append('부산/울산/경남')
        sql_data_area['total'].append(round(row['부산/울산/경남']*per_int))

        sql_data_area['name'].append(name)
        sql_data_area['area'].append('강원')
        sql_data_area['total'].append(round(row['강원']*per_int))

        sql_data_area['name'].append(name)
        sql_data_area['area'].append('제주')
        sql_data_area['total'].append(round(row['제주']*per_int))

# print('total_data : ', total_data)
# print('idx_gender : ', idx_gender)
# print('idx_age : ', idx_age)
# print('idx_area : ', idx_area)


# INSERT 쿼리 작성
insert_query_gender = "INSERT INTO newsGender (gender, name, total) VALUES (%s,%s, %s)"
for i in range(idx_gender):
    data_to_insert = (
        sql_data_gender['gender'][i], sql_data_gender['name'][i], sql_data_gender['total'][i])
    cursor.execute(insert_query_gender, data_to_insert)

# INSERT 쿼리 작성
insert_query_age = "INSERT INTO newsAge (age, name, total) VALUES (%s,%s, %s)"
for i in range(idx_age):
    data_to_insert = (
        sql_data_age['age'][i], sql_data_age['name'][i], sql_data_age['total'][i])
    cursor.execute(insert_query_age, data_to_insert)

# INSERT 쿼리 작성
insert_query_area = "INSERT INTO newsArea (area, name, total) VALUES (%s, %s, %s)"
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
