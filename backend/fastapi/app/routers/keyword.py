import numpy as np
import pymysql

from fastapi import APIRouter
from pydantic import BaseModel
from sklearn.metrics.pairwise import cosine_similarity

router = APIRouter(prefix="/fastapi")


class Item(BaseModel):
    productSmallId: int
    memberName: str
    listSize: int


class ResponseItem(BaseModel):
    success: bool
    data: dict
    count: int
    msg: str


# 광고 매체 추천 - 품목
@router.post("/keyword")
def offline(item: Item):
    # DB 연결
    db_config = {
        "host": "j9c107.p.ssafy.io",
        "user": "c107",
        "password": "c107adrec",
        "database": "adrec"
    }

    conn = pymysql.connect(**db_config)
    cursor = conn.cursor()

    member_select_query = "SELECT * FROM member WHERE name = %s"
    cursor.execute(member_select_query, (item.memberName))
    member_query_result = cursor.fetchall()

    member_id = member_query_result[0][0]

    keywordRec_select_query = "SELECT * FROM keywordRec WHERE productSmall_id = %s"
    cursor.execute(keywordRec_select_query, (item.productSmallId,))
    keywordRec_query_result = cursor.fetchall()

    target = []
    target_keywordRec_select_query = "SELECT * FROM keywordRec WHERE member_id = %s;"
    cursor.execute(target_keywordRec_select_query, (member_id,))
    target_keywordRec_query_result = cursor.fetchall()

    keywordLike_select_query = "SELECT * FROM keywordLike WHERE keywordRec_id = %s"
    for row in target_keywordRec_query_result:
        cursor.execute(keywordLike_select_query, (row[0],))
        target_keywordLike_query_result = cursor.fetchall()
        for r in target_keywordLike_query_result:
            target.append(r[1])

    data = {}
    for row in keywordRec_query_result:
        if row[2] in data:
            cursor.execute(keywordLike_select_query, (row[0],))
            keywordLike_query_result = cursor.fetchall()
            for r in keywordLike_query_result:
                data[row[2]].append(r[1])
        else:
            data[row[2]]=[]
            cursor.execute(keywordLike_select_query, (row[0],))
            keywordLike_query_result = cursor.fetchall()
            for r in keywordLike_query_result:
                data[row[2]].append(r[1])



    # 모든 키워드 목록 가져오기
    keywords = list(set([keyword for user_keywords in data.values() for keyword in user_keywords]))
    keywords.extend(target)
    keywords = list(set(keywords))
    keywords.sort()
    # 각 사용자의 키워드 좋아요 여부를 이진 벡터로 변환
    binary_vectors = []
    for user_keywords in data.values():
        binary_vector = [1 if keyword in user_keywords else 0 for keyword in keywords]
        binary_vectors.append(binary_vector)

    # Target 사용자의 키워드 좋아요 여부를 이진 벡터로 변환
    target_vector = [1 if keyword in target else 0 for keyword in keywords]

    # 데이터를 행렬 형태로 변환
    keyword_matrix = np.array(binary_vectors)

    # Target 사용자의 유사도 계산
    target_similarity = cosine_similarity([target_vector], keyword_matrix)[0]

    user_similarities = list(zip(data.keys(), target_similarity))
    user_similarities.sort(key=lambda x: x[1], reverse=True)

    recommendations = {}

    for value in user_similarities:
        for keyword in data[value[0]]:
            if keyword in recommendations:
                recommendations[keyword] += value[1]
            else:
                recommendations[keyword] = value[1]

    # 값을 기준으로 딕셔너리 정렬
    sorted_recommendations = dict(sorted(recommendations.items(), key=lambda item: item[1], reverse=True))

    keyword_recommendations=[]
    idx = 0
    for key, value in sorted_recommendations.items():
        if idx == item.listSize:
            break

        if key in target:
            continue
        keyword_recommendation={}
        keyword_recommendation["rank"]=idx+1

        keyword_recommendation["keyword"]=key
        keyword_recommendations.append(keyword_recommendation)
        idx += 1

    response_data = ResponseItem(
        success=True,
        data={
            "keywordList": keyword_recommendations
        },
        count=len(keyword_recommendations),
        msg="데이터를 성공적으로 불러왔습니다."
    )

    return response_data






