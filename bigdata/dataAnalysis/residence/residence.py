import os
import pandas as pd
import pymysql
import re

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
query = """SELECT dong.id, dong.name AS dong_name, sigungu.name AS sigungu_name, sido.name AS sido_name
            FROM dong
            JOIN sigungu ON dong.sigungu_id = sigungu.id
            JOIN sido ON sigungu.sido_id = sido.id;"""
cursor.execute(query)

address_data = {}

# 결과 가져오기
address = cursor.fetchall()
for row in address:
    if row[3] in address_data:
        if row[2] in address_data[row[3]]:
            if row[1] in address_data[row[3]][row[2]]:
                if address_data[row[3]][row[2]][row[1]] > row[0]:
                    address_data[row[3]][row[2]][row[1]] = row[0]

            address_data[row[3]][row[2]][row[1]] = row[0]
        else:
            address_data[row[3]][row[2]] = {}
            address_data[row[3]][row[2]][row[1]] = row[0]
    else:
        address_data[row[3]] = {}
        address_data[row[3]][row[2]] = {}
        address_data[row[3]][row[2]][row[1]] = row[0]


csv_path = 'data/residence/202308_202308_연령별인구현황_월간 (2).csv'
csv_file = pd.read_csv(csv_path, encoding='cp949')


# 정규표현식 패턴
pattern = r"([가-힣]+) ([가-힣]+) ([가-힣]+)\((\d+)\)"

sido_data = {}

sido_data["강원특별자치도"] = "강원"
sido_data["경기도"] = "경기"
sido_data["경상남도"] = "경남"
sido_data["경상북도"] = "경북"
sido_data["광주광역시"] = "광주"
sido_data["대구광역시"] = "대구"
sido_data["대전광역시"] = "대전"
sido_data["부산광역시"] = "부산"
sido_data["서울특별시"] = "서울"
sido_data["세종특별자치시"] = "세종"
sido_data["울산광역시"] = "울산"
sido_data["인천광역시"] = "인천"
sido_data["전라남도"] = "전남"
sido_data["전라북도"] = "전북"
sido_data["제주특별자치도"] = "제주"
sido_data["충청남도"] = "충남"
sido_data["충청북도"] = "충북"


for row_num, row in csv_file.iterrows():
    area = row["행정구역"]
    match = re.match(pattern, area)
    if match:
        sido = match.group(1)
        sigungu = match.group(2)
        dong = match.group(3)
        try:
            dong_id = address_data[sido_data[sido]][sigungu][dong]
            insert_query = "INSERT INTO residence (gender, age, total, dong_id) VALUE(%s, %s, %s, %s)"
            # 0:여성, 1:남성

            cursor.execute(insert_query, (1, 0, int(
                row["2023년08월_남_0~9세"].replace(",", "")), dong_id))
            connection.commit()

            cursor.execute(insert_query, (1, 10, int(
                row["2023년08월_남_10~19세"].replace(",", "")), dong_id))
            connection.commit()

            cursor.execute(insert_query, (1, 20, int(
                row["2023년08월_남_20~29세"].replace(",", "")), dong_id))
            connection.commit()

            cursor.execute(insert_query, (1, 30, int(
                row["2023년08월_남_30~39세"].replace(",", "")), dong_id))
            connection.commit()

            cursor.execute(insert_query, (1, 40, int(
                row["2023년08월_남_40~49세"].replace(",", "")), dong_id))
            connection.commit()

            cursor.execute(insert_query, (1, 50, int(
                row["2023년08월_남_50~59세"].replace(",", "")), dong_id))
            connection.commit()

            cursor.execute(insert_query, (1, 60, int(
                row["2023년08월_남_60~69세"].replace(",", "")), dong_id))
            connection.commit()

            cursor.execute(insert_query, (1, 70, int(
                row["2023년08월_남_70~79세"].replace(",", "")), dong_id))
            connection.commit()

            cursor.execute(insert_query, (1, 80, int(
                row["2023년08월_남_80~89세"].replace(",", "")), dong_id))
            connection.commit()

            cursor.execute(insert_query, (1, 90, int(
                row["2023년08월_남_90~99세"].replace(",", "")), dong_id))
            connection.commit()

            cursor.execute(insert_query, (0, 0, int(
                row["2023년08월_여_0~9세"].replace(",", "")), dong_id))
            connection.commit()

            cursor.execute(insert_query, (0, 10, int(
                row["2023년08월_여_10~19세"].replace(",", "")), dong_id))
            connection.commit()

            cursor.execute(insert_query, (0, 20, int(
                row["2023년08월_여_20~29세"].replace(",", "")), dong_id))
            connection.commit()

            cursor.execute(insert_query, (0, 30, int(
                row["2023년08월_여_30~39세"].replace(",", "")), dong_id))
            connection.commit()

            cursor.execute(insert_query, (0, 40, int(
                row["2023년08월_여_40~49세"].replace(",", "")), dong_id))
            connection.commit()

            cursor.execute(insert_query, (0, 50, int(
                row["2023년08월_여_50~59세"].replace(",", "")), dong_id))
            connection.commit()

            cursor.execute(insert_query, (0, 60, int(
                row["2023년08월_여_60~69세"].replace(",", "")), dong_id))
            connection.commit()

            cursor.execute(insert_query, (0, 70, int(
                row["2023년08월_여_70~79세"].replace(",", "")), dong_id))
            connection.commit()

            cursor.execute(insert_query, (0, 80, int(
                row["2023년08월_여_80~89세"].replace(",", "")), dong_id))
            connection.commit()

            cursor.execute(insert_query, (0, 90, int(
                row["2023년08월_여_90~99세"].replace(",", "")), dong_id))
            connection.commit()

        except Exception as e:
            print(e)
            # query = """SELECT s.id
            #         FROM sigungu s
            #         JOIN sido d ON s.sido_id = d.id
            #         WHERE d.name = %s AND s.name = %s;"""
            # cursor.execute(query, (sido_data[sido],sigungu))
            # result = cursor.fetchall()
            # print(sido, sigungu, dong)
            # print(result[0][0])
            # sigungu_id = result[0][0]

            # insert_query_dong = "INSERT INTO dong (name, sigungu_id) VALUES (%s, %s)"
            # cursor.execute(insert_query_dong, (dong, sigungu_id))
            # connection.commit()
            break


# 변경사항을 커밋
connection.commit()

# 커서 닫기
cursor.close()

# 연결 닫기
connection.close()
