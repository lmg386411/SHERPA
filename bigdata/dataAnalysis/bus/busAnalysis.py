import os
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

# SQL 쿼리 실행
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

data = {}

csv_path_bus_addressr = 'data/bus/버스정류장_주소_데이터.csv'
csv_file_bus_address = pd.read_csv(csv_path_bus_addressr, encoding='cp949')

gu = ''
dong = ''
for row_num, row in csv_file_bus_address.iterrows():
    ars_id = row["ARS_ID"]
    gu = row['구']
    dong = row['동']
    if pd.isna(ars_id):
        continue
    data[ars_id] = {
        'address_id': address_data[gu][dong],
        'name': row["정류장"]
    }

# 폴더 경로 설정
folder_path = 'data/bus/'
# 폴더 내의 모든 파일 목록 가져오기
file_list = os.listdir(folder_path)

# XLSX 파일만 선택
xlsx_files = [file for file in file_list if file.endswith('.xlsx')]
non_list = {}
pass_list = [5019, 5020, 3192]
ind = 0
total_data = 0
for xlsx_file in xlsx_files:
    file_path = os.path.join(folder_path, xlsx_file)
    all_sheets = pd.read_excel(file_path, sheet_name=None)
    print(file_path)
    for sheet_name, df in all_sheets.items():

        for row_num, row in df.iterrows():
            total_data += 1
            ars_id = row["ARS_ID"]
            num = row["거래건수"]
            if pd.isna(ars_id):
                continue
            if ars_id in data:
                if "total" in data[ars_id]:
                    data[ars_id]["total"] += num
                else:
                    data[ars_id]["total"] = num
            else:
                if ars_id > 6000:
                    pass
                elif ars_id in pass_list:
                    pass
                elif ars_id in non_list:
                    pass
                else:
                    non_list[ars_id] = 0
                    print(ind, "----------------")
                    print(sheet_name)
                    print(int(ars_id))
                    print(row["정류장명"])
                    ind += 1


sql_data = {
    'dong_id': [],
    'name': [],
    'total': [],
}
idx = 0
for key, value in data.items():
    idx += 1
    sql_data['dong_id'].append(value['address_id'])
    sql_data['name'].append(value['name'])
    if "total" in value:
        sql_data['total'].append(value['total'])
    else:
        sql_data['total'].append(0)

print('total_data : ', total_data)
print('idx : ', idx)


# 변경사항을 커밋
connection.commit()

# 커서 닫기
cursor.close()

# 연결 닫기
connection.close()
