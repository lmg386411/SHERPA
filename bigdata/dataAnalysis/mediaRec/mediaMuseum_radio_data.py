# 매체 호감 데이터 전처리한 csv 파일 서버에 넣는 코드
import pandas as pd
import mysql.connector

# TV - 영상 / 라디오 - 라디오 / 인쇄 - 인쇄 / 옥외 - 옥외 / SNS / 커뮤니티
data_radio = pd.read_csv('../csv/한국방송광고진흥공사_광고박물관 소장 광고소재(라디오광고) 현황_20220311 (1).csv', encoding='cp949', low_memory=False)
# print(data_radio)  # [3176 rows x 9 columns]

# 안쓰는 컬럼들 정리
data_radio_colums = data_radio.columns
# Index(['파일명', '년도', '광고주', '대분류', '중분류', '소분류', '제품명', '제목', '대행사'], dtype='object')
radio = data_radio[['년도', '광고주', '대분류', '중분류', '소분류', '제품명', '제목']].drop_duplicates()
# print(radio)  # [3153 rows x 7 columns]

# 제작년도에 Nan인 것은 3000으로 전처리
for _, item in radio.iterrows():
    if pd.isna(item['년도']):
        item['년도'] = 3000
        # print(item)

# 제작년도로 정렬
radio = radio[radio['년도'] >= 1990]
# print(radio)  # [1493 rows x 7 columns]

# 대분류/중분류/소분류 우리꺼 맞춰서 수정 *** 중요 ***
radio_options = radio.drop_duplicates(subset=['대분류', '중분류', '소분류'])
radio_options = radio_options.sort_values(by=['대분류', '중분류', '소분류'])
# print(radio_options)  # [221 rows x 7 columns]
# for _, item in radio_options.iterrows():
    # print(item['대분류'], ",", item['중분류'], ",", item['소분류'], sep="")

