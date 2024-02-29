# 매체 호감 데이터 전처리한 csv 파일 서버에 넣는 코드
import pandas as pd
import mysql.connector

# tv - 영상 / 라디오 - 라디오 / 인쇄 - 인쇄 / 옥외 - 옥외 / SNS / 커뮤니티
data_outdoor = pd.read_csv('../csv/한국방송광고진흥공사_광고박물관 소장 광고소재(옥외광고) 현황_20220311.csv', encoding='cp949', low_memory=False)
# print(data_outdoor)  # [1508 rows x 8 columns]

# 안쓰는 컬럼들 정리
data_outdoor_colums = data_outdoor.columns
# print(data_outdoor_colums)
# Index(['번호', '광고주', '대분류', '중분류', '소분류', '제목', '내용', '매체'], dtype='object')
# outdoor = data_outdoor[['내용']].drop_duplicates()
# for _, item in outdoor.iterrows():
#     print(item['내용'])

data_outdoor = data_outdoor[['번호', '대분류', '중분류', '소분류', '제목', '내용']].drop_duplicates()
print(data_outdoor)  # [17851 rows x 7 columns]

outdoor_bus = data_outdoor[(data_outdoor['내용'] == "버스광고") | (data_outdoor['내용'] == "택시정류장") | (data_outdoor['내용'] == "정류장") | (data_outdoor['내용'] == "차량광고_버스") |
                           (data_outdoor['내용'] == "버스래핑광고") | (data_outdoor['내용'] == "교통광고") | (data_outdoor['내용'] == "차량광고_택시, 승용차, 탑차") | (data_outdoor['내용'] == "차량래핑광고") |
                           (data_outdoor['내용'] == "버스쉘터광고") | (data_outdoor['내용'] == "택시 쉘터광고") | (data_outdoor['내용'] == "고속도로 안내판광고") | (data_outdoor['내용'] == "자가용광고") |
                           (data_outdoor['내용'] == "자동세차장광고") | (data_outdoor['내용'] == "오토바이래핑광고") | (data_outdoor['내용'] == "차량광고") | (data_outdoor['내용'] == "옥상광고") |
                           (data_outdoor['내용'] == "이동통신 매장광고") | (data_outdoor['내용'] == "입간판") | (data_outdoor['내용'] == "기업광고") | (data_outdoor['내용'] == "조형물") |
                            (data_outdoor['내용'] == "스포츠센터 광고") | (data_outdoor['내용'] == "건물래핑광고") | (data_outdoor['내용'] == "노래방광고") | (data_outdoor['내용'] == "찻집광고") |
                           (data_outdoor['내용'] == "병원광고") | (data_outdoor['내용'] == "은행광고") | (data_outdoor['내용'] == "서점광고") | (data_outdoor['내용'] == "전광판광고")
                           ]
print(outdoor_bus)  # [278 rows x 8 columns]
outdoor_sub = data_outdoor[(data_outdoor['내용'] == "지하철광고") | (data_outdoor['내용'] == "서울역 천정배너광고") | (data_outdoor['내용'] == "지하철 래핑광고") | (data_outdoor['내용'] == "브라비아 지하철래핑광고") |
                           (data_outdoor['내용'] == "지하철")| (data_outdoor['내용'] == "코엑스몰 바닥광고") | (data_outdoor['내용'] == "벽면래핑광고") | (data_outdoor['내용'] == "건물외벽래핑") |
                           (data_outdoor['내용'] == "건물외벽 래핑광고") | (data_outdoor['내용'] == "계단래핑광고") | (data_outdoor['내용'] == "래핑열차") | (data_outdoor['내용'] == "지하철래핑광고") | (data_outdoor['내용'] == "벽면그림") |
                           (data_outdoor['내용'] == "돌출간판") | (data_outdoor['내용'] == "헤어샵 매장광고") | (data_outdoor['내용'] == "베이커리 매장광고") | (data_outdoor['내용'] == "음식점 매장광고") |
                           (data_outdoor['내용'] == "제과점 매장광고") | (data_outdoor['내용'] == "제과점 광고") | (data_outdoor['내용'] == "편의점 광고") | (data_outdoor['내용'] == "미용실 매장광고") |
                           (data_outdoor['내용'] == "건설광고") | (data_outdoor['내용'] == "지방자치단체 광고") | (data_outdoor['내용'] == "아파트광고") | (data_outdoor['내용'] == "약국광고") |
                           (data_outdoor['내용'] == "의류 매장광고") | (data_outdoor['내용'] == "극장광고") | (data_outdoor['내용'] == "숙박광고") | (data_outdoor['내용'] == "에드벌룬")
                           ]
print(outdoor_sub)  # [306 rows x 8 columns]
outdoor_card = data_outdoor[(data_outdoor['내용'] == "현수막") | (data_outdoor['내용'] == "현수막_돌출, 지주이용형") | (data_outdoor['내용'] == "현수막_벽면이용형") |
                            (data_outdoor['내용'] == "플랜카드") | (data_outdoor['내용'] == "매장광고") | (data_outdoor['내용'] == "플랜카드") |
                            (data_outdoor['내용'] == "입간판") | (data_outdoor['내용'] == "포스터") | (data_outdoor['내용'] == "깃발") |
                            (data_outdoor['내용'] == "기둥") | (data_outdoor['내용'] == "전광판광고") | (data_outdoor['내용'] == "배너게시대") |
                            (data_outdoor['내용'] == "배너거치대") | (data_outdoor['내용'] == "베너광고") | (data_outdoor['내용'] == "바닥광고") |
                            (data_outdoor['내용'] == "외벽 현수막") | (data_outdoor['내용'] == "건물외벽 실사출력") | (data_outdoor['내용'] == "안내사인")|
                            (data_outdoor['내용'] == "체험포토존") | (data_outdoor['내용'] == "화장품 매장광고") | (data_outdoor['내용'] == "주점 매장광고") | (data_outdoor['내용'] == "일출상징탑") |
                           (data_outdoor['내용'] == "백페인트글라스") | (data_outdoor['내용'] == "야립간판") | (data_outdoor['내용'] == "동출간판") | (data_outdoor['내용'] == "마네킹광고") |
                            (data_outdoor['내용'] == "조형물광고") | (data_outdoor['내용'] == "LED") | (data_outdoor['내용'] == "톨출사인") | (data_outdoor['내용'] == "실사출력") |
                            (data_outdoor['내용'] == "물스크린광고") | (data_outdoor['내용'] == "파라솔광고") | (data_outdoor['내용'] == "이미지간판") | (data_outdoor['내용'] == "경기장광고") |
                            (data_outdoor['내용'] == "건물외벽실사출력") | (data_outdoor['내용'] == "외부조형물광고") | (data_outdoor['내용'] == "이미지광고") | (data_outdoor['내용'] == " 기둥광고") |
                            (data_outdoor['내용'] == "베너실사출력") | (data_outdoor['내용'] == "조형간판") | (data_outdoor['내용'] == "경기장 바닥광고") | (data_outdoor['내용'] == "외벽 LED광고") |
                            (data_outdoor['내용'] == "볼타렌광고") | (data_outdoor['내용'] == "돌출간판 외곽의 LED전광판") | (data_outdoor['내용'] == "백화점광고") | (data_outdoor['내용'] == "LED도트형 채널사인")
                            ]
print(outdoor_card)  # [250 rows x 8 columns]


# 대분류/중분류/소분류 우리꺼 맞춰서 수정 *** 중요 ***
# outdoor_options = data_outdoor.drop_duplicates(subset=['대분류', '중분류', '소분류'])
# outdoor_options = outdoor_options.sort_values(by=['대분류', '중분류', '소분류'])
# print(outdoor_options)  # [213 rows x 6 columns]
# for _, item in outdoor_options.iterrows():
#     print(item['대분류'], ",", item['중분류'], ",", item['소분류'], sep="")

