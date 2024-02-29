# 커뮤니티 세부 주제 추천
import warnings

import pymysql
from pydantic import BaseModel
from fastapi import APIRouter

from app.algorithm import community_sub_rec

# Request Body로 받을 데이터
class Target(BaseModel):
    productSmallId: int

class ResponseItem(BaseModel):
    success: bool
    data: list
    count: int
    msg: str

warnings.filterwarnings("ignore")

router = APIRouter(prefix="/fastapi/online")

@router.post("/community/sub", status_code=200)
async def recommend_community_category(target: Target):
    result_category = community_sub_rec.recommend_community_category(target.productSmallId)

    # 연결 설정
    connection = pymysql.connect(
        host='j9c107.p.ssafy.io',
        user='c107',
        password='c107adrec',
        database='adrec'
    )

    # 커서 생성
    cursor = connection.cursor()

    # 품목 데이터 가져와서 추가
    query = "SELECT title_post, name_author, url, img FROM communityTheme where theme_sub like '%" + result_category + "%'"
    cursor.execute(query)
    communityTheme_sql = cursor.fetchall()

    communityList = []
    for row in communityTheme_sql:
        communityInfo = {}
        communityInfo['img'] = row[3]
        communityInfo['author'] = row[1]
        communityInfo['title'] = row[0]
        communityInfo['url'] = row[2]
        communityList.append(communityInfo)

    response_data = ResponseItem(
        success = True,
        data = communityList,
        count = len(communityList),
        msg = "데이터를 성공적으로 불러왔습니다."
    )

    return response_data
