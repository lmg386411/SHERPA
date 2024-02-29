import pandas as pd
import mysql.connector

# DB
# local db 연결
# conn = mysql.connector.connect(host="localhost", user="root", password="ssafy", database="adrec")
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

# MySQL에 연결
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()  # 커서 생성

# CSV 로딩
data = pd.read_csv("./csv/연령별인구현황_월간.csv", encoding='CP949')

# 행정구역 헤더의 읍, 면, 동 유무에 따른 필터링
filtered_data = data[data['행정구역'].str.contains('읍|면|동')]

def extract_dong_name(administrative_area):
    dong_name = administrative_area.split('(')[0]
    dong_name =  dong_name.split(' ')[-1]
    return dong_name

def extract_age(col):
    # If the last character is not a digit, return None
    if not col[-1].isdigit():
        return None
    
    # Split by "_" and take the last part to get the age range
    age_range = col.split('_')[-1]
    
    # Split by "~" and take the first part as the age
    age = age_range.split('~')[0]
    
    return int(age) if age.isdigit() else None

def get_dong_id(dong_name, cursor):
    query = "SELECT id FROM dong WHERE name = %s"
    cursor.execute(query, (dong_name,))
    result = cursor.fetchall()
    if result:
        return result[0][0]
    else:
        # print(f"Missing dong name in dong table: {dong_name}")
        return None

# 데이터 처리
def process_data(row, col, cursor):
    # column 이름에서 gender, age 추출
    gender = 0 if '여' in col else 1
    # print(gender)
    age = col.replace('세', '').replace('여성', '').replace('남성', '').strip()
    age = extract_age(age)
    # print(age)
    
    # dong_id와 total 구하기
    dong_name = extract_dong_name(row['행정구역'])
    dong_id = get_dong_id(dong_name, cursor)
    total = row[col]
    # total이 정수형이 아닌 경우 ',' 제거 후 int 변환
    if type(total) != int :
        total = total.replace(',', '')
        total = int(total)
        
    return {
        'gender': gender,
        'age': age,
        'total': total,
        'dong_id': dong_id
    }

# 결과값 저장
result = []
residence_df = pd.DataFrame(result)
# 결과를 CSV 파일로 저장
residence_df.to_csv("./csv/거주지전처리.csv", index=False, encoding='cp949')

# residence 테이블에 값 넣기 
insert_query = "INSERT INTO residence (gender, age, total, dong_id) VALUES (%s, %s, %s, %s)"
for idx, row in filtered_data.iterrows():
    for col in row.index[3:]:  # skipping the first 3 columns: 행정구역, 총인구수, 총인구수. 남성, 총인구수. 여성
        item = process_data(row, col, cursor)
        # break
        if item['dong_id'] and item['age'] is not None:  # Only insert if dong_id is found
            print(insert_query, (item['gender'], item['age'], item['total'], item['dong_id']))
            cursor.execute(insert_query, (item['gender'], item['age'], item['total'], item['dong_id']))
            conn.commit()

# 결과 확인을 위해 csv 저장
print("끝났어요")
