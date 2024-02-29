import os
import pymysql
import pandas as pd

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
folder_path = 'data/trendKeyword/'

# 폴더 내의 모든 파일 목록 가져오기
file_list = os.listdir(folder_path)

# XLSX 파일만 선택
xlsx_files = [file for file in file_list if file.endswith('.xlsx')]


data = {}
total_data = 0
for xlsx_file in xlsx_files:
    file_path = os.path.join(folder_path, xlsx_file)
    df = pd.read_excel(file_path)

    for row_num, row in df.iterrows():
        total_data += 1
        data_key = row["tmng"]

        if data_key == "- topic":
            data_key = "topic"

        if data_key in data:
            data[data_key] += 1
        else:
            data[data_key] = 1


sql_data = {
    'name': [],
    'total': [],
}
idx = 0
for key, value in data.items():
    idx += 1
    sql_data['name'].append(key)
    sql_data['total'].append(value)

print('total_data : ', total_data)
print('idx : ', idx)

# INSERT 쿼리 작성
insert_query = "INSERT INTO youtubeKeyword (name, total) VALUES (%s, %s)"

# INSERT 쿼리 실행 (데이터는 튜플로 전달)
for i in range(idx):
    data_to_insert = (sql_data['name'][i], sql_data['total'][i])
    cursor.execute(insert_query, data_to_insert)


# 변경사항을 커밋
connection.commit()

# 커서 닫기
cursor.close()

# 연결 닫기
connection.close()
