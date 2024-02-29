import pymysql
import pandas as pd


# # 연결 설정
connection = pymysql.connect(
    host='j9c107.p.ssafy.io',
    user='c107',
    password='c107adrec',
    database='adrec'
)


# 커서 생성
cursor = connection.cursor()


# CSV 파일이 있는 디렉토리 경로
csv_file_ad_detail = 'data/keyword/AiSAC 광고소재명별 광고 정보.csv'
csv_file_ad_keyword = 'data/keyword/AiSAC시스템 AI 인식결과 및 광고소재명별 키워드.csv'
csv_file_keyword_product = 'data/keyword/keword_product.csv'


dataframe_ad_detail = pd.read_csv(csv_file_ad_detail, encoding='cp949')
dataframe_ad_keyword = pd.read_csv(csv_file_ad_keyword, encoding='cp949')
dataframe_keyword_product = pd.read_csv(csv_file_keyword_product, encoding='cp949')

idx = 0
pi = 0
keyword_product={}

for row_num, row in dataframe_keyword_product.iterrows():
    large_product = row['large']
    middle_product = row['medium']
    small_product = row['small']
    product_id = [word.strip("' ").strip() for word in row['product_id'].split(', ')]

    if large_product in keyword_product:

        if middle_product in keyword_product[large_product]:

            if small_product in keyword_product[large_product][middle_product]:
                for i in product_id:
                    pi+=1
                    keyword_product[large_product][middle_product][small_product].append(int(i))
            else:
                keyword_product[large_product][middle_product][small_product]=[]
                for i in product_id:
                    pi+=1
                    keyword_product[large_product][middle_product][small_product].append(int(i))
        else:
            keyword_product[large_product][middle_product]={}
            keyword_product[large_product][middle_product][small_product]=[]
            for i in product_id:
                    pi+=1
                    keyword_product[large_product][middle_product][small_product].append(int(i))
    else:
        keyword_product[large_product]={}
        keyword_product[large_product][middle_product]={}
        keyword_product[large_product][middle_product][small_product]=[]
        for i in product_id:
                pi+=1
                keyword_product[large_product][middle_product][small_product].append(int(i))

data = {}
for row_num_ad_detail, row_ad_detail in dataframe_ad_detail.iterrows():
    large_product = row_ad_detail['대업종 분류']
    middle_product = row_ad_detail['중업종 분류']
    small_product = row_ad_detail['소업종 분류']

    for row_num_ad_keyword, row_ad_keyword in dataframe_ad_keyword[idx:].iterrows():


        if row_ad_detail['광고소재명'] == row_ad_keyword['광고소재명']:
            keywords = [word.strip("' ").strip()
                        for word in row_ad_keyword['키워드'].split(',')]
            
            product_ids = keyword_product[large_product][middle_product][small_product]

            for product_id in product_ids:
                
                if product_id in data:
                    for keyword in keywords:
                        if keyword in data[product_id]:
                            data[product_id][keyword] += 1
                        else:
                            data[product_id][keyword] = 1
                else:
                    data[product_id]  = {}
                    for keyword in keywords:
                        data[product_id][keyword] = 1
                            
            idx += 1
            break


sql_data = {
    'productSmall_id': [],
    'name': [],
    'total': [],
}
index =0
for key, value in data.items():
    for k, v in value.items():
        index += 1
        sql_data['productSmall_id'].append(key)
        sql_data['name'].append(k)
        sql_data['total'].append(v)
print('index : ',index)
print('idx : ',idx)
print('pi : ',pi)
# INSERT 쿼리 작성
insert_query= "INSERT INTO adKeyword (name, total, productSmall_id) VALUES (%s, %s, %s)"
for i in range(index):
    data_to_insert = (sql_data['name'][i],sql_data['total'][i],sql_data['productSmall_id'][i])
    cursor.execute(insert_query, data_to_insert)


# 변경사항을 커밋
connection.commit()

# 커서 닫기
cursor.close()

# 연결 닫기
connection.close()