# outdoor_bus['code'] = 0
outdoor_bus.loc[:, 'code'] = 0
for idx, item in outdoor_bus.iterrows():
    if item['대분류'] == "가정용 전기전자" and item['중분류'] == "가사용 전기전자":
        outdoor_bus.at[idx, 'code'] = 3101
    elif item['대분류'] == "가정용 전기전자" and item['중분류'] == "가정용 전기전자 기타":
        outdoor_bus.at[idx, 'code'] = 3199
    elif item['대분류'] == "가정용 전기전자" and item['중분류'] == "냉방 및 공기 청정기":
        outdoor_bus.at[idx, 'code'] = 3102
    elif item['대분류'] == "가정용 전기전자" and item['중분류'] == "냉방 및 공기청정기":
        outdoor_bus.at[idx, 'code'] = 3102
    elif item['대분류'] == "가정용 전기정자" and item['중분류'] == "냉방 및 공기청정기":
        outdoor_bus.at[idx, 'code'] = 3102
    elif item['대분류'] == "가정용 전기전자" and item['중분류'] == "영상기기":
        outdoor_bus.at[idx, 'code'] = 3199
    elif item['대분류'] == "가정용 전기전자" and item['중분류'] == "음향기기":
        outdoor_bus.at[idx, 'code'] = 3199
    elif item['대분류'] == "가정용 전기전자" and item['중분류'] == "조명 및 전기소품":
        outdoor_bus.at[idx, 'code'] = 3201
    elif item['대분류'] == "가정용 전기전자" and item['중분류'] == "주방용 전기전자":
        outdoor_bus.at[idx, 'code'] = 3203
    elif item['대분류'] == "가정용품" and item['중분류'] == "가구류" and item['소분류'] == "주방용 가구":
        outdoor_bus.at[idx, 'code'] = 3203
        continue
    elif item['대분류'] == "가정용품" and item['중분류'] == "가구류":
        outdoor_bus.at[idx, 'code'] = 3201
    elif item['대분류'] == "가정용품" and item['중분류'] == "가정용 인테리어":
        outdoor_bus.at[idx, 'code'] = 3404
    elif item['대분류'] == "가정용품" and item['중분류'] == "난방기기":
        outdoor_bus.at[idx, 'code'] = 3102
    elif item['대분류'] == "가정용품" and item['중분류'] == "방취 및 방균제":
        outdoor_bus.at[idx, 'code'] = 4110
    elif item['대분류'] == "가정용품" and item['중분류'] == "생활잡화 및 기기":
        outdoor_bus.at[idx, 'code'] = 4110
    elif item['대분류'] == "가정용품" and item['중분류'] == "세제류":
        outdoor_bus.at[idx, 'code'] = 3299
    elif item['대분류'] == "가정용품" and item['중분류'] == "식품 기타":
        outdoor_bus.at[idx, 'code'] = 2499
    elif item['대분류'] == "가정용품" and item['중분류'] == "악기류":
        outdoor_bus.at[idx, 'code'] = 6100
    elif item['대분류'] == "가정용품" and item['중분류'] == "주방용품":
        outdoor_bus.at[idx, 'code'] = 3299
    elif item['대분류'] == "가정용품" and item['중분류'] == "취미,레저용품":
        outdoor_bus.at[idx, 'code'] = 6099
    elif item['대분류'] == "가정용품" and item['중분류'] == "컴퓨터S/W":
        outdoor_bus.at[idx, 'code'] = 6104
    elif item['대분류'] == "가정용품" and item['중분류'] == "완구류":
        outdoor_bus.at[idx, 'code'] = 6204
    elif item['대분류'] == "건설, 건재 및 부동산":
        outdoor_bus.at[idx, 'code'] = 8210
    elif item['대분류'] == "관공서 및 단체" and item['중분류'] == "관공서 및 단체 기타":
        outdoor_bus.at[idx, 'code'] = 4202
    elif item['대분류'] == "관공서 및 단체" and item['중분류'] == "단체":
        outdoor_bus.at[idx, 'code'] = 6101
    elif item['대분류'] == "관공서 및 단체" and item['중분류'] == "중앙 및 지방 관공서":
        outdoor_bus.at[idx, 'code'] = 4202
    elif item['대분류'] == "교육 및 복지 후생" and item['중분류'] == "교육 및 복지후생 기타":
        outdoor_bus.at[idx, 'code'] = 4202
    elif item['대분류'] == "교육 및 복지 후생" and item['중분류'] == "교육기관":
        outdoor_bus.at[idx, 'code'] = 4202
    elif item['대분류'] == "교육 및 복지후생" and item['중분류'] == "교육기관":
        outdoor_bus.at[idx, 'code'] = 4202
    elif item['대분류'] == "그룹 및 기업광고" and item['중분류'] == "그룹광고":
        outdoor_bus.at[idx, 'code'] = 9001
    elif item['대분류'] == "그룹 및 기업광고" and item['중분류'] == "기타광고":
        outdoor_bus.at[idx, 'code'] = 9001
    elif item['대분류'] == "금융, 보험 및 증권":
        outdoor_bus.at[idx, 'code'] = 8099
    elif item['대분류'] == "기초재" and item['중분류'] == "기초재 기타":
        outdoor_bus.at[idx, 'code'] = 3406
    elif item['대분류'] == "기초재" and item['중분류'] == "농축수산 기초재":
        outdoor_bus.at[idx, 'code'] = 3406
    elif item['대분류'] == "기초재" and item['중분류'] == "금속":
        outdoor_bus.at[idx, 'code'] = 3499
    elif item['대분류'] == "기초재" and item['중분류'] == "석탄,석유 및 가스":
        outdoor_bus.at[idx, 'code'] = 4199
    elif item['대분류'] == "서비스" and item['중분류'] == "개인서비스":
        outdoor_bus.at[idx, 'code'] = 4199
    elif item['대분류'] == "서비스" and item['중분류'] == "문화 및 공연":
        outdoor_bus.at[idx, 'code'] = 6210
    elif item['대분류'] == "서비스" and item['중분류'] == "서비스 기타":
        outdoor_bus.at[idx, 'code'] = 6299
    elif item['대분류'] == "서비스" and item['중분류'] == "스포츠 및 오락시설":
        outdoor_bus.at[idx, 'code'] = 6001
    elif item['대분류'] == "서비스" and item['중분류'] == "여행":
        outdoor_bus.at[idx, 'code'] = 5301
    elif item['대분류'] == "서비스" and item['중분류'] == "운송":
        outdoor_bus.at[idx, 'code'] = 5399
    elif item['대분류'] == "서비스" and item['중분류'] == "음식 및 숙박":
        outdoor_bus.at[idx, 'code'] = 5103
    elif item['대분류'] == "서비스" and item['중분류'] == "전문서비스":
        outdoor_bus.at[idx, 'code'] = 8211
    elif item['대분류'] == "서비스" and item['중분류'] == "물품임대":
        outdoor_bus.at[idx, 'code'] = 5399
    elif item['대분류'] == "수송기기" and item['중분류'] == "수송기기 기타":
        outdoor_bus.at[idx, 'code'] = 8205
    elif item['대분류'] == "수송기기" and item['중분류'] == "수송기기 부품 및 용품":
        outdoor_bus.at[idx, 'code'] = 8205
    elif item['대분류'] == "수송기기" and item['중분류'] == "수입자동차":
        outdoor_bus.at[idx, 'code'] = 9099
    elif item['대분류'] == "수송기기" and item['중분류'] == "승용자동차":
        outdoor_bus.at[idx, 'code'] = 9099
    elif item['대분류'] == "수송기기" and item['중분류'] == "승합차":
        outdoor_bus.at[idx, 'code'] = 9099
    elif item['대분류'] == "수송기기" and item['중분류'] == "오토바이":
        outdoor_bus.at[idx, 'code'] = 9099
    elif item['대분류'] == "수송기기" and item['중분류'] == "자전거":
        outdoor_bus.at[idx, 'code'] = 9099
    elif item['대분류'] == "수송기기" and item['중분류'] == "트럭":
        outdoor_bus.at[idx, 'code'] = 9099
    elif item['대분류'] == "수송기기" and item['중분류'] == "특수자동차":
        outdoor_bus.at[idx, 'code'] = 9099
    elif item['대분류'] == "식품" and item['중분류'] == "건강식품":
        outdoor_bus.at[idx, 'code'] = 2404
    elif item['대분류'] == "식품" and item['중분류'] == "농산품":
        outdoor_bus.at[idx, 'code'] = 2406
    elif item['대분류'] == "식품" and item['중분류'] == "대용식품":
        outdoor_bus.at[idx, 'code'] = 2199
    elif item['대분류'] == "식품" and item['중분류'] == "면류":
        outdoor_bus.at[idx, 'code'] = 2104
    elif item['대분류'] == "식품" and item['중분류'] == "수산품":
        outdoor_bus.at[idx, 'code'] = 2406
    elif item['대분류'] == "식품" and item['중분류'] == "식품 기타":
        outdoor_bus.at[idx, 'code'] = 2499
    elif item['대분류'] == "식품" and item['중분류'] == "식품기타":
        outdoor_bus.at[idx, 'code'] = 2499
    elif item['대분류'] == "식품" and item['중분류'] == "아이스크림":
        outdoor_bus.at[idx, 'code'] = 2044
    elif item['대분류'] == "식품" and item['중분류'] == "유제품":
        outdoor_bus.at[idx, 'code'] = 2044
    elif item['대분류'] == "식품" and item['중분류'] == "제과":
        outdoor_bus.at[idx, 'code'] = 2044
    elif item['대분류'] == "식품" and item['중분류'] == "제빵":
        outdoor_bus.at[idx, 'code'] = 2044
    elif item['대분류'] == "식품" and item['중분류'] == "조미향신료":
        outdoor_bus.at[idx, 'code'] = 2044
    elif item['대분류'] == "식품" and item['중분류'] == "축산품":
        outdoor_bus.at[idx, 'code'] = 2406
    elif item['대분류'] == "유통" and item['중분류'] == "대형유통":
        outdoor_bus.at[idx, 'code'] =  4123
    elif item['대분류'] == "유통" and item['중분류'] == "소형, 소매유통":
        outdoor_bus.at[idx, 'code'] = 4107
    elif item['대분류'] == "유통" and item['중분류'] == "유통 기타":
        outdoor_bus.at[idx, 'code'] = 4123
    elif item['대분류'] == "유통" and item['중분류'] == "특수유통":
        outdoor_bus.at[idx, 'code'] = 4123
    elif item['대분류'] == "음료 및 기호식품" and item['중분류'] == "기호식품":
        outdoor_bus.at[idx, 'code'] = 2406
    elif item['대분류'] == "음료 및 기호식품" and item['중분류'] == "비알콜음료":
        outdoor_bus.at[idx, 'code'] = 2499
    elif item['대분류'] == "음료 및 기호식품" and item['중분류'] == "알콜음료":
        outdoor_bus.at[idx, 'code'] = 2407
    elif item['대분류'] == "음료 및 기호식품" and item['중분류'] == "음료 및 기호식품 기타":
        outdoor_bus.at[idx, 'code'] = 2499
    elif item['대분류'] == "정밀기기 및 사무기기" and item['중분류'] == "문구류":
        outdoor_bus.at[idx, 'code'] = 6114
    elif item['대분류'] == "정밀기기 및 사무기기" and item['중분류'] == "사무기기":
        outdoor_bus.at[idx, 'code'] = 6101
    elif item['대분류'] == "정밀기기 및 사무기기" and item['중분류'] == "시계":
        outdoor_bus.at[idx, 'code'] = 6101
    elif item['대분류'] == "정밀기기 및 사무기기" and item['중분류'] == "이광학기기":
        outdoor_bus.at[idx, 'code'] = 6102
    elif item['대분류'] == "정밀기기 및 사무기기" and item['중분류'] == "정밀기기 및 사무기기 기타":
        outdoor_bus.at[idx, 'code'] = 3101
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "감기약":
        outdoor_bus.at[idx, 'code'] = 7005
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "근육 및 신경통제":
        outdoor_bus.at[idx, 'code'] = 7005
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "농축산약제":
        outdoor_bus.at[idx, 'code'] = 7009
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "대사성의약":
        outdoor_bus.at[idx, 'code'] = 7009
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "두피 및 피부용제":
        outdoor_bus.at[idx, 'code'] = 7009
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "백신,구충 및 살충제":
        outdoor_bus.at[idx, 'code'] = 7099
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "백신, 구충 및 살충제":
        outdoor_bus.at[idx, 'code'] = 7099
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "생리피임 및 치질용약":
        outdoor_bus.at[idx, 'code'] = 7005
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "소화위장약":
        outdoor_bus.at[idx, 'code'] = 7005
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "순환기관용제":
        outdoor_bus.at[idx, 'code'] = 7005
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "의료기기":
        outdoor_bus.at[idx, 'code'] = 7107
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "의료용품":
        outdoor_bus.at[idx, 'code'] = 7107
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "이비인후, 치과 및 안과용제":
        outdoor_bus.at[idx, 'code'] = 7099
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "의료 및 보건기관":
        outdoor_bus.at[idx, 'code'] = 7099
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "제약 및 의료 기타":
        outdoor_bus.at[idx, 'code'] = 7099
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "진통제 및 안정제":
        outdoor_bus.at[idx, 'code'] = 7005
    elif item['대분류'] == "출판" and item['중분류'] == "서적":
        outdoor_bus.at[idx, 'code'] = 6199
    elif item['대분류'] == "출판" and item['중분류'] == "신문":
        outdoor_bus.at[idx, 'code'] = 6199
    elif item['대분류'] == "출판" and item['중분류'] == "여가용 S/W":
        outdoor_bus.at[idx, 'code'] = 6299
    elif item['대분류'] == "출판" and item['중분류'] == "유아용 교재":
        outdoor_bus.at[idx, 'code'] = 8114
    elif item['대분류'] == "출판" and item['중분류'] == "일반용 교재":
        outdoor_bus.at[idx, 'code'] = 8111
    elif item['대분류'] == "출판" and item['중분류'] == "잡지":
        outdoor_bus.at[idx, 'code'] = 6199
    elif item['대분류'] == "출판" and item['중분류'] == "중고생용 교재":
        outdoor_bus.at[idx, 'code'] = 8199
    elif item['대분류'] == "출판" and item['중분류'] == "초등학생용 교재":
        outdoor_bus.at[idx, 'code'] = 8199
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "방송":
        outdoor_bus.at[idx, 'code'] = 6102
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "컴퓨터":
        outdoor_bus.at[idx, 'code'] = 6103
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "컴퓨터 및 정보통신 기타":
        outdoor_bus.at[idx, 'code'] = 6102
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "컴퓨터 출력장치":
        outdoor_bus.at[idx, 'code'] = 6103
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "컴퓨터 카드류":
        outdoor_bus.at[idx, 'code'] = 6103
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "컴퓨터S/W":
        outdoor_bus.at[idx, 'code'] = 6103
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "통신기기":
        outdoor_bus.at[idx, 'code'] = 6103
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "통신망":
        outdoor_bus.at[idx, 'code'] = 6102
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "통신정보 서비스":
        outdoor_bus.at[idx, 'code'] = 6102
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "통신정보서비스":
        outdoor_bus.at[idx, 'code'] = 6102
    elif item['대분류'] == "패션" and item['중분류'] == "가방류":
        outdoor_bus.at[idx, 'code'] = 1205
    elif item['대분류'] == "패션" and item['중분류'] == "내의류":
        outdoor_bus.at[idx, 'code'] = 1008
    elif item['대분류'] == "패션" and item['중분류'] == "스포츠 전문복":
        outdoor_bus.at[idx, 'code'] = 1099
    elif item['대분류'] == "패션" and item['중분류'] == "신발류":
        outdoor_bus.at[idx, 'code'] = 1099
    elif item['대분류'] == "패션" and item['중분류'] == "원사 및 원단":
        outdoor_bus.at[idx, 'code'] = 1199
    elif item['대분류'] == "패션" and item['중분류'] == "유아 및 아동복":
        outdoor_bus.at[idx, 'code'] = 1007
    elif item['대분류'] == "패션" and item['중분류'] == "정장의류":
        outdoor_bus.at[idx, 'code'] = 1001
    elif item['대분류'] == "패션" and item['중분류'] == "캐주얼의류":
        outdoor_bus.at[idx, 'code'] = 1004
    elif item['대분류'] == "패션" and item['중분류'] == "패션 신변용품":
        outdoor_bus.at[idx, 'code'] = 1299
    elif item['대분류'] == "패션" and item['중분류'] == "패션기타":
        outdoor_bus.at[idx, 'code'] = 1299
    elif item['대분류'] == "패션" and item['중분류'] == "패션 기타":
        outdoor_bus.at[idx, 'code'] = 1299
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "가정 및 보건용 제지":
        outdoor_bus.at[idx, 'code'] = 7099
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "구강용품":
        outdoor_bus.at[idx, 'code'] = 7099
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "남성 화장품":
        outdoor_bus.at[idx, 'code'] = 7106
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "모발 및 목욕용제":
        outdoor_bus.at[idx, 'code'] = 7199
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "방향 화장품":
        outdoor_bus.at[idx, 'code'] = 7199
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "세제류":
        outdoor_bus.at[idx, 'code'] = 7199
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "여성 기초화장품":
        outdoor_bus.at[idx, 'code'] = 7106
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "여성 색조화장품":
        outdoor_bus.at[idx, 'code'] = 7106
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "여성 썬탠류":
        outdoor_bus.at[idx, 'code'] = 7106
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "유,아동용 화장 및 세제":
        outdoor_bus.at[idx, 'code'] = 8110
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "화장도구":
        outdoor_bus.at[idx, 'code'] = 7108
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "화장품 및 보건용품 기타":
        outdoor_bus.at[idx, 'code'] = 7199
    elif item['대분류'] == "화학공업" and item['중분류'] == "고무 및 플라스틱":
        outdoor_bus.at[idx, 'code'] = 9001
    elif item['대분류'] == "화학공업" and item['중분류'] == "화학공업 기타":
        outdoor_bus.at[idx, 'code'] = 9001
    elif item['대분류'] == "화학공업" and item['중분류'] == "화학제품":
        outdoor_bus.at[idx, 'code'] = 9001
    else:
        print(item)

