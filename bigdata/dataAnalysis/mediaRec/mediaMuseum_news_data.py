# 매체 호감 데이터 전처리한 csv 파일 서버에 넣는 코드
import pandas as pd
import mysql.connector

# TV - 영상 / 라디오 - 라디오 / 인쇄 - 인쇄 / 옥외 - 옥외 / SNS / 커뮤니티
data_news = pd.read_csv('../csv/한국방송광고진흥공사_광고박물관 소장 광고소재(인쇄광고) 현황_20220311.csv', encoding='cp949', low_memory=False)
# print(data_news)  # [20226 rows x 10 columns]

# 안쓰는 컬럼들 정리
data_news_colums = data_news.columns
# print(data_news_colums)
# Index(['번호', '년도', '매체구분', '매체', '대분류', '중분류', '소분류', '광고주', '제품', '내용'], dtype='object')
news = data_news[['번호', '년도', '매체구분', '매체', '대분류', '중분류', '소분류', '제품']].drop_duplicates()
# print(news)  # [20226 rows x 8 columns]

# 년도에 Nan인 것은 3000으로 전처리
for _, item in news.iterrows():
    if pd.isna(item['년도']):
        item['년도'] = 3000
        # print(item)

# 제작년도로 정렬
news = news[news['년도'] >= 1990]
# print(news)  # [14289 rows x 8 columns]

# 대분류/중분류/소분류 우리꺼 맞춰서 수정 *** 중요 ***
news_options = news.drop_duplicates(subset=['대분류', '중분류', '소분류'])
news_options = news_options.sort_values(by=['대분류', '중분류', '소분류'])
# print(news_options)  # [610 rows x 8 columns]
# for _, item in news_options.iterrows():
    # print(item['대분류'], ",", item['중분류'], ",", item['소분류'], sep="")

