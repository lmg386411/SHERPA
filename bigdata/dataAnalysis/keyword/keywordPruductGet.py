import pandas as pd

# CSV 파일이 있는 디렉토리 경로
csv_file_ad_detail = 'data/keyword/AiSAC 광고소재명별 광고 정보.csv'

dataframe_ad_detail = pd.read_csv(csv_file_ad_detail, encoding='cp949')

idx = 0
data = {}
for row_num_ad_detail, row_ad_detail in dataframe_ad_detail.iterrows():
    large_product = row_ad_detail['대업종 분류']
    middle_product = row_ad_detail['중업종 분류']
    small_product = row_ad_detail['소업종 분류']
    data_key = large_product + ','+middle_product + ','+small_product
    if data_key in data:
        data[data_key] += 1
    else:
        data[data_key] = 1

sql_data = {
    'large': [],
    'medium': [],
    'small': [],
}

for key, value in data.items():
    product_lst = [word.strip("' ").strip() for word in key.split(',')]
    sql_data['large'].append(product_lst[0])
    sql_data['medium'].append(product_lst[1])
    sql_data['small'].append(product_lst[2])
df = pd.DataFrame(sql_data)
print(df)
df.to_csv('keword_product.csv', index=True, encoding='euc-kr')