outdoor_sub.loc[:, 'code'] = 0
for idx, item in outdoor_sub.iterrows():
    if item['대분류'] == "가정용 전기전자" and item['중분류'] == "가사용 전기전자":
        outdoor_sub.at[idx, 'code'] = 3101
    elif item['대분류'] == "가정용 전기전자" and item['중분류'] == "가정용 전기전자 기타":
        outdoor_sub.at[idx, 'code'] = 3199
    elif item['대분류'] == "가정용 전기전자" and item['중분류'] == "냉방 및 공기 청정기":
        outdoor_sub.at[idx, 'code'] = 3102
    elif item['대분류'] == "가정용 전기전자" and item['중분류'] == "냉방 및 공기청정기":
        outdoor_sub.at[idx, 'code'] = 3102
    elif item['대분류'] == "가정용 전기정자" and item['중분류'] == "냉방 및 공기청정기":
        outdoor_sub.at[idx, 'code'] = 3102
    elif item['대분류'] == "가정용 전기전자" and item['중분류'] == "영상기기":
        outdoor_sub.at[idx, 'code'] = 3199
    elif item['대분류'] == "가정용 전기전자" and item['중분류'] == "음향기기":
        outdoor_sub.at[idx, 'code'] = 3199
    elif item['대분류'] == "가정용 전기전자" and item['중분류'] == "조명 및 전기소품":
        outdoor_sub.at[idx, 'code'] = 3201
    elif item['대분류'] == "가정용 전기전자" and item['중분류'] == "주방용 전기전자":
        outdoor_sub.at[idx, 'code'] = 3203
    elif item['대분류'] == "가정용품" and item['중분류'] == "가구류" and item['소분류'] == "주방용 가구":
        outdoor_sub.at[idx, 'code'] = 3203
        continue
    elif item['대분류'] == "가정용품" and item['중분류'] == "가구류":
        outdoor_sub.at[idx, 'code'] = 3201
    elif item['대분류'] == "가정용품" and item['중분류'] == "가정용 인테리어":
        outdoor_sub.at[idx, 'code'] = 3404
    elif item['대분류'] == "가정용품" and item['중분류'] == "난방기기":
        outdoor_sub.at[idx, 'code'] = 3102
    elif item['대분류'] == "가정용품" and item['중분류'] == "방취 및 방균제":
        outdoor_sub.at[idx, 'code'] = 4110
    elif item['대분류'] == "가정용품" and item['중분류'] == "생활잡화 및 기기":
        outdoor_sub.at[idx, 'code'] = 4110
    elif item['대분류'] == "가정용품" and item['중분류'] == "세제류":
        outdoor_sub.at[idx, 'code'] = 3299
    elif item['대분류'] == "가정용품" and item['중분류'] == "식품 기타":
        outdoor_sub.at[idx, 'code'] = 2499
    elif item['대분류'] == "가정용품" and item['중분류'] == "악기류":
        outdoor_sub.at[idx, 'code'] = 6100
    elif item['대분류'] == "가정용품" and item['중분류'] == "주방용품":
        outdoor_sub.at[idx, 'code'] = 3299
    elif item['대분류'] == "가정용품" and item['중분류'] == "취미,레저용품":
        outdoor_sub.at[idx, 'code'] = 6099
    elif item['대분류'] == "가정용품" and item['중분류'] == "컴퓨터S/W":
        outdoor_sub.at[idx, 'code'] = 6104
    elif item['대분류'] == "가정용품" and item['중분류'] == "완구류":
        outdoor_sub.at[idx, 'code'] = 6204
    elif item['대분류'] == "건설, 건재 및 부동산":
        outdoor_sub.at[idx, 'code'] = 8210
    elif item['대분류'] == "관공서 및 단체" and item['중분류'] == "관공서 및 단체 기타":
        outdoor_sub.at[idx, 'code'] = 4202
    elif item['대분류'] == "관공서 및 단체" and item['중분류'] == "단체":
        outdoor_sub.at[idx, 'code'] = 6101
    elif item['대분류'] == "관공서 및 단체" and item['중분류'] == "중앙 및 지방 관공서":
        outdoor_sub.at[idx, 'code'] = 4202
    elif item['대분류'] == "교육 및 복지 후생" and item['중분류'] == "교육 및 복지후생 기타":
        outdoor_sub.at[idx, 'code'] = 4202
    elif item['대분류'] == "교육 및 복지 후생" and item['중분류'] == "교육기관":
        outdoor_sub.at[idx, 'code'] = 4202
    elif item['대분류'] == "교육 및 복지후생" and item['중분류'] == "교육기관":
        outdoor_sub.at[idx, 'code'] = 4202
    elif item['대분류'] == "그룹 및 기업광고" and item['중분류'] == "그룹광고":
        outdoor_sub.at[idx, 'code'] = 9001
    elif item['대분류'] == "그룹 및 기업광고" and item['중분류'] == "기타광고":
        outdoor_sub.at[idx, 'code'] = 9001
    elif item['대분류'] == "금융, 보험 및 증권":
        outdoor_sub.at[idx, 'code'] = 8099
    elif item['대분류'] == "기초재" and item['중분류'] == "기초재 기타":
        outdoor_sub.at[idx, 'code'] = 3406
    elif item['대분류'] == "기초재" and item['중분류'] == "농축수산 기초재":
        outdoor_sub.at[idx, 'code'] = 3406
    elif item['대분류'] == "기초재" and item['중분류'] == "금속":
        outdoor_sub.at[idx, 'code'] = 3499
    elif item['대분류'] == "기초재" and item['중분류'] == "석탄,석유 및 가스":
        outdoor_sub.at[idx, 'code'] = 4199
    elif item['대분류'] == "서비스" and item['중분류'] == "개인서비스":
        outdoor_sub.at[idx, 'code'] = 4199
    elif item['대분류'] == "서비스" and item['중분류'] == "문화 및 공연":
        outdoor_sub.at[idx, 'code'] = 6210
    elif item['대분류'] == "서비스" and item['중분류'] == "서비스 기타":
        outdoor_sub.at[idx, 'code'] = 6299
    elif item['대분류'] == "서비스" and item['중분류'] == "스포츠 및 오락시설":
        outdoor_sub.at[idx, 'code'] = 6001
    elif item['대분류'] == "서비스" and item['중분류'] == "여행":
        outdoor_sub.at[idx, 'code'] = 5301
    elif item['대분류'] == "서비스" and item['중분류'] == "운송":
        outdoor_sub.at[idx, 'code'] = 5399
    elif item['대분류'] == "서비스" and item['중분류'] == "음식 및 숙박":
        outdoor_sub.at[idx, 'code'] = 5103
    elif item['대분류'] == "서비스" and item['중분류'] == "전문서비스":
        outdoor_sub.at[idx, 'code'] = 8211
    elif item['대분류'] == "서비스" and item['중분류'] == "물품임대":
        outdoor_sub.at[idx, 'code'] = 5399
    elif item['대분류'] == "수송기기" and item['중분류'] == "수송기기 기타":
        outdoor_sub.at[idx, 'code'] = 8205
    elif item['대분류'] == "수송기기" and item['중분류'] == "수송기기 부품 및 용품":
        outdoor_sub.at[idx, 'code'] = 8205
    elif item['대분류'] == "수송기기" and item['중분류'] == "수입자동차":
        outdoor_sub.at[idx, 'code'] = 9099
    elif item['대분류'] == "수송기기" and item['중분류'] == "승용자동차":
        outdoor_sub.at[idx, 'code'] = 9099
    elif item['대분류'] == "수송기기" and item['중분류'] == "승합차":
        outdoor_sub.at[idx, 'code'] = 9099
    elif item['대분류'] == "수송기기" and item['중분류'] == "오토바이":
        outdoor_sub.at[idx, 'code'] = 9099
    elif item['대분류'] == "수송기기" and item['중분류'] == "자전거":
        outdoor_sub.at[idx, 'code'] = 9099
    elif item['대분류'] == "수송기기" and item['중분류'] == "트럭":
        outdoor_sub.at[idx, 'code'] = 9099
    elif item['대분류'] == "수송기기" and item['중분류'] == "특수자동차":
        outdoor_sub.at[idx, 'code'] = 9099
    elif item['대분류'] == "식품" and item['중분류'] == "건강식품":
        outdoor_sub.at[idx, 'code'] = 2404
    elif item['대분류'] == "식품" and item['중분류'] == "농산품":
        outdoor_sub.at[idx, 'code'] = 2406
    elif item['대분류'] == "식품" and item['중분류'] == "대용식품":
        outdoor_sub.at[idx, 'code'] = 2199
    elif item['대분류'] == "식품" and item['중분류'] == "면류":
        outdoor_sub.at[idx, 'code'] = 2104
    elif item['대분류'] == "식품" and item['중분류'] == "수산품":
        outdoor_sub.at[idx, 'code'] = 2406
    elif item['대분류'] == "식품" and item['중분류'] == "식품 기타":
        outdoor_sub.at[idx, 'code'] = 2499
    elif item['대분류'] == "식품" and item['중분류'] == "식품기타":
        outdoor_sub.at[idx, 'code'] = 2499
    elif item['대분류'] == "식품" and item['중분류'] == "아이스크림":
        outdoor_sub.at[idx, 'code'] = 2044
    elif item['대분류'] == "식품" and item['중분류'] == "유제품":
        outdoor_sub.at[idx, 'code'] = 2044
    elif item['대분류'] == "식품" and item['중분류'] == "제과":
        outdoor_sub.at[idx, 'code'] = 2044
    elif item['대분류'] == "식품" and item['중분류'] == "제빵":
        outdoor_sub.at[idx, 'code'] = 2044
    elif item['대분류'] == "식품" and item['중분류'] == "조미향신료":
        outdoor_sub.at[idx, 'code'] = 2044
    elif item['대분류'] == "식품" and item['중분류'] == "축산품":
        outdoor_sub.at[idx, 'code'] = 2406
    elif item['대분류'] == "유통" and item['중분류'] == "대형유통":
        outdoor_sub.at[idx, 'code'] =  4123
    elif item['대분류'] == "유통" and item['중분류'] == "소형, 소매유통":
        outdoor_sub.at[idx, 'code'] = 4107
    elif item['대분류'] == "유통" and item['중분류'] == "유통 기타":
        outdoor_sub.at[idx, 'code'] = 4123
    elif item['대분류'] == "유통" and item['중분류'] == "특수유통":
        outdoor_sub.at[idx, 'code'] = 4123
    elif item['대분류'] == "음료 및 기호식품" and item['중분류'] == "기호식품":
        outdoor_sub.at[idx, 'code'] = 2406
    elif item['대분류'] == "음료 및 기호식품" and item['중분류'] == "비알콜음료":
        outdoor_sub.at[idx, 'code'] = 2499
    elif item['대분류'] == "음료 및 기호식품" and item['중분류'] == "알콜음료":
        outdoor_sub.at[idx, 'code'] = 2407
    elif item['대분류'] == "음료 및 기호식품" and item['중분류'] == "음료 및 기호식품 기타":
        outdoor_sub.at[idx, 'code'] = 2499
    elif item['대분류'] == "정밀기기 및 사무기기" and item['중분류'] == "문구류":
        outdoor_sub.at[idx, 'code'] = 6114
    elif item['대분류'] == "정밀기기 및 사무기기" and item['중분류'] == "사무기기":
        outdoor_sub.at[idx, 'code'] = 6101
    elif item['대분류'] == "정밀기기 및 사무기기" and item['중분류'] == "시계":
        outdoor_sub.at[idx, 'code'] = 6101
    elif item['대분류'] == "정밀기기 및 사무기기" and item['중분류'] == "이광학기기":
        outdoor_sub.at[idx, 'code'] = 6102
    elif item['대분류'] == "정밀기기 및 사무기기" and item['중분류'] == "정밀기기 및 사무기기 기타":
        outdoor_sub.at[idx, 'code'] = 3101
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "감기약":
        outdoor_sub.at[idx, 'code'] = 7005
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "근육 및 신경통제":
        outdoor_sub.at[idx, 'code'] = 7005
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "농축산약제":
        outdoor_sub.at[idx, 'code'] = 7009
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "대사성의약":
        outdoor_sub.at[idx, 'code'] = 7009
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "두피 및 피부용제":
        outdoor_sub.at[idx, 'code'] = 7009
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "백신,구충 및 살충제":
        outdoor_sub.at[idx, 'code'] = 7099
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "백신, 구충 및 살충제":
        outdoor_sub.at[idx, 'code'] = 7099
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "생리피임 및 치질용약":
        outdoor_sub.at[idx, 'code'] = 7005
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "소화위장약":
        outdoor_sub.at[idx, 'code'] = 7005
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "순환기관용제":
        outdoor_sub.at[idx, 'code'] = 7005
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "의료기기":
        outdoor_sub.at[idx, 'code'] = 7107
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "의료용품":
        outdoor_sub.at[idx, 'code'] = 7107
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "이비인후, 치과 및 안과용제":
        outdoor_sub.at[idx, 'code'] = 7099
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "의료 및 보건기관":
        outdoor_sub.at[idx, 'code'] = 7099
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "제약 및 의료 기타":
        outdoor_sub.at[idx, 'code'] = 7099
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "진통제 및 안정제":
        outdoor_sub.at[idx, 'code'] = 7005
    elif item['대분류'] == "출판" and item['중분류'] == "서적":
        outdoor_sub.at[idx, 'code'] = 6199
    elif item['대분류'] == "출판" and item['중분류'] == "신문":
        outdoor_sub.at[idx, 'code'] = 6199
    elif item['대분류'] == "출판" and item['중분류'] == "여가용 S/W":
        outdoor_sub.at[idx, 'code'] = 6299
    elif item['대분류'] == "출판" and item['중분류'] == "유아용 교재":
        outdoor_sub.at[idx, 'code'] = 8114
    elif item['대분류'] == "출판" and item['중분류'] == "일반용 교재":
        outdoor_sub.at[idx, 'code'] = 8111
    elif item['대분류'] == "출판" and item['중분류'] == "잡지":
        outdoor_sub.at[idx, 'code'] = 6199
    elif item['대분류'] == "출판" and item['중분류'] == "중고생용 교재":
        outdoor_sub.at[idx, 'code'] = 8199
    elif item['대분류'] == "출판" and item['중분류'] == "초등학생용 교재":
        outdoor_sub.at[idx, 'code'] = 8199
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "방송":
        outdoor_sub.at[idx, 'code'] = 6102
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "컴퓨터":
        outdoor_sub.at[idx, 'code'] = 6103
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "컴퓨터 및 정보통신 기타":
        outdoor_sub.at[idx, 'code'] = 6102
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "컴퓨터 출력장치":
        outdoor_sub.at[idx, 'code'] = 6103
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "컴퓨터 카드류":
        outdoor_sub.at[idx, 'code'] = 6103
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "컴퓨터S/W":
        outdoor_sub.at[idx, 'code'] = 6103
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "통신기기":
        outdoor_sub.at[idx, 'code'] = 6103
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "통신망":
        outdoor_sub.at[idx, 'code'] = 6102
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "통신정보 서비스":
        outdoor_sub.at[idx, 'code'] = 6102
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "통신정보서비스":
        outdoor_sub.at[idx, 'code'] = 6102
    elif item['대분류'] == "패션" and item['중분류'] == "가방류":
        outdoor_sub.at[idx, 'code'] = 1205
    elif item['대분류'] == "패션" and item['중분류'] == "내의류":
        outdoor_sub.at[idx, 'code'] = 1008
    elif item['대분류'] == "패션" and item['중분류'] == "스포츠 전문복":
        outdoor_sub.at[idx, 'code'] = 1099
    elif item['대분류'] == "패션" and item['중분류'] == "신발류":
        outdoor_sub.at[idx, 'code'] = 1099
    elif item['대분류'] == "패션" and item['중분류'] == "원사 및 원단":
        outdoor_sub.at[idx, 'code'] = 1199
    elif item['대분류'] == "패션" and item['중분류'] == "유아 및 아동복":
        outdoor_sub.at[idx, 'code'] = 1007
    elif item['대분류'] == "패션" and item['중분류'] == "정장의류":
        outdoor_sub.at[idx, 'code'] = 1001
    elif item['대분류'] == "패션" and item['중분류'] == "캐주얼의류":
        outdoor_sub.at[idx, 'code'] = 1004
    elif item['대분류'] == "패션" and item['중분류'] == "패션 신변용품":
        outdoor_sub.at[idx, 'code'] = 1299
    elif item['대분류'] == "패션" and item['중분류'] == "패션기타":
        outdoor_sub.at[idx, 'code'] = 1299
    elif item['대분류'] == "패션" and item['중분류'] == "패션 기타":
        outdoor_sub.at[idx, 'code'] = 1299
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "가정 및 보건용 제지":
        outdoor_sub.at[idx, 'code'] = 7099
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "구강용품":
        outdoor_sub.at[idx, 'code'] = 7099
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "남성 화장품":
        outdoor_sub.at[idx, 'code'] = 7106
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "모발 및 목욕용제":
        outdoor_sub.at[idx, 'code'] = 7199
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "방향 화장품":
        outdoor_sub.at[idx, 'code'] = 7199
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "세제류":
        outdoor_sub.at[idx, 'code'] = 7199
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "여성 기초화장품":
        outdoor_sub.at[idx, 'code'] = 7106
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "여성 색조화장품":
        outdoor_sub.at[idx, 'code'] = 7106
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "여성 썬탠류":
        outdoor_sub.at[idx, 'code'] = 7106
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "유,아동용 화장 및 세제":
        outdoor_sub.at[idx, 'code'] = 8110
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "화장도구":
        outdoor_sub.at[idx, 'code'] = 7108
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "화장품 및 보건용품 기타":
        outdoor_sub.at[idx, 'code'] = 7199
    elif item['대분류'] == "화학공업" and item['중분류'] == "고무 및 플라스틱":
        outdoor_sub.at[idx, 'code'] = 9001
    elif item['대분류'] == "화학공업" and item['중분류'] == "화학공업 기타":
        outdoor_sub.at[idx, 'code'] = 9001
    elif item['대분류'] == "화학공업" and item['중분류'] == "화학제품":
        outdoor_sub.at[idx, 'code'] = 9001
    else:
        print(item)