news['code'] = 0
for idx, item in news.iterrows():
    if item['대분류'] == "가정용 전기전자" and item['중분류'] == "가사용 전기전자":
        news.at[idx, 'code'] = 3101
    elif item['대분류'] == "가정용 전기전자" and item['중분류'] == "가정용 전기전자 기타":
        news.at[idx, 'code'] = 3199
    elif item['대분류'] == "가정용 전기전자" and item['중분류'] == "냉방 및 공기 청정기":
        news.at[idx, 'code'] = 3102
    elif item['대분류'] == "가정용 전기전자" and item['중분류'] == "냉방 및 공기청정기":
        news.at[idx, 'code'] = 3102
    elif item['대분류'] == "가정용 전기전자" and item['중분류'] == "영상기기":
        news.at[idx, 'code'] = 3199
    elif item['대분류'] == "가정용 전기전자" and item['중분류'] == "음향기기":
        news.at[idx, 'code'] = 3199
    elif item['대분류'] == "가정용 전기전자" and item['중분류'] == "조명 및 전기소품":
        news.at[idx, 'code'] = 3201
    elif item['대분류'] == "가정용 전기전자" and item['중분류'] == "주방용 전기전자":
        news.at[idx, 'code'] = 3203
    elif item['대분류'] == "가정용품" and item['중분류'] == "가구류" and item['소분류'] == "주방용 가구":
        news.at[idx, 'code'] = 3203
        continue
    elif item['대분류'] == "가정용품" and item['중분류'] == "가구류":
        news.at[idx, 'code'] = 3201
    elif item['대분류'] == "가정용품" and item['중분류'] == "가정용 인테리어":
        news.at[idx, 'code'] = 3404
    elif item['대분류'] == "가정용품" and item['중분류'] == "난방기기":
        news.at[idx, 'code'] = 3102
    elif item['대분류'] == "가정용품" and item['중분류'] == "방취 및 방균제":
        news.at[idx, 'code'] = 4110
    elif item['대분류'] == "가정용품" and item['중분류'] == "생활잡화 및 기기":
        news.at[idx, 'code'] = 4110
    elif item['대분류'] == "가정용품" and item['중분류'] == "가정용품 기타":
        news.at[idx, 'code'] = 4110
    elif item['대분류'] == "가정용품" and item['중분류'] == "세제류":
        news.at[idx, 'code'] = 3299
    elif item['대분류'] == "가정용품" and item['중분류'] == "식품 기타":
        news.at[idx, 'code'] = 2499
    elif item['대분류'] == "가정용품" and item['중분류'] == "악기류":
        news.at[idx, 'code'] = 6100
    elif item['대분류'] == "가정용품" and item['중분류'] == "주방용품":
        news.at[idx, 'code'] = 3299
    elif item['대분류'] == "가정용품" and item['중분류'] == "취미,레저용품":
        news.at[idx, 'code'] = 6099
    elif item['대분류'] == "가정용품" and item['중분류'] == "컴퓨터S/W":
        news.at[idx, 'code'] = 6104
    elif item['대분류'] == "가정용품" and item['중분류'] == "완구류":
        news.at[idx, 'code'] = 6204
    elif item['대분류'] == "가정용품":
        news.at[idx, 'code'] = 4110
        continue
    elif item['대분류'] == "건설, 건재 및 부동산":
        news.at[idx, 'code'] = 8210
    elif item['대분류'] == "관공서 및 단체" and item['중분류'] == "관공서 및 단체 기타":
        news.at[idx, 'code'] = 4202
    elif item['대분류'] == "관공서 및 단체" and item['중분류'] == "단체":
        news.at[idx, 'code'] = 6101
    elif item['대분류'] == "관공서 및 단체" and item['중분류'] == "중앙 및 지방 관공서":
        news.at[idx, 'code'] = 4202
    elif item['대분류'] == "교육 및 복지 후생" and item['중분류'] == "교육 및 복지후생 기타":
        news.at[idx, 'code'] = 4202
    elif item['대분류'] == "교육 및 복지후생" and item['중분류'] == "교육 및 복지후생 기타":
        news.at[idx, 'code'] = 4202
    elif item['대분류'] == "교육 및 복지후생" and item['중분류'] == "사회교육":
        news.at[idx, 'code'] = 4202
    elif item['대분류'] == "교육 및 복지 후생" and item['중분류'] == "교육기관":
        news.at[idx, 'code'] = 4202
    elif item['대분류'] == "교육 및 복지후생" and item['중분류'] == "교육기관":
        news.at[idx, 'code'] = 4202
    elif item['대분류'] == "그룹 및 기업광고" and item['중분류'] == "그룹광고":
        news.at[idx, 'code'] = 9001
    elif item['대분류'] == "그룹 및 기업광고" and item['중분류'] == "기타광고":
        news.at[idx, 'code'] = 9001
    elif item['대분류'] == "금융, 보험 및 증권":
        news.at[idx, 'code'] = 8099
    elif item['대분류'] == "기초재" and item['중분류'] == "기초재 기타":
        news.at[idx, 'code'] = 3406
    elif item['대분류'] == "기초재" and item['중분류'] == "금속":
        news.at[idx, 'code'] = 3499
    elif item['대분류'] == "기초재" and item['중분류'] == "비금속":
        news.at[idx, 'code'] = 3499
    elif item['대분류'] == "기초재" and item['중분류'] == "농축수산 기초재":
        news.at[idx, 'code'] = 3406
    elif item['대분류'] == "기초재" and item['중분류'] == "석탄,석유 및 가스":
        news.at[idx, 'code'] = 4199
    elif item['대분류'] == "기초재" and item['중분류'] == "석탄, 석유 및 가스":
        news.at[idx, 'code'] = 4199
    elif item['대분류'] == "기초재" and item['중분류'] == "전력 및 열":
        news.at[idx, 'code'] = 3408
    elif item['대분류'] == "산업기기" and item['중분류'] == "전기관련 기계":
        news.at[idx, 'code'] = 3402
    elif item['대분류'] == "산업기기" and item['중분류'] == "산업기기 기타":
        news.at[idx, 'code'] = 3402
    elif item['대분류'] == "산업기기" and item['중분류'] == "상업 및 공업용 기기":
        news.at[idx, 'code'] = 3402
    elif item['대분류'] == "산업기기" and item['중분류'] == "금속 가공기계":
        news.at[idx, 'code'] = 3403
    elif item['대분류'] == "서비스" and item['중분류'] == "개인서비스":
        news.at[idx, 'code'] = 4199
    elif item['대분류'] == "서비스" and item['중분류'] == "문화 및 공연":
        news.at[idx, 'code'] = 6210
    elif item['대분류'] == "서비스" and item['중분류'] == "서비스 기타":
        news.at[idx, 'code'] = 6299
    elif item['대분류'] == "서비스" and item['중분류'] == "광고및 정보서비스":
        news.at[idx, 'code'] = 6299
    elif item['대분류'] == "서비스" and item['중분류'] == "스포츠 및 오락시설":
        news.at[idx, 'code'] = 6001
    elif item['대분류'] == "서비스" and item['중분류'] == "여행":
        news.at[idx, 'code'] = 5301
    elif item['대분류'] == "서비스" and item['중분류'] == "운송":
        news.at[idx, 'code'] = 5399
    elif item['대분류'] == "서비스" and item['중분류'] == "음식 및 숙박":
        news.at[idx, 'code'] = 5103
    elif item['대분류'] == "서비스" and item['중분류'] == "전문서비스":
        news.at[idx, 'code'] = 8211
    elif item['대분류'] == "수송기기" and item['중분류'] == "수송기기 기타":
        news.at[idx, 'code'] = 8205
    elif item['대분류'] == "수송기기" and item['중분류'] == "수송기기 부품 및 용품":
        news.at[idx, 'code'] = 8205
    elif item['대분류'] == "수송기기" and item['중분류'] == "수입자동차":
        news.at[idx, 'code'] = 9099
    elif item['대분류'] == "수송기기" and item['중분류'] == "승용자동차":
        news.at[idx, 'code'] = 9099
    elif item['대분류'] == "수송기기" and item['중분류'] == "승합차":
        news.at[idx, 'code'] = 9099
    elif item['대분류'] == "수송기기" and item['중분류'] == "오토바이":
        news.at[idx, 'code'] = 9099
    elif item['대분류'] == "수송기기" and item['중분류'] == "자전거":
        news.at[idx, 'code'] = 9099
    elif item['대분류'] == "수송기기" and item['중분류'] == "트럭":
        news.at[idx, 'code'] = 9099
    elif item['대분류'] == "수송기기" and item['중분류'] == "특수자동차":
        news.at[idx, 'code'] = 9099
    elif item['대분류'] == "수송기기" and item['중분류'] == "철도차륜":
        news.at[idx, 'code'] = 9099
    elif item['대분류'] == "식품" and item['중분류'] == "건강식품":
        news.at[idx, 'code'] = 2404
    elif item['대분류'] == "식품" and item['중분류'] == "농산품":
        news.at[idx, 'code'] = 2406
    elif item['대분류'] == "식품" and item['중분류'] == "대용식품":
        news.at[idx, 'code'] = 2199
    elif item['대분류'] == "식품" and item['중분류'] == "면류":
        news.at[idx, 'code'] = 2104
    elif item['대분류'] == "식품" and item['중분류'] == "수산품":
        news.at[idx, 'code'] = 2406
    elif item['대분류'] == "식품" and item['중분류'] == "식품 기타":
        news.at[idx, 'code'] = 2499
    elif item['대분류'] == "식품" and item['중분류'] == "아이스크림":
        news.at[idx, 'code'] = 2044
    elif item['대분류'] == "식품" and item['중분류'] == "유제품":
        news.at[idx, 'code'] = 2044
    elif item['대분류'] == "식품" and item['중분류'] == "제과":
        news.at[idx, 'code'] = 2044
    elif item['대분류'] == "식품" and item['중분류'] == "제빵":
        news.at[idx, 'code'] = 2044
    elif item['대분류'] == "식품" and item['중분류'] == "조미향신료":
        news.at[idx, 'code'] = 2044
    elif item['대분류'] == "식품" and item['중분류'] == "축산품":
        news.at[idx, 'code'] = 2406
    elif item['대분류'] == "유통" and item['중분류'] == "대형유통":
        news.at[idx, 'code'] =  4123
    elif item['대분류'] == "유통" and item['중분류'] == "소형, 소매유통":
        news.at[idx, 'code'] = 4107
    elif item['대분류'] == "유통" and item['중분류'] == "유통 기타":
        news.at[idx, 'code'] = 4123
    elif item['대분류'] == "유통" and item['중분류'] == "유통기타":
        news.at[idx, 'code'] = 4123
    elif item['대분류'] == "유통" and item['중분류'] == "특수유통":
        news.at[idx, 'code'] = 4123
    elif item['대분류'] == "음료 및 기호식품" and item['중분류'] == "기호식품":
        news.at[idx, 'code'] = 2406
    elif item['대분류'] == "음료 및 기호식품" and item['중분류'] == "비알콜음료":
        news.at[idx, 'code'] = 2499
    elif item['대분류'] == "음료 및 기호식품" and item['중분류'] == "알콜음료":
        news.at[idx, 'code'] = 2407
    elif item['대분류'] == "음료 및 기호식품" and item['중분류'] == "음료 및 기호식품 기타":
        news.at[idx, 'code'] = 2499
    elif item['대분류'] == "음료 및 기호식품" and item['중분류'] == "유제품":
        news.at[idx, 'code'] = 2003
    elif item['대분류'] == "정밀기기 및 사무기기" and item['중분류'] == "문구류":
        news.at[idx, 'code'] = 6114
    elif item['대분류'] == "정밀기기 및 사무기기" and item['중분류'] == "사무기기":
        news.at[idx, 'code'] = 6101
    elif item['대분류'] == "정밀기기 및 사무기기" and item['중분류'] == "보안기기":
        news.at[idx, 'code'] = 6102
    elif item['대분류'] == "정밀기기 및 사무기기" and item['중분류'] == "시계":
        news.at[idx, 'code'] = 6101
    elif item['대분류'] == "정밀기기 및 사무기기" and item['중분류'] == "이광학기기":
        news.at[idx, 'code'] = 6102
    elif item['대분류'] == "정밀기기 및 사무기기" and item['중분류'] == "정밀기기 및 사무기기 기타":
        news.at[idx, 'code'] = 3101
    elif item['대분류'] == "정밀기기 및 사무기기" and item['중분류'] == "수송기기 부품 및 용품":
        news.at[idx, 'code'] = 3101
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "감기약":
        news.at[idx, 'code'] = 7005
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "근육 및 신경통제":
        news.at[idx, 'code'] = 7005
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "농축산약제":
        news.at[idx, 'code'] = 7009
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "대사성의약":
        news.at[idx, 'code'] = 7009
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "두피 및 피부용제":
        news.at[idx, 'code'] = 7009
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "백신,구충 및 살충제":
        news.at[idx, 'code'] = 7099
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "백신, 구충 및 살충제":
        news.at[idx, 'code'] = 7099
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "생리피임 및 치질용약":
        news.at[idx, 'code'] = 7005
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "소화위장약":
        news.at[idx, 'code'] = 7005
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "의료 및 보건기관":
        news.at[idx, 'code'] = 7002
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "순환기관용제":
        news.at[idx, 'code'] = 7005
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "의료기기":
        news.at[idx, 'code'] = 7107
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "의료용품":
        news.at[idx, 'code'] = 7107
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "이비인후, 치과 및 안과용제":
        news.at[idx, 'code'] = 7099
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "제약 및 의료 기타":
        news.at[idx, 'code'] = 7099
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "진통제 및 안정제":
        news.at[idx, 'code'] = 7005
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "구강용품":
        news.at[idx, 'code'] = 7005
    elif item['대분류'] == "출판" and item['중분류'] == "서적":
        news.at[idx, 'code'] = 6199
    elif item['대분류'] == "출판" and item['중분류'] == "출판 기타":
        news.at[idx, 'code'] = 6199
    elif item['대분류'] == "출판" and item['중분류'] == "신문":
        news.at[idx, 'code'] = 6199
    elif item['대분류'] == "출판" and item['중분류'] == "여가용 S/W":
        news.at[idx, 'code'] = 6299
    elif item['대분류'] == "출판" and item['중분류'] == "유아용 교재":
        news.at[idx, 'code'] = 8114
    elif item['대분류'] == "출판" and item['중분류'] == "일반용 교재":
        news.at[idx, 'code'] = 8111
    elif item['대분류'] == "출판" and item['중분류'] == "잡지":
        news.at[idx, 'code'] = 6199
    elif item['대분류'] == "출판" and item['중분류'] == "중고생용 교재":
        news.at[idx, 'code'] = 8199
    elif item['대분류'] == "출판" and item['중분류'] == "초등학생용 교재":
        news.at[idx, 'code'] = 8199
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "방송":
        news.at[idx, 'code'] = 6102
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "컴퓨터":
        news.at[idx, 'code'] = 6103
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "컴퓨터 및 정보통신 기타":
        news.at[idx, 'code'] = 6102
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "통신정보서비스":
        news.at[idx, 'code'] = 6102
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "컴퓨터 솔루션":
        news.at[idx, 'code'] = 6102
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "컴퓨터 출력장치":
        news.at[idx, 'code'] = 6103
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "컴퓨터 입력장치":
        news.at[idx, 'code'] = 6103
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "컴퓨터 통신장치":
        news.at[idx, 'code'] = 6103
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "컴퓨터 저장장치":
        news.at[idx, 'code'] = 6103
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "컴퓨터 카드류":
        news.at[idx, 'code'] = 6103
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "컴퓨터S/W":
        news.at[idx, 'code'] = 6103
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "컴퓨터 S/W":
        news.at[idx, 'code'] = 6103
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "통신기기":
        news.at[idx, 'code'] = 6103
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "통신망":
        news.at[idx, 'code'] = 6102
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "통신정보 서비스":
        news.at[idx, 'code'] = 6102
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "컴퓨터용품":
        news.at[idx, 'code'] = 6102
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "사무기기":
        news.at[idx, 'code'] = 6101
    elif item['대분류'] == "패션" and item['중분류'] == "가방류":
        news.at[idx, 'code'] = 1205
    elif item['대분류'] == "패션" and item['중분류'] == "내의류":
        news.at[idx, 'code'] = 1008
    elif item['대분류'] == "패션" and item['중분류'] == "스포츠 전문복":
        news.at[idx, 'code'] = 1099
    elif item['대분류'] == "패션" and item['중분류'] == "신발류":
        news.at[idx, 'code'] = 1099
    elif item['대분류'] == "패션" and item['중분류'] == "원사 및 원단":
        news.at[idx, 'code'] = 1199
    elif item['대분류'] == "패션" and item['중분류'] == "유아 및 아동복":
        news.at[idx, 'code'] = 1007
    elif item['대분류'] == "패션" and item['중분류'] == "정장의류":
        news.at[idx, 'code'] = 1001
    elif item['대분류'] == "패션" and item['중분류'] == "캐주얼의류":
        news.at[idx, 'code'] = 1004
    elif item['대분류'] == "패션" and item['중분류'] == "패션 신변용품":
        news.at[idx, 'code'] = 1299
    elif item['대분류'] == "패션" and item['중분류'] == "패션기타":
        news.at[idx, 'code'] = 1299
    elif item['대분류'] == "패션" and item['중분류'] == "패션 기타":
        news.at[idx, 'code'] = 1299
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "가정 및 보건용 제지":
        news.at[idx, 'code'] = 7099
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "구강용품":
        news.at[idx, 'code'] = 7099
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "남성 화장품":
        news.at[idx, 'code'] = 7106
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "모발 및 목욕용제":
        news.at[idx, 'code'] = 7199
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "방향 화장품":
        news.at[idx, 'code'] = 7199
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "세제류":
        news.at[idx, 'code'] = 7199
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "여성 기초화장품":
        news.at[idx, 'code'] = 7106
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "여성 색조화장품":
        news.at[idx, 'code'] = 7106
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "여성 썬탠류":
        news.at[idx, 'code'] = 7106
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "가정용 화장품":
        news.at[idx, 'code'] = 7106
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "유,아동용 화장 및 세제":
        news.at[idx, 'code'] = 8110
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "유, 아동용 화장 및 세제":
        news.at[idx, 'code'] = 8110
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "주니어 화장품":
        news.at[idx, 'code'] = 8110
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "화장도구":
        news.at[idx, 'code'] = 7108
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "화장품 및 보건용품 기타":
        news.at[idx, 'code'] = 7199
    elif item['대분류'] == "화학공업" and item['중분류'] == "고무 및 플라스틴":
        news.at[idx, 'code'] = 9001
    elif item['대분류'] == "화학공업" and item['중분류'] == "고무 및 플라스틱":
        news.at[idx, 'code'] = 9001
    elif item['대분류'] == "화학공업" and item['중분류'] == "화학공업 기타":
        news.at[idx, 'code'] = 9001
    elif item['대분류'] == "화학공업" and item['중분류'] == "석탄, 석유 및 가스":
        news.at[idx, 'code'] = 9001
    elif item['대분류'] == "화학공업" and item['중분류'] == "화학제품":
        news.at[idx, 'code'] = 9001
    else:
        print(item)