radio['code'] = 0
for idx, item in radio.iterrows():
    if item['대분류'] == "가정용 전기전자" and item['중분류'] == "가사용 전기전자":
        radio.at[idx, 'code'] = 3101
    elif item['대분류'] == "가정용 전기전자" and item['중분류'] == "가정용 전기전자 기타":
        radio.at[idx, 'code'] = 3199
    elif item['대분류'] == "가정용 전기전자" and item['중분류'] == "냉방 및 공기 청정기":
        radio.at[idx, 'code'] = 3102
    elif item['대분류'] == "가정용 전기전자" and item['중분류'] == "냉방 및 공기청정기":
        radio.at[idx, 'code'] = 3102
    elif item['대분류'] == "가정용 전기전자" and item['중분류'] == "영상기기":
        radio.at[idx, 'code'] = 3199
    elif item['대분류'] == "가정용 전기전자" and item['중분류'] == "음향기기":
        radio.at[idx, 'code'] = 3199
    elif item['대분류'] == "가정용 전기전자" and item['중분류'] == "조명 및 전기소품":
        radio.at[idx, 'code'] = 3201
    elif item['대분류'] == "가정용 전기전자" and item['중분류'] == "주방용 전기전자":
        radio.at[idx, 'code'] = 3203
    elif item['대분류'] == "가정용품" and item['중분류'] == "가구류" and item['소분류'] == "주방용 가구":
        radio.at[idx, 'code'] = 3203
        continue
    elif item['대분류'] == "가정용품" and item['중분류'] == "가구류":
        radio.at[idx, 'code'] = 3201
    elif item['대분류'] == "가정용품" and item['중분류'] == "가정용 인테리어":
        radio.at[idx, 'code'] = 3404
    elif item['대분류'] == "가정용품" and item['중분류'] == "난방기기":
        radio.at[idx, 'code'] = 3102
    elif item['대분류'] == "가정용품" and item['중분류'] == "방취 및 방균제":
        radio.at[idx, 'code'] = 4110
    elif item['대분류'] == "가정용품" and item['중분류'] == "생활잡화 및 기기":
        radio.at[idx, 'code'] = 4110
    elif item['대분류'] == "가정용품" and item['중분류'] == "세제류":
        radio.at[idx, 'code'] = 3299
    elif item['대분류'] == "가정용품" and item['중분류'] == "식품 기타":
        radio.at[idx, 'code'] = 2499
    elif item['대분류'] == "가정용품" and item['중분류'] == "악기류":
        radio.at[idx, 'code'] = 6100
    elif item['대분류'] == "가정용품" and item['중분류'] == "주방용품":
        radio.at[idx, 'code'] = 3299
    elif item['대분류'] == "가정용품" and item['중분류'] == "취미,레저용품":
        radio.at[idx, 'code'] = 6099
    elif item['대분류'] == "가정용품" and item['중분류'] == "컴퓨터S/W":
        radio.at[idx, 'code'] = 6104
    elif item['대분류'] == "가정용품" and item['중분류'] == "완구류":
        radio.at[idx, 'code'] = 6204
    elif item['대분류'] == "건설, 건재 및 부동산":
        radio.at[idx, 'code'] = 8210
    elif item['대분류'] == "건설,건재 및 부동산":
        radio.at[idx, 'code'] = 8210
    elif item['대분류'] == "관공서 및 단체" and item['중분류'] == "관공서 및 단체 기타":
        radio.at[idx, 'code'] = 4202
    elif item['대분류'] == "관공서 및 단체" and item['중분류'] == "단체":
        radio.at[idx, 'code'] = 6101
    elif item['대분류'] == "관공서 및 단체" and item['중분류'] == "중앙 및 지방 관공서":
        radio.at[idx, 'code'] = 4202
    elif item['대분류'] == "교육 및 복지 후생" and item['중분류'] == "교육 및 복지후생 기타":
        radio.at[idx, 'code'] = 4202
    elif item['대분류'] == "교육 및 복지후생" and item['중분류'] == "교육기관":
        radio.at[idx, 'code'] = 4202
    elif item['대분류'] == "교육 및 복지 후생" and item['중분류'] == "교육기관":
        radio.at[idx, 'code'] = 4202
    elif item['대분류'] == "그룹 및 기업광고" and item['중분류'] == "그룹광고":
        radio.at[idx, 'code'] = 9001
    elif item['대분류'] == "그룹 및 기업광고" and item['중분류'] == "기타광고":
        radio.at[idx, 'code'] = 9001
    elif item['대분류'] == "금융, 보험 및 증권":
        radio.at[idx, 'code'] = 8099
    elif item['대분류'] == "기초재" and item['중분류'] == "기초재 기타":
        radio.at[idx, 'code'] = 3406
    elif item['대분류'] == "기초재" and item['중분류'] == "농축수산 기초재":
        radio.at[idx, 'code'] = 3406
    elif item['대분류'] == "기초재" and item['중분류'] == "석탄,석유 및 가스":
        radio.at[idx, 'code'] = 4199
    elif item['대분류'] == "기초재" and item['중분류'] == "석탄, 석유 및 가스":
        radio.at[idx, 'code'] = 4199
    elif item['대분류'] == "서비스" and item['중분류'] == "개인서비스":
        radio.at[idx, 'code'] = 4199
    elif item['대분류'] == "서비스" and item['중분류'] == "문화 및 공연":
        radio.at[idx, 'code'] = 6210
    elif item['대분류'] == "서비스" and item['중분류'] == "서비스 기타":
        radio.at[idx, 'code'] = 6299
    elif item['대분류'] == "서비스" and item['중분류'] == "스포츠 및 오락시설":
        radio.at[idx, 'code'] = 6001
    elif item['대분류'] == "서비스" and item['중분류'] == "여행":
        radio.at[idx, 'code'] = 5301
    elif item['대분류'] == "서비스" and item['중분류'] == "운송":
        radio.at[idx, 'code'] = 5399
    elif item['대분류'] == "서비스" and item['중분류'] == "음식 및 숙박":
        radio.at[idx, 'code'] = 5103
    elif item['대분류'] == "서비스" and item['중분류'] == "전문서비스":
        radio.at[idx, 'code'] = 8211
    elif item['대분류'] == "수송기기" and item['중분류'] == "수송기기 기타":
        radio.at[idx, 'code'] = 8205
    elif item['대분류'] == "수송기기" and item['중분류'] == "수송기기 부품 및 용품":
        radio.at[idx, 'code'] = 8205
    elif item['대분류'] == "수송기기" and item['중분류'] == "수입자동차":
        radio.at[idx, 'code'] = 9099
    elif item['대분류'] == "수송기기" and item['중분류'] == "승용자동차":
        radio.at[idx, 'code'] = 9099
    elif item['대분류'] == "수송기기" and item['중분류'] == "승합차":
        radio.at[idx, 'code'] = 9099
    elif item['대분류'] == "수송기기" and item['중분류'] == "오토바이":
        radio.at[idx, 'code'] = 9099
    elif item['대분류'] == "수송기기" and item['중분류'] == "자전거":
        radio.at[idx, 'code'] = 9099
    elif item['대분류'] == "수송기기" and item['중분류'] == "자전거 ":
        radio.at[idx, 'code'] = 9099
    elif item['대분류'] == "수송기기" and item['중분류'] == "트럭":
        radio.at[idx, 'code'] = 9099
    elif item['대분류'] == "수송기기" and item['중분류'] == "특수자동차":
        radio.at[idx, 'code'] = 9099
    elif item['대분류'] == "식품" and item['중분류'] == "건강식품":
        radio.at[idx, 'code'] = 2404
    elif item['대분류'] == "식품" and item['중분류'] == "농산품":
        radio.at[idx, 'code'] = 2406
    elif item['대분류'] == "식품" and item['중분류'] == "대용식품":
        radio.at[idx, 'code'] = 2199
    elif item['대분류'] == "식품" and item['중분류'] == "면류":
        radio.at[idx, 'code'] = 2104
    elif item['대분류'] == "식품" and item['중분류'] == "수산품":
        radio.at[idx, 'code'] = 2406
    elif item['대분류'] == "식품" and item['중분류'] == "식품 기타":
        radio.at[idx, 'code'] = 2499
    elif item['대분류'] == "식품" and item['중분류'] == "아이스크림":
        radio.at[idx, 'code'] = 2044
    elif item['대분류'] == "식품" and item['중분류'] == "유제품":
        radio.at[idx, 'code'] = 2044
    elif item['대분류'] == "식품" and item['중분류'] == "제과":
        radio.at[idx, 'code'] = 2044
    elif item['대분류'] == "식품" and item['중분류'] == "제빵":
        radio.at[idx, 'code'] = 2044
    elif item['대분류'] == "식품" and item['중분류'] == "조미향신료":
        radio.at[idx, 'code'] = 2044
    elif item['대분류'] == "식품" and item['중분류'] == "축산품":
        radio.at[idx, 'code'] = 2406
    elif item['대분류'] == "유통" and item['중분류'] == "대형유통":
        radio.at[idx, 'code'] =  4123
    elif item['대분류'] == "유통" and item['중분류'] == "소형, 소매유통":
        radio.at[idx, 'code'] = 4107
    elif item['대분류'] == "유통" and item['중분류'] == "유통 기타":
        radio.at[idx, 'code'] = 4123
    elif item['대분류'] == "유통" and item['중분류'] == "특수유통":
        radio.at[idx, 'code'] = 4123
    elif item['대분류'] == "음료 및 기호식품" and item['중분류'] == "기호식품":
        radio.at[idx, 'code'] = 2406
    elif item['대분류'] == "음료 및 기호식품" and item['중분류'] == "비알콜음료":
        radio.at[idx, 'code'] = 2499
    elif item['대분류'] == "음료 및 기호식품" and item['중분류'] == "알콜음료":
        radio.at[idx, 'code'] = 2407
    elif item['대분류'] == "음료 및 기호식품" and item['중분류'] == "음료 및 기호식품 기타":
        radio.at[idx, 'code'] = 2499
    elif item['대분류'] == "정밀기기 및 사무기기" and item['중분류'] == "문구류":
        radio.at[idx, 'code'] = 6114
    elif item['대분류'] == "정밀기기 및 사무기기" and item['중분류'] == "사무기기":
        radio.at[idx, 'code'] = 6101
    elif item['대분류'] == "정밀기기 및 사무기기" and item['중분류'] == "시계":
        radio.at[idx, 'code'] = 6101
    elif item['대분류'] == "정밀기기 및 사무기기" and item['중분류'] == "이광학기기":
        radio.at[idx, 'code'] = 6102
    elif item['대분류'] == "정밀기기 및 사무기기" and item['중분류'] == "정밀기기 및 사무기기 기타":
        radio.at[idx, 'code'] = 3101
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "감기약":
        radio.at[idx, 'code'] = 7005
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "근육 및 신경통제":
        radio.at[idx, 'code'] = 7005
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "농축산약제":
        radio.at[idx, 'code'] = 7009
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "대사성의약":
        radio.at[idx, 'code'] = 7009
    elif item['대분류'] == "제약 및 외료" and item['중분류'] == "대사성의약":
        radio.at[idx, 'code'] = 7009
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "두피 및 피부용제":
        radio.at[idx, 'code'] = 7009
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "백신,구충 및 살충제":
        radio.at[idx, 'code'] = 7099
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "백신, 구충 및 살충제":
        radio.at[idx, 'code'] = 7099
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "생리피임 및 치질용약":
        radio.at[idx, 'code'] = 7005
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "소화위장약":
        radio.at[idx, 'code'] = 7005
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "순환기관용제":
        radio.at[idx, 'code'] = 7005
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "의료기기":
        radio.at[idx, 'code'] = 7107
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "의료용품":
        radio.at[idx, 'code'] = 7107
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "이비인후, 치과 및 안과용제":
        radio.at[idx, 'code'] = 7099
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "제약 및 의료 기타":
        radio.at[idx, 'code'] = 7099
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "진통제 및 안정제":
        radio.at[idx, 'code'] = 7005
    elif item['대분류'] == "출판" and item['중분류'] == "서적":
        radio.at[idx, 'code'] = 6199
    elif item['대분류'] == "출판" and item['중분류'] == "신문":
        radio.at[idx, 'code'] = 6199
    elif item['대분류'] == "출판" and item['중분류'] == "여가용 S/W":
        radio.at[idx, 'code'] = 6299
    elif item['대분류'] == "출판" and item['중분류'] == "여가용S/W":
        radio.at[idx, 'code'] = 6299
    elif item['대분류'] == "출판" and item['중분류'] == "유아용 교재":
        radio.at[idx, 'code'] = 8114
    elif item['대분류'] == "출판" and item['중분류'] == "일반용 교재":
        radio.at[idx, 'code'] = 8111
    elif item['대분류'] == "출판" and item['중분류'] == "잡지":
        radio.at[idx, 'code'] = 6199
    elif item['대분류'] == "출핀" and item['중분류'] == "중고생용 교재":
        radio.at[idx, 'code'] = 8199
    elif item['대분류'] == "출판" and item['중분류'] == "중고생용 교재":
        radio.at[idx, 'code'] = 8199
    elif item['대분류'] == "출판" and item['중분류'] == "초등학생용 교재":
        radio.at[idx, 'code'] = 8199
    elif item['대분류'] == "출판" and item['중분류'] == "출판 기타":
        radio.at[idx, 'code'] = 6199
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "방송":
        radio.at[idx, 'code'] = 6102
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "컴퓨터":
        radio.at[idx, 'code'] = 6103
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "컴퓨터 및 정보통신 기타":
        radio.at[idx, 'code'] = 6102
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "컴퓨터 출력장치":
        radio.at[idx, 'code'] = 6103
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "컴퓨터 카드류":
        radio.at[idx, 'code'] = 6103
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "컴퓨터S/W":
        radio.at[idx, 'code'] = 6103
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "컴퓨터 용품":
        radio.at[idx, 'code'] = 6103
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "통신기기":
        radio.at[idx, 'code'] = 6103
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "통신망":
        radio.at[idx, 'code'] = 6102
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "통신정보 서비스":
        radio.at[idx, 'code'] = 6102
    elif item['대분류'] == "패션" and item['중분류'] == "가방류":
        radio.at[idx, 'code'] = 1205
    elif item['대분류'] == "패션" and item['중분류'] == "내의류":
        radio.at[idx, 'code'] = 1008
    elif item['대분류'] == "패션" and item['중분류'] == "스포츠 전문복":
        radio.at[idx, 'code'] = 1099
    elif item['대분류'] == "패션" and item['중분류'] == "신발류":
        radio.at[idx, 'code'] = 1099
    elif item['대분류'] == "패션" and item['중분류'] == "원사 및 원단":
        radio.at[idx, 'code'] = 1199
    elif item['대분류'] == "패션" and item['중분류'] == "유아 및 아동복":
        radio.at[idx, 'code'] = 1007
    elif item['대분류'] == "패션" and item['중분류'] == "정장의류":
        radio.at[idx, 'code'] = 1001
    elif item['대분류'] == "패션" and item['중분류'] == "캐주얼의류":
        radio.at[idx, 'code'] = 1004
    elif item['대분류'] == "패션" and item['중분류'] == "패션 신변용품":
        radio.at[idx, 'code'] = 1299
    elif item['대분류'] == "패션" and item['중분류'] == "패션기타":
        radio.at[idx, 'code'] = 1299
    elif item['대분류'] == "패션" and item['중분류'] == "패션 기타":
        radio.at[idx, 'code'] = 1299
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "가정 및 보건용 제지":
        radio.at[idx, 'code'] = 7099
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "구강용품":
        radio.at[idx, 'code'] = 7099
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "남성 화장품":
        radio.at[idx, 'code'] = 7106
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "모발 및 목욕용제":
        radio.at[idx, 'code'] = 7199
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "모욕 및 목욕용제":
        radio.at[idx, 'code'] = 7199
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "방향 화장품":
        radio.at[idx, 'code'] = 7199
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "세제류":
        radio.at[idx, 'code'] = 7199
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "여성 기초화장품":
        radio.at[idx, 'code'] = 7106
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "여성 색조화장품":
        radio.at[idx, 'code'] = 7106
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "여성 썬탠류":
        radio.at[idx, 'code'] = 7106
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "유,아동용 화장 및 세제":
        radio.at[idx, 'code'] = 8110
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "화장도구":
        radio.at[idx, 'code'] = 7108
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "화장품 및 보건용품 기타":
        radio.at[idx, 'code'] = 7199
    elif item['대분류'] == "화학공업" and item['중분류'] == "고무 및 플라스틴":
        radio.at[idx, 'code'] = 9001
    elif item['대분류'] == "화학공업" and item['중분류'] == "화학공업 기타":
        radio.at[idx, 'code'] = 9001
    elif item['대분류'] == "화학공업" and item['중분류'] == "화학제품":
        radio.at[idx, 'code'] = 9001
    else:
        print(item)