outdoor_card.loc[:, 'code'] = 0
for idx, item in outdoor_card.iterrows():
    if item['대분류'] == "가정용 전기전자" and item['중분류'] == "가사용 전기전자":
        outdoor_card.at[idx, 'code'] = 3101
    elif item['대분류'] == "가정용 전기전자" and item['중분류'] == "가정용 전기전자 기타":
        outdoor_card.at[idx, 'code'] = 3199
    elif item['대분류'] == "가정용 전기전자" and item['중분류'] == "냉방 및 공기 청정기":
        outdoor_card.at[idx, 'code'] = 3102
    elif item['대분류'] == "가정용 전기전자" and item['중분류'] == "냉방 및 공기청정기":
        outdoor_card.at[idx, 'code'] = 3102
    elif item['대분류'] == "가정용 전기정자" and item['중분류'] == "냉방 및 공기청정기":
        outdoor_card.at[idx, 'code'] = 3102
    elif item['대분류'] == "가정용 전기전자" and item['중분류'] == "영상기기":
        outdoor_card.at[idx, 'code'] = 3199
    elif item['대분류'] == "가정용 전기전자" and item['중분류'] == "음향기기":
        outdoor_card.at[idx, 'code'] = 3199
    elif item['대분류'] == "가정용 전기전자" and item['중분류'] == "조명 및 전기소품":
        outdoor_card.at[idx, 'code'] = 3201
    elif item['대분류'] == "가정용 전기전자" and item['중분류'] == "주방용 전기전자":
        outdoor_card.at[idx, 'code'] = 3203
    elif item['대분류'] == "가정용품" and item['중분류'] == "가구류" and item['소분류'] == "주방용 가구":
        outdoor_card.at[idx, 'code'] = 3203
        continue
    elif item['대분류'] == "가정용품" and item['중분류'] == "가구류":
        outdoor_card.at[idx, 'code'] = 3201
    elif item['대분류'] == "가정용품" and item['중분류'] == "가정용 인테리어":
        outdoor_card.at[idx, 'code'] = 3404
    elif item['대분류'] == "가정용품" and item['중분류'] == "난방기기":
        outdoor_card.at[idx, 'code'] = 3102
    elif item['대분류'] == "가정용품" and item['중분류'] == "방취 및 방균제":
        outdoor_card.at[idx, 'code'] = 4110
    elif item['대분류'] == "가정용품" and item['중분류'] == "생활잡화 및 기기":
        outdoor_card.at[idx, 'code'] = 4110
    elif item['대분류'] == "가정용품" and item['중분류'] == "세제류":
        outdoor_card.at[idx, 'code'] = 3299
    elif item['대분류'] == "가정용품" and item['중분류'] == "식품 기타":
        outdoor_card.at[idx, 'code'] = 2499
    elif item['대분류'] == "가정용품" and item['중분류'] == "악기류":
        outdoor_card.at[idx, 'code'] = 6100
    elif item['대분류'] == "가정용품" and item['중분류'] == "주방용품":
        outdoor_card.at[idx, 'code'] = 3299
    elif item['대분류'] == "가정용품" and item['중분류'] == "취미,레저용품":
        outdoor_card.at[idx, 'code'] = 6099
    elif item['대분류'] == "가정용품" and item['중분류'] == "컴퓨터S/W":
        outdoor_card.at[idx, 'code'] = 6104
    elif item['대분류'] == "가정용품" and item['중분류'] == "완구류":
        outdoor_card.at[idx, 'code'] = 6204
    elif item['대분류'] == "건설, 건재 및 부동산":
        outdoor_card.at[idx, 'code'] = 8210
    elif item['대분류'] == "관공서 및 단체" and item['중분류'] == "관공서 및 단체 기타":
        outdoor_card.at[idx, 'code'] = 4202
    elif item['대분류'] == "관공서 및 단체" and item['중분류'] == "단체":
        outdoor_card.at[idx, 'code'] = 6101
    elif item['대분류'] == "관공서 및 단체" and item['중분류'] == "중앙 및 지방 관공서":
        outdoor_card.at[idx, 'code'] = 4202
    elif item['대분류'] == "교육 및 복지 후생" and item['중분류'] == "교육 및 복지후생 기타":
        outdoor_card.at[idx, 'code'] = 4202
    elif item['대분류'] == "교육 및 복지 후생" and item['중분류'] == "교육기관":
        outdoor_card.at[idx, 'code'] = 4202
    elif item['대분류'] == "교육 및 복지후생" and item['중분류'] == "교육기관":
        outdoor_card.at[idx, 'code'] = 4202
    elif item['대분류'] == "그룹 및 기업광고" and item['중분류'] == "그룹광고":
        outdoor_card.at[idx, 'code'] = 9001
    elif item['대분류'] == "그룹 및 기업광고" and item['중분류'] == "기타광고":
        outdoor_card.at[idx, 'code'] = 9001
    elif item['대분류'] == "금융, 보험 및 증권":
        outdoor_card.at[idx, 'code'] = 8099
    elif item['대분류'] == "기초재" and item['중분류'] == "기초재 기타":
        outdoor_card.at[idx, 'code'] = 3406
    elif item['대분류'] == "기초재" and item['중분류'] == "농축수산 기초재":
        outdoor_card.at[idx, 'code'] = 3406
    elif item['대분류'] == "기초재" and item['중분류'] == "금속":
        outdoor_card.at[idx, 'code'] = 3499
    elif item['대분류'] == "기초재" and item['중분류'] == "석탄,석유 및 가스":
        outdoor_card.at[idx, 'code'] = 4199
    elif item['대분류'] == "산업기기" and item['중분류'] == "상업 및 공업용 기기":
        outdoor_card.at[idx, 'code'] = 3402
    elif item['대분류'] == "서비스" and item['중분류'] == "개인서비스":
        outdoor_card.at[idx, 'code'] = 4199
    elif item['대분류'] == "서비스" and item['중분류'] == "문화 및 공연":
        outdoor_card.at[idx, 'code'] = 6210
    elif item['대분류'] == "서비스" and item['중분류'] == "서비스 기타":
        outdoor_card.at[idx, 'code'] = 6299
    elif item['대분류'] == "서비스" and item['중분류'] == "스포츠 및 오락시설":
        outdoor_card.at[idx, 'code'] = 6001
    elif item['대분류'] == "서비스" and item['중분류'] == "여행":
        outdoor_card.at[idx, 'code'] = 5301
    elif item['대분류'] == "서비스" and item['중분류'] == "운송":
        outdoor_card.at[idx, 'code'] = 5399
    elif item['대분류'] == "서비스" and item['중분류'] == "음식 및 숙박":
        outdoor_card.at[idx, 'code'] = 5103
    elif item['대분류'] == "서비스" and item['중분류'] == "전문서비스":
        outdoor_card.at[idx, 'code'] = 8211
    elif item['대분류'] == "서비스" and item['중분류'] == "물품임대":
        outdoor_card.at[idx, 'code'] = 5399
    elif item['대분류'] == "수송기기" and item['중분류'] == "수송기기 기타":
        outdoor_card.at[idx, 'code'] = 8205
    elif item['대분류'] == "수송기기" and item['중분류'] == "수송기기 부품 및 용품":
        outdoor_card.at[idx, 'code'] = 8205
    elif item['대분류'] == "수송기기" and item['중분류'] == "수입자동차":
        outdoor_card.at[idx, 'code'] = 9099
    elif item['대분류'] == "수송기기" and item['중분류'] == "승용자동차":
        outdoor_card.at[idx, 'code'] = 9099
    elif item['대분류'] == "수송기기" and item['중분류'] == "승합차":
        outdoor_card.at[idx, 'code'] = 9099
    elif item['대분류'] == "수송기기" and item['중분류'] == "오토바이":
        outdoor_card.at[idx, 'code'] = 9099
    elif item['대분류'] == "수송기기" and item['중분류'] == "자전거":
        outdoor_card.at[idx, 'code'] = 9099
    elif item['대분류'] == "수송기기" and item['중분류'] == "트럭":
        outdoor_card.at[idx, 'code'] = 9099
    elif item['대분류'] == "수송기기" and item['중분류'] == "특수자동차":
        outdoor_card.at[idx, 'code'] = 9099
    elif item['대분류'] == "식품" and item['중분류'] == "건강식품":
        outdoor_card.at[idx, 'code'] = 2404
    elif item['대분류'] == "식품" and item['중분류'] == "농산품":
        outdoor_card.at[idx, 'code'] = 2406
    elif item['대분류'] == "식품" and item['중분류'] == "대용식품":
        outdoor_card.at[idx, 'code'] = 2199
    elif item['대분류'] == "식품" and item['중분류'] == "면류":
        outdoor_card.at[idx, 'code'] = 2104
    elif item['대분류'] == "식품" and item['중분류'] == "수산품":
        outdoor_card.at[idx, 'code'] = 2406
    elif item['대분류'] == "식품" and item['중분류'] == "식품 기타":
        outdoor_card.at[idx, 'code'] = 2499
    elif item['대분류'] == "식품" and item['중분류'] == "식품기타":
        outdoor_card.at[idx, 'code'] = 2499
    elif item['대분류'] == "식품" and item['중분류'] == "아이스크림":
        outdoor_card.at[idx, 'code'] = 2044
    elif item['대분류'] == "식품" and item['중분류'] == "유제품":
        outdoor_card.at[idx, 'code'] = 2044
    elif item['대분류'] == "식품" and item['중분류'] == "제과":
        outdoor_card.at[idx, 'code'] = 2044
    elif item['대분류'] == "식품" and item['중분류'] == "제빵":
        outdoor_card.at[idx, 'code'] = 2044
    elif item['대분류'] == "식품" and item['중분류'] == "조미향신료":
        outdoor_card.at[idx, 'code'] = 2044
    elif item['대분류'] == "식품" and item['중분류'] == "축산품":
        outdoor_card.at[idx, 'code'] = 2406
    elif item['대분류'] == "유통" and item['중분류'] == "대형유통":
        outdoor_card.at[idx, 'code'] =  4123
    elif item['대분류'] == "유통" and item['중분류'] == "소형, 소매유통":
        outdoor_card.at[idx, 'code'] = 4107
    elif item['대분류'] == "유통" and item['중분류'] == "유통 기타":
        outdoor_card.at[idx, 'code'] = 4123
    elif item['대분류'] == "유통" and item['중분류'] == "특수유통":
        outdoor_card.at[idx, 'code'] = 4123
    elif item['대분류'] == "음료 및 기호식품" and item['중분류'] == "기호식품":
        outdoor_card.at[idx, 'code'] = 2406
    elif item['대분류'] == "음료 및 기호식품" and item['중분류'] == "비알콜음료":
        outdoor_card.at[idx, 'code'] = 2499
    elif item['대분류'] == "음료 및 기호식품" and item['중분류'] == "알콜음료":
        outdoor_card.at[idx, 'code'] = 2407
    elif item['대분류'] == "음료 및 기호식품" and item['중분류'] == "음료 및 기호식품 기타":
        outdoor_card.at[idx, 'code'] = 2499
    elif item['대분류'] == "정밀기기 및 사무기기" and item['중분류'] == "문구류":
        outdoor_card.at[idx, 'code'] = 6114
    elif item['대분류'] == "정밀기기 및 사무기기" and item['중분류'] == "사무기기":
        outdoor_card.at[idx, 'code'] = 6101
    elif item['대분류'] == "정밀기기 및 사무기기" and item['중분류'] == "시계":
        outdoor_card.at[idx, 'code'] = 6101
    elif item['대분류'] == "정밀기기 및 사무기기" and item['중분류'] == "이광학기기":
        outdoor_card.at[idx, 'code'] = 6102
    elif item['대분류'] == "정밀기기 및 사무기기" and item['중분류'] == "정밀기기 및 사무기기 기타":
        outdoor_card.at[idx, 'code'] = 3101
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "감기약":
        outdoor_card.at[idx, 'code'] = 7005
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "근육 및 신경통제":
        outdoor_card.at[idx, 'code'] = 7005
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "농축산약제":
        outdoor_card.at[idx, 'code'] = 7009
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "대사성의약":
        outdoor_card.at[idx, 'code'] = 7009
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "두피 및 피부용제":
        outdoor_card.at[idx, 'code'] = 7009
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "백신,구충 및 살충제":
        outdoor_card.at[idx, 'code'] = 7099
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "백신, 구충 및 살충제":
        outdoor_card.at[idx, 'code'] = 7099
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "생리피임 및 치질용약":
        outdoor_card.at[idx, 'code'] = 7005
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "소화위장약":
        outdoor_card.at[idx, 'code'] = 7005
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "순환기관용제":
        outdoor_card.at[idx, 'code'] = 7005
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "의료기기":
        outdoor_card.at[idx, 'code'] = 7107
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "의료용품":
        outdoor_card.at[idx, 'code'] = 7107
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "이비인후, 치과 및 안과용제":
        outdoor_card.at[idx, 'code'] = 7099
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "의료 및 보건기관":
        outdoor_card.at[idx, 'code'] = 7099
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "제약 및 의료 기타":
        outdoor_card.at[idx, 'code'] = 7099
    elif item['대분류'] == "제약 및 의료" and item['중분류'] == "진통제 및 안정제":
        outdoor_card.at[idx, 'code'] = 7005
    elif item['대분류'] == "출판" and item['중분류'] == "서적":
        outdoor_card.at[idx, 'code'] = 6199
    elif item['대분류'] == "출판" and item['중분류'] == "출판 기타":
        outdoor_card.at[idx, 'code'] = 6199
    elif item['대분류'] == "출판" and item['중분류'] == "신문":
        outdoor_card.at[idx, 'code'] = 6199
    elif item['대분류'] == "출판" and item['중분류'] == "여가용 S/W":
        outdoor_card.at[idx, 'code'] = 6299
    elif item['대분류'] == "출판" and item['중분류'] == "유아용 교재":
        outdoor_card.at[idx, 'code'] = 8114
    elif item['대분류'] == "출판" and item['중분류'] == "일반용 교재":
        outdoor_card.at[idx, 'code'] = 8111
    elif item['대분류'] == "출판" and item['중분류'] == "잡지":
        outdoor_card.at[idx, 'code'] = 6199
    elif item['대분류'] == "출판" and item['중분류'] == "중고생용 교재":
        outdoor_card.at[idx, 'code'] = 8199
    elif item['대분류'] == "출판" and item['중분류'] == "초등학생용 교재":
        outdoor_card.at[idx, 'code'] = 8199
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "방송":
        outdoor_card.at[idx, 'code'] = 6102
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "컴퓨터":
        outdoor_card.at[idx, 'code'] = 6103
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "컴퓨터 및 정보통신 기타":
        outdoor_card.at[idx, 'code'] = 6102
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "컴퓨터 출력장치":
        outdoor_card.at[idx, 'code'] = 6103
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "컴퓨터 카드류":
        outdoor_card.at[idx, 'code'] = 6103
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "컴퓨터S/W":
        outdoor_card.at[idx, 'code'] = 6103
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "통신기기":
        outdoor_card.at[idx, 'code'] = 6103
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "통신망":
        outdoor_card.at[idx, 'code'] = 6102
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "통신정보 서비스":
        outdoor_card.at[idx, 'code'] = 6102
    elif item['대분류'] == "컴퓨터 및 정보통신" and item['중분류'] == "통신정보서비스":
        outdoor_card.at[idx, 'code'] = 6102
    elif item['대분류'] == "패션" and item['중분류'] == "가방류":
        outdoor_card.at[idx, 'code'] = 1205
    elif item['대분류'] == "패션" and item['중분류'] == "내의류":
        outdoor_card.at[idx, 'code'] = 1008
    elif item['대분류'] == "패션" and item['중분류'] == "스포츠 전문복":
        outdoor_card.at[idx, 'code'] = 1099
    elif item['대분류'] == "패션" and item['중분류'] == "신발류":
        outdoor_card.at[idx, 'code'] = 1099
    elif item['대분류'] == "패션" and item['중분류'] == "원사 및 원단":
        outdoor_card.at[idx, 'code'] = 1199
    elif item['대분류'] == "패션" and item['중분류'] == "유아 및 아동복":
        outdoor_card.at[idx, 'code'] = 1007
    elif item['대분류'] == "패션" and item['중분류'] == "정장의류":
        outdoor_card.at[idx, 'code'] = 1001
    elif item['대분류'] == "패션" and item['중분류'] == "캐주얼의류":
        outdoor_card.at[idx, 'code'] = 1004
    elif item['대분류'] == "패션" and item['중분류'] == "패션 신변용품":
        outdoor_card.at[idx, 'code'] = 1299
    elif item['대분류'] == "패션" and item['중분류'] == "패션기타":
        outdoor_card.at[idx, 'code'] = 1299
    elif item['대분류'] == "패션" and item['중분류'] == "패션 기타":
        outdoor_card.at[idx, 'code'] = 1299
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "가정 및 보건용 제지":
        outdoor_card.at[idx, 'code'] = 7099
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "구강용품":
        outdoor_card.at[idx, 'code'] = 7099
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "남성 화장품":
        outdoor_card.at[idx, 'code'] = 7106
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "모발 및 목욕용제":
        outdoor_card.at[idx, 'code'] = 7199
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "방향 화장품":
        outdoor_card.at[idx, 'code'] = 7199
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "세제류":
        outdoor_card.at[idx, 'code'] = 7199
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "여성 기초화장품":
        outdoor_card.at[idx, 'code'] = 7106
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "여성 색조화장품":
        outdoor_card.at[idx, 'code'] = 7106
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "여성 썬탠류":
        outdoor_card.at[idx, 'code'] = 7106
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "유,아동용 화장 및 세제":
        outdoor_card.at[idx, 'code'] = 8110
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "화장도구":
        outdoor_card.at[idx, 'code'] = 7108
    elif item['대분류'] == "화장품 및 보건용품" and item['중분류'] == "화장품 및 보건용품 기타":
        outdoor_card.at[idx, 'code'] = 7199
    elif item['대분류'] == "화학공업" and item['중분류'] == "고무 및 플라스틱":
        outdoor_card.at[idx, 'code'] = 9001
    elif item['대분류'] == "화학공업" and item['중분류'] == "화학공업 기타":
        outdoor_card.at[idx, 'code'] = 9001
    elif item['대분류'] == "화학공업" and item['중분류'] == "화학제품":
        outdoor_card.at[idx, 'code'] = 9001
    else:
        print(item)

