import pymysql
import pandas as pd


# 연결 설정
connection = pymysql.connect(
    host='j9c107.p.ssafy.io',
    user='c107',
    password='c107adrec',
    database='adrec'
)

# 커서 생성
cursor = connection.cursor()

# SQL 쿼리 실행
query = """
        SELECT
            ps.id,
            pl.Large,
            pm.medium,
            ps.small
        FROM
            productLarge pl
        JOIN
            productMedium pm ON pl.id = pm.productLarge_id
        JOIN
            productSmall ps ON pm.id = ps.productMedium_id;"""
cursor.execute(query)

produc_list = []
sql_data = {
    'id': [],
    'large': [],
    'medium': [],
    'small': [],
}
# 결과 가져오기
product_data = cursor.fetchall()
print(product_data)
for row in product_data:
    product = {
        'id':  row[0],
        'large': row[1],
        'medium': row[2],
        'small': row[3],
    }
    sql_data['id'].append(row[0])
    sql_data['large'].append(row[1])
    sql_data['medium'].append(row[2])
    sql_data['small'].append(row[3])

    produc_list.append(product)

print(produc_list)

df = pd.DataFrame(sql_data)
print(df)
df.to_csv('products.csv', index=False, encoding='euc-kr')

# 변경사항을 커밋
connection.commit()

# 커서 닫기
cursor.close()

# 연결 닫기
connection.close()
