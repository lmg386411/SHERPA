import pandas as pd
import mysql.connector

# DB
# local db 연결
conn = mysql.connector.connect(host="localhost", user="root", password="ssafy", database="adrec")
cursor = conn.cursor()  # 커서 생성

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

# csv 파일
tv_data = pd.read_csv('./csv/TV광고단가.csv', encoding='cp949')
newspaper_data = pd.read_csv('./csv/신문광고단가.csv', encoding='cp949')
community_data = pd.read_csv('./csv/커뮤니티광고단가.csv', encoding='utf-8')
radio_data = pd.read_csv('./csv/radio광고단가.csv', encoding='cp949')

# 최솟값 최댓값 계산
tv_min, tv_max = tv_data['TV광고단가'].min(), tv_data['TV광고단가'].max()
newspaper_min, newspaper_max = newspaper_data['신문광고단가'].min(), newspaper_data['신문광고단가'].max()
community_min, community_max = community_data['커뮤니티광고단가'].min(), community_data['커뮤니티광고단가'].max()
radio_min, radio_max = radio_data['radio광고단가'].min(), radio_data['radio광고단가'].max()


media_types = ["TV", "신문", "커뮤니티", "라디오", "버스", "지하철", "현수막", "SNS"]
budget_values = [
    (tv_min, tv_max),
    (newspaper_min, newspaper_max),
    (community_min, community_max),
    (radio_min, radio_max),
    (350000, 2200000),
    (1000000, 4000000),
    (12900, 12900),
    (1200, 1000000)
]

# mediaType 및 mediaSub에서 id 값 가져오기
def get_media_type_id(large, medium):
    query = "SELECT id FROM mediaType WHERE large=%s AND medium=%s"
    cursor.execute(query, (large, medium))
    return cursor.fetchone()[0]

def get_media_sub_id(small):
    query = "SELECT id FROM mediaSub WHERE small=%s"
    cursor.execute(query, (small,))
    result = cursor.fetchone()
    return result[0] if result else None

# budget 테이블에 데이터 삽입
def insert_into_budget(min_budget, max_budget, mediaType_id, mediaSub_id=None):
    query = "INSERT INTO budget (min_budget, max_budget, mediaType_id, mediaSub_id) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (min_budget, max_budget, mediaType_id, mediaSub_id))
    conn.commit()

# 각 데이터를 budget 테이블에 삽입
data_mappings = [
    ("온라인", "커뮤니티", community_data['커뮤니티광고단가'].min().item(), community_data['커뮤니티광고단가'].max().item(), None),
    ("온라인", "SNS", 1500, 1000000, None),
    ("오프라인", "TV", tv_data['TV광고단가'].min().item(), tv_data['TV광고단가'].max().item(), None),
    ("오프라인", "라디오", radio_data['radio광고단가'].min().item(), radio_data['radio광고단가'].max().item(), None),
    ("오프라인", "인쇄", newspaper_data['신문광고단가'].min().item(), newspaper_data['신문광고단가'].max().item(), None),
    ("오프라인", "옥외", 350000, 2200000, "버스"),
    ("오프라인", "옥외", 1000000, 4000000, "지하철"),
    ("오프라인", "옥외", 4500, 12000, "현수막")
]

for large, medium, min_budget, max_budget, small in data_mappings:
    mediaType_id = get_media_type_id(large, medium)
    mediaSub_id = get_media_sub_id(small) if small else None
    insert_into_budget(min_budget, max_budget, mediaType_id, mediaSub_id)

# DB 연결 종료
cursor.close()
conn.close()