# 광고 사용률 - 그룹화
# data_outdoor = data_outdoor[['번호', '대분류', '중분류', '소분류', '제목', '내용']].drop_duplicates()
outdoor_bus = outdoor_bus[['번호', '대분류', '중분류', '소분류', '제목', 'code']]
# print(outdoor_bus)  # [278 rows x 6 columns]
outdoor_sub = outdoor_sub[['번호', '대분류', '중분류', '소분류', '제목', 'code']]
# print(outdoor_sub)  # [306 rows x 6 columns]
outdoor_card = outdoor_card[['번호', '대분류', '중분류', '소분류', '제목', 'code']]
# print(outdoor_card)  # [250 rows x 6 columns]

# 3. 데이터 합치기: 'total' 값 추출
# 대분류, 중분류, 소분류, code 가 모두 같은 항목들을 그룹화하고 각 그룹의 크기를 계산하여 'total' 열에 저장
outdoor_bus['total'] = outdoor_bus.groupby(['대분류', '중분류', '소분류', 'code'])['번호'].transform('count')
merged_outdoor_bus = outdoor_bus[['code', 'total']].drop_duplicates()
# print(merged_outdoor_bus)  # [66 rows x 2 columns]
outdoor_sub['total'] = outdoor_sub.groupby(['대분류', '중분류', '소분류', 'code'])['번호'].transform('count')
merged_outdoor_sub = outdoor_sub[['code', 'total']].drop_duplicates()
# print(merged_outdoor_sub)  # [64 rows x 2 columns]
outdoor_card['total'] = outdoor_card.groupby(['대분류', '중분류', '소분류', 'code'])['번호'].transform('count')
merged_outdoor_card = outdoor_card[['code', 'total']].drop_duplicates()
# print(merged_outdoor_card)  # [59 rows x 2 columns]
# productMedia
# id fk fk fk total
# id / 매체유형 / 매체유형 소분류 / 업종명 소분류 / total

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

