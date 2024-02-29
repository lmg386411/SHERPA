import pymysql

from fastapi import APIRouter
from pydantic import BaseModel

class Target(BaseModel):
    gender: dict
    age: dict
    sidoId:  int


class ResponseItem(BaseModel):
    success: bool
    data: dict
    count: int
    msg: str

router = APIRouter(prefix="/fastapi/offline")

@router.post("/news/newspaper", status_code=200)
async def read_root(target: Target):

    if target.sidoId<1 or target.sidoId>17:
        response_data = ResponseItem(
            success=False,
            data={},
            count= 0 ,
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

    data={}

    # 성별 데이터 가져오기
    gender_select_query = "SELECT * FROM newsGender;"
    cursor.execute(gender_select_query)

    gender_sql = cursor.fetchall()
    for row in gender_sql:

        if row[2] not in data:
            data[row[2]] = {}

        if row[1] == 1:
            key = '1'
        else:
            key = '0'
        data[row[2]][key] = row[3]


    # 연령 데이터 가져오기
    age_select_query = "SELECT * FROM newsAge;"
    cursor.execute(age_select_query)

    age_sql = cursor.fetchall()
    for row in age_sql:
        data[row[2]][str(row[1])] = row[3]


    # 지역 데이터 가져오기
    seoul = "서울"
    in_gyeon = "인천/경기"
    dae_se_chung = "대전/세종/충청"
    gwang_jeo = "광주/전라"
    dae_gyeong = "대구/경북"
    bu_ul_gyeong = "부산/울산/경남"
    gangwon = "강원"
    jeju = "제주"

    area_data = {}
    area_data[1] = gangwon
    area_data[2] = in_gyeon
    area_data[3] = bu_ul_gyeong
    area_data[4] =dae_gyeong
    area_data[5] =gwang_jeo
    area_data[6] =dae_gyeong
    area_data[7] =dae_se_chung
    area_data[8] =bu_ul_gyeong
    area_data[9] =seoul
    area_data[10] =dae_se_chung
    area_data[11] =bu_ul_gyeong
    area_data[12] =in_gyeon
    area_data[13] =gwang_jeo
    area_data[14] =gwang_jeo
    area_data[15] =jeju
    area_data[16] =dae_se_chung
    area_data[17] =dae_se_chung

    area_select_query = "SELECT * FROM newsArea where area = %s;"
    cursor.execute(area_select_query, area_data[target.sidoId])

    area_sql = cursor.fetchall()
    for row in area_sql:
        data[row[2]]["area"] = row[3]

    # 가중치
    weight =58936

    # 각 신문사의 점수 계산
    scores = {}
    total_score = 0

    for key,value in data.items():
        newspaper = key
        score = 0
        for k,v in target.age.items():
            if k not in value:
                continue
            score += weight * v * value[k]

        for k,v in target.gender.items():
            score += weight * v * value[k]
        score += weight * value["area"]
        scores[newspaper] = score
        total_score += score

    results = []
    for key, value in scores.items():
        result = {}
        result["type"] = key
        result["ratio"] = round((value / total_score) * 100)
        results.append(result)
    sorted_results = sorted(results, key=lambda x: x["ratio"], reverse=True)

    response_data = ResponseItem(
        success=True,
        data={
            "newsList" : sorted_results
        },
        count=len(sorted_results),
        msg="데이터를 성공적으로 불러왔습니다."
    )
    return response_data


