# 커뮤니티 추천
import pandas as pd
import warnings

import pymysql
from pydantic import BaseModel
from fastapi import APIRouter

from typing import Dict

# Request Body로 받을 데이터
class Target(BaseModel):
    gender: Dict[str, int]
    age: Dict[str, int]
    sidoId: int

class ResponseItem(BaseModel):
    success: bool
    data: dict
    count: int
    msg: str

warnings.filterwarnings("ignore")

router = APIRouter(prefix="/fastapi/online")

@router.post("/community", status_code=200)
async def recommend_community(target: Target):

    # 연결 설정
    connection = pymysql.connect(
        host='j9c107.p.ssafy.io',
        user='c107',
        password='c107adrec',
        database='adrec'
    )

    # 커서 생성
    cursor = connection.cursor()

    # 성별
    data_gender={}

    query = "SELECT * FROM communityGender"
    cursor.execute(query)
    community_gender_sql = cursor.fetchall()

    community_gender = pd.DataFrame(community_gender_sql, columns=['id', 'gender', 'name', 'total', 'year'])

    for index, row in community_gender.iterrows():
        if row['year'] not in data_gender:
            data_gender[row['year']] = {}

        if row['name'] not in data_gender[row['year']]:
            data_gender[row['year']][row['name']] = {}

        data_gender[row['year']][row['name']][row['gender']] = row['total']


    # 연령별
    data_age={}

    query = "SELECT * FROM communityAge"
    cursor.execute(query)
    community_age_sql = cursor.fetchall()

    community_age = pd.DataFrame(community_age_sql, columns=['id', 'age', 'name', 'total', 'year'])

    for index, row in community_age.iterrows():
        if row['year'] not in data_age:
            data_age[row['year']] = {}

        if row['name'] not in data_age[row['year']]:
            data_age[row['year']][row['name']] = {}

        data_age[row['year']][row['name']][row['age']] = row['total']


    # 지역별
    data_area={}

    data_area[2021] = {}
    data_area[2022] = {}

    # 시도 이름 DB에서 조회
    query = "SELECT name FROM sido WHERE id = %s;"
    cursor.execute(query, target.sidoId)
    result_sido_name = cursor.fetchone()

    sido_name = ""
    if result_sido_name:
        sido_name = str(result_sido_name[0])

        query = "SELECT * FROM communityArea WHERE area = %s;"
        cursor.execute(query, (sido_name))
        community_sql = cursor.fetchall()


        community_area = pd.DataFrame(community_sql, columns=['id', 'area', 'name', 'total', 'year'])

        for index, row in community_area.iterrows():
            if row['year'] not in data_area:
                data_area[row['year']] = {}

            if row['name'] not in data_area[row['year']]:
                data_area[row['year']][row['name']] = {}

            data_area[row['year']][row['name']][row['area']] = row['total']

    else:
        print('해당 지역 아이디가 없습니다.')

    # 커뮤니티 별 점수 계산
    scores = {}
    scores[2021] = {}
    scores[2022] = {}
    total_scores = [0, 1]


    # 가중치 설정
    weight = {}
    weight[2021] = {}
    weight[2022] = {}
    weight[2021][1] = 349
    weight[2021][0] = 397
    weight[2022][1] = 235.2
    weight[2022][0] = 374.9

    # 성별 가중치 계산
    cnt = 0
    for year, community_data in data_gender.items():
        for community, value in community_data.items():
            score = 0
            for gender_data, ratio in target.gender.items():
                score += weight[year][int(gender_data)] * ratio * value[int(gender_data)]
            scores[year][community] = score
            total_scores[cnt] += score
        cnt += 1


    # 가중치 설정
    weight[2021][10] = 47
    weight[2021][20] = 226.8
    weight[2021][30] = 205.3
    weight[2021][40] = 192.2
    weight[2021][50] = 58.9
    weight[2021][60] = 12

    weight[2022][10] = 31.7
    weight[2022][20] = 199.7
    weight[2022][30] = 155.2
    weight[2022][40] = 151.9
    weight[2022][50] = 58.8
    weight[2022][60] = 11

    # 연령대별 가중치 계산
    cnt = 0
    for year, community_data in data_age.items():
        for community, value in community_data.items():
            score = 0
            for age_data, ratio in target.age.items():
                if (int(age_data) > 60):
                    continue
                score += weight[year][int(age_data)] * ratio * value[int(age_data)]
            scores[year][community] += score
            total_scores[cnt] += score
        cnt += 1


    # 지역 가중치 계산

    # 가중치 설정
    weight[2021]['서울'] = 195.2
    weight[2021]['부산'] = 44
    weight[2021]['대구'] = 23.4
    weight[2021]['인천'] = 28.2
    weight[2021]['광주'] = 6.1
    weight[2021]['대전'] = 24.1
    weight[2021]['울산'] = 2.8
    weight[2021]['세종'] = 1.9
    weight[2021]['경기'] = 224
    weight[2021]['강원'] = 7.2
    weight[2021]['충북'] = 43.5
    weight[2021]['충남'] = 55.2
    weight[2021]['전북'] = 15.4
    weight[2021]['전남'] = 8.2
    weight[2021]['경북'] = 37.3
    weight[2021]['경남'] = 9.5
    weight[2021]['제주'] = 20.1

    weight[2022]['서울'] = 148
    weight[2022]['부산'] = 31.5
    weight[2022]['대구'] = 22.8
    weight[2022]['인천'] = 33.4
    weight[2022]['광주'] = 8.2
    weight[2022]['대전'] = 7
    weight[2022]['울산'] = 0.7
    weight[2022]['세종'] = 18.2
    weight[2022]['경기'] = 238.1
    weight[2022]['강원'] = 7.6
    weight[2022]['충북'] = 19.5
    weight[2022]['충남'] = 24.4
    weight[2022]['전북'] = 7.3
    weight[2022]['전남'] = 1.7
    weight[2022]['경북'] = 27.9
    weight[2022]['경남'] = 10.9
    weight[2022]['제주'] = 2.9


    cnt = 0
    for year, community_data in data_area.items():
        for community, ratio in community_data.items():
            score = 0

            score += weight[year][sido_name] * ratio[sido_name] * community_data[community][sido_name]
            scores[year][community] += score
            total_scores[cnt] += score
        cnt += 1

    sorted_results = []

    cnt = 0
    for year, community_data in scores.items():
        results = []
        for key, value in community_data.items():
            result = {}
            result["type"] = key
            result["ratio"] = round((value / total_scores[cnt]) * 100)
            results.append(result)
        sorted_results.append(sorted(results, key=lambda x: x["ratio"], reverse=True))
        cnt += 1


    response_data = ResponseItem(
        success = True,
        data = {
            "communityList_2021" : sorted_results[0],
            "communityList_2022" : sorted_results[1]
        },
        count = len(sorted_results),
        msg = "데이터를 성공적으로 불러왔습니다."
    )

    return response_data
