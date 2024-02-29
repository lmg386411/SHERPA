# radio 추천
import pandas as pd
import pymysql

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/fastapi/offline")


class Target(BaseModel):
    gender: dict
    age: dict
    sidoId: int


class TargetAge(BaseModel):
    age: dict


class Response(BaseModel):
    success: bool
    data: dict
    count: int
    msg: str


@router.post("/radio", status_code=200)
async def read_root(target: Target):
    if target.sidoId < 1 or target.sidoId > 17:
        response_data = Response(
            success=False,
            data={},
            count=0,
            msg="sidoId가 잘못 되었습니다. 1~17 사이의 숫자로 보내세요."
        )
        return response_data

    # 연결 설정
    connection = pymysql.connect(
        host='j9c107.p.ssafy.io',
        user='c107',
        password='c107adrec',
        database='adrec'
    )

    # 커서 생성
    cursor = connection.cursor()

    data = {}

    # 성별 데이터 가져오기
    gender_select_query = "SELECT * FROM radioGender"
    cursor.execute(gender_select_query)

    gender_sql = cursor.fetchall()
    print(gender_sql)
    for row in gender_sql:

        if row[3] not in data:
            data[row[3]] = {}

        if row[1] == 1:
            key = '1'
        else:
            key = '0'
        data[row[3]][key] = row[2]

    # 연령 데이터 가져오기
    age_select_query = "SELECT * FROM radioAge"
    cursor.execute(age_select_query)

    age_sql = cursor.fetchall()
    for row in age_sql:
        data[row[3]][str(row[1])] = row[2]

    # 지역 데이터 가져오기
    seoul = "서울"
    in_gyeon = "인천/경기"
    dae_se_chung = "대전/충청"
    gwang_jeo = "광주/전라"
    dae_gyeong = "대구/경북"
    bu_ul_gyeong = "부산/울산/경남"
    gangwon = "강원"
    jeju = "제주"

    area_data = {1: gangwon, 2: in_gyeon, 3: bu_ul_gyeong, 4: dae_gyeong, 5: gwang_jeo, 6: dae_gyeong,
                 7: dae_se_chung, 8: bu_ul_gyeong, 9: seoul, 10: dae_se_chung, 11: bu_ul_gyeong, 12: in_gyeon,
                 13: gwang_jeo, 14: gwang_jeo, 15: jeju, 16: dae_se_chung, 17: dae_se_chung}

    area_select_query = "SELECT * FROM radioArea where area = %s"
    cursor.execute(area_select_query, area_data[target.sidoId])

    area_sql = cursor.fetchall()
    for row in area_sql:
        data[row[3]]["area"] = row[2]

    # 가중치 - 전체 인원 수가 없어 news 데이터 사용
    weight = 1948

    # 각 TV 방송 유형 점수 계산
    scores = {}
    total_score = 0

    print(data)
    # '뉴스/시사보도': {'0': 66, '1': 70, '10': 18, '20': 39, '30': 58, '40': 75, '50': 85, '60': 88, '70': 82, 'area': 73}
    # '교양': {'0': 37, '1': 38, '10': 14, '20': 16, '30': 27, '40': 37, '50': 51, '60': 54, '70': 48, 'area': 32}
    for key, value in data.items():
        radio = key
        score = 0
        for k, v in target.age.items():
            if k not in value:
                continue
            score += weight * v * value[k]

        for k, v in target.gender.items():
            score += weight * v * value[k]
        score += weight * value["area"]
        scores[radio] = score
        total_score += score

    results = []
    for key, value in scores.items():
        result = {}
        result["type"] = key
        result["ratio"] = round((value / total_score) * 100)
        results.append(result)
    sorted_results = sorted(results, key=lambda x: x["ratio"], reverse=True)

    response_data = Response(
        success=True,
        data={
            "radioList": sorted_results
        },
        count=len(sorted_results),
        msg="데이터를 성공적으로 불러왔습니다."
    )
    return response_data


@router.post("/radio/time", status_code=200)
async def radio_timeline(target: TargetAge):
    # 연결 설정
    connection = pymysql.connect(
        host='j9c107.p.ssafy.io',
        user='c107',
        password='c107adrec',
        database='adrec'
    )

    # 커서 생성
    cursor = connection.cursor()

    weekday_data = {}
    weekend_data = {}

    # 주중 시간대 데이터 가져오기
    weekday_select_query = "SELECT * FROM radioTime WHERE is_weekday=0"
    cursor.execute(weekday_select_query)

    weekday_time_sql = cursor.fetchall()
    # print(weekday_time_sql)
    for row in weekday_time_sql:
        if row[3] not in weekday_data:
            weekday_data[row[3]] = {}

        weekday_data[row[3]][str(row[1])] = row[4]
    # print(data)

    # 주말 시간대 데이터 가져오기
    weekend_select_query = "SELECT * FROM radioTime WHERE is_weekday=1"
    cursor.execute(weekend_select_query)

    weekend_time_sql = cursor.fetchall()
    # print(weekend_time_sql)
    for row in weekend_time_sql:
        if row[3] not in weekend_data:
            weekend_data[row[3]] = {}

        weekend_data[row[3]][str(row[1])] = row[4]
    # print(weekend_data)
    cursor.close()

    # 주중별 각 라디오 방송 유형 점수 계산
    weekday_scores = {}
    weekday_total_score = 0

    for key, value in weekday_data.items():
        time = key
        score = 0
        for k, v in target.age.items():
            if k not in value:
                continue
            score += v * value[k]
        weekday_scores[time] = score
        weekday_total_score += score

    # 주말별 각 라디오 방송 유형 점수 계산
    weekend_scores = {}
    weekend_total_score = 0

    for key, value in weekend_data.items():
        time = key
        score = 0
        for k, v in target.age.items():
            if k not in value:
                continue
            score += v * value[k]
        weekend_scores[time] = score
        weekend_total_score += score
    # print(weekend_scores)

    weekday_results = []
    weekday_max_time = 0
    weekday_max_time_value = 0
    for key, value in weekday_scores.items():
        result = round((value / weekday_total_score) * 100)
        weekday_results.append(result)

        if result > weekday_max_time_value:
            weekday_max_time = key
            weekday_max_time_value = result

    weekend_results = []
    weekend_max_time = 0
    weekend_max_time_value = 0
    for key, value in weekend_scores.items():
        result = round((value / weekend_total_score) * 100)
        weekend_results.append(result)

        if result > weekend_max_time_value:
            weekend_max_time = key
            weekend_max_time_value = result

    response_data = Response(
        success=True,
        data={
            "weekday_recommend": weekday_max_time,
            "weekdaysDatas": weekday_results,
            "weekend_recommend": weekend_max_time,
            "weekendsDatas": weekend_results
        },
        count=len(weekday_results),
        msg="라디오 광고 시간대 분석 데이터를 성공적으로 불러왔습니다."
    )
    return response_data

