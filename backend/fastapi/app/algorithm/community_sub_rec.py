# word2Vec을 이용한 단어 유사도 추천
import pymysql

from soynlp.tokenizer import RegexTokenizer
import pandas as pd
import warnings
from gensim.models import word2vec
import nltk
import re


import logging

def recommend_community_category(product_small_id):
    nltk.download('punkt')
    warnings.filterwarnings(action = 'ignore')

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
    query = "SELECT * FROM productSmallCategory"
    cursor.execute(query)
    productSmall_sql = cursor.fetchall()

    allProductSmall = pd.DataFrame(productSmall_sql, columns=['id', 'name', 'category'])

    # 품목 이름 가져오기
    query = "SELECT small FROM productSmall where id = %s;"
    cursor.execute(query, product_small_id)
    result_product_name = cursor.fetchone()

    product_name = ""
    if result_product_name:
        product_name = str(result_product_name[0])

    product_name = re.sub(r"[^\uAC00-\uD7A30-9a-zA-Z]", "", product_name)

    # 커뮤니티 세부 주제 데이터 조회
    query = "SELECT id, theme, theme_sub, title_post, text FROM communityTheme"
    cursor.execute(query)
    community_theme_sql = cursor.fetchall()

    community_theme = pd.DataFrame(community_theme_sql,
                                   columns=['id', 'category', 'category_sub', 'title_post', 'text'])

    # 컬럼을 합침
    cols=['category', 'category_sub', 'title_post', 'text']
    cols_2=['name', 'category']
    data=community_theme[cols]
    data['total']=data[cols].apply(lambda row: ' '.join(row.values.astype(str)), axis=1)
    allProductSmall['total']=allProductSmall[cols_2].apply(lambda row: ' '.join(row.values.astype(str)), axis=1)

    data_merge = pd.concat([data['total'], allProductSmall['total']])

    # 데이터 전처리 후 토큰화
    tokenizer = RegexTokenizer()

    # 텍스트 학습전 전처리 적용
    sentences = data_merge.apply(preprocessing)

    # 텍스트 데이터 토큰화
    tokens = sentences.apply(tokenizer.tokenize)

    # word2Vec 모델 학습
    # 로그 출력
    logging.basicConfig(
        format='%(asctime)s : %(levelname)s : %(message)s',
        level=logging.INFO)

    # 모델에 학습
    model = word2vec.Word2Vec(tokens, min_count=1)

    # 모델 이름 지정 후 저장
    model_name = 'recommendModel'
    model.save(model_name)

    # 단어 사전 수
    print(len(model.wv))

    # 개수
    print(model.wv.get_vecattr("예술", "count"))

    category_sub_list = [
        '문학', '책', '영화', '미술', '디자인', '공연', '전시', '음악', '드라마', '스타', '연예인', '만화', '애니', '방송',
        '일상', '생각', '육아', '결혼', '반려동물', '좋은글', '이미지', '패션', '미용', '인테리어', 'DIY', '요리', '레시피', '상품리뷰', '원예', '재배',
        '게임', '스포츠', '사진', '자동차', '취미', '국내여행', '세계여행', '맛집',
        'IT', '컴퓨터', '사회', '정치', '건강', '의학', '비즈니스', '경제', '어학', '외국어', '교육', '학문'
    ]

    # 두 단어를 입력하여 유사도 구하기
    print('두 단어 유사도')
    print(product_name)
    max_value = -1
    max_value_category = ""
    for category_sub in category_sub_list:
        word_similarity = model.wv.similarity(product_name, category_sub)

        if (max_value < word_similarity):
            max_value = word_similarity
            max_value_category = category_sub

    return max_value_category


# 전처리 함수
def preprocessing(data):
    # 개행문자 제거
    data = re.sub('\\\\n', ' ', data)
    # 한글, 영문만 남기고 모두 제거
    data = re.sub('[^가-힣ㄱ-ㅎㅏ-ㅣa-zA-Z]', ' ', data)
    return data