for _, item in merged_outdoor_bus.iterrows():
    print(_)
    total = int(item['total'])  # numpy.int64를 정수로 변환
    code = int(item['code'])  # numpy.int64를 정수로 변환

    check_query = "SELECT id FROM productSmall WHERE code = %s"
    cursor.execute(check_query, (code,))
    result = cursor.fetchone()

    if result:
        productSmall_id = result[0]

        insert_query = "INSERT INTO productMedia (total, productSmall_id, mediaType_id, mediaSub_id) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert_query, (total, productSmall_id, 6, 1))
        conn.commit()

for _, item in merged_outdoor_sub.iterrows():
    print(_)
    total = int(item['total'])  # numpy.int64를 정수로 변환
    code = int(item['code'])  # numpy.int64를 정수로 변환

    check_query = "SELECT id FROM productSmall WHERE code = %s"
    cursor.execute(check_query, (code,))
    result = cursor.fetchone()

    if result:
        productSmall_id = result[0]

        insert_query = "INSERT INTO productMedia (total, productSmall_id, mediaType_id, mediaSub_id) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert_query, (total, productSmall_id, 6, 2))
        conn.commit()

for _, item in merged_outdoor_card.iterrows():
    print(_)
    total = int(item['total'])  # numpy.int64를 정수로 변환
    code = int(item['code'])  # numpy.int64를 정수로 변환

    check_query = "SELECT id FROM productSmall WHERE code = %s"
    cursor.execute(check_query, (code,))
    result = cursor.fetchone()

    if result:
        productSmall_id = result[0]

        insert_query = "INSERT INTO productMedia (total, productSmall_id, mediaType_id, mediaSub_id) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert_query, (total, productSmall_id, 6, 3))
        conn.commit()

conn.commit()

# 커서와 연결 종료
cursor.close()
conn.close()