# 광고 사용률 - 그룹화
radio = radio[['년도', '대분류', '중분류', '소분류', '제품명', 'code']]
# print(radio)  # [1493 rows x 6 columns]

# 3. 데이터 합치기: 'total' 값 추출
# 대분류, 중분류, 소분류, code 가 모두 같은 항목들을 그룹화하고 각 그룹의 크기를 계산하여 'total' 열에 저장
radio['total'] = radio.groupby(['대분류', '중분류', '소분류', 'code'])['제품명'].transform('count')
merged_radio_data = radio[['code', 'total']].drop_duplicates()
# print(merged_radio_data)  # [143 rows x 2 columns]
# productMedia
# id fk fk fk total
# id / 매체유형 / 매체유형 소분류 / 업종명 소분류 / total
#  / 라디오 / 4 / code / total

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

for _, item in merged_radio_data.iterrows():
    print(_)
    total = int(item['total'])  # numpy.int64를 정수로 변환
    code = int(item['code'])  # numpy.int64를 정수로 변환

    check_query = "SELECT id FROM productSmall WHERE code = %s"
    cursor.execute(check_query, (code,))
    result = cursor.fetchone()

    if result:
        productSmall_id = result[0]

        insert_query = "INSERT INTO productMedia (total, productSmall_id, mediaType_id) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (total, productSmall_id, 4))
        conn.commit()

conn.commit()

# 커서와 연결 종료
cursor.close()
conn.close()