# 광고 사용률 - 그룹화
news = news[['년도', '대분류', '중분류', '소분류', '제품', 'code']]
# print(news)  # [14289 rows x 6 columns]

# 3. 데이터 합치기: 'total' 값 추출
# 대분류, 중분류, 소분류, code 가 모두 같은 항목들을 그룹화하고 각 그룹의 크기를 계산하여 'total' 열에 저장
news['total'] = news.groupby(['대분류', '중분류', '소분류', 'code'])['제품'].transform('count')
merged_news_data = news[['code', 'total']].drop_duplicates()
# print(merged_news_data)  # [457 rows x 2 columns]
# productMedia
# id fk fk fk total
# id / 매체유형 / 매체유형 소분류 / 업종명 소분류 / total
#  / 영상 / 5 / code / total

# server db 연결
db_config = {
    "host": "j9c107.p.ssafy.io",
    "user": "c107",
    "password": "c107adrec",
    "database": "adrec",
    "auth_plugin": "mysql_native_password"  # MySQL 8.0 이상일 경우에 필요한 옵션
}

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()  # 커서 생성

for _, item in merged_news_data.iterrows():
    print(_)
    total = int(item['total'])  # numpy.int64를 정수로 변환
    code = int(item['code'])  # numpy.int64를 정수로 변환

    check_query = "SELECT id FROM productSmall WHERE code = %s"
    cursor.execute(check_query, (code,))
    result = cursor.fetchone()

    if result:
        productSmall_id = result[0]

        insert_query = "INSERT INTO productMedia (total, productSmall_id, mediaType_id) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (total, productSmall_id, 5))
        conn.commit()

conn.commit()

# 커서와 연결 종료
cursor.close()
conn.close()



