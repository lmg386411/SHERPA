import requests
from bs4 import BeautifulSoup
import re
import csv

# 데이터 크롤링 함수
def crawling_radio():
  URL = "https://www.mpunch.co.kr/101"
  response = requests.get(URL)
  soup = BeautifulSoup(response.content, 'html.parser')

  tds = soup.select('td[style*="background-color: rgb(248, 248, 248);"]')
  return [td.select('div:nth-of-type(2)')[0].text for td in tds if td.select('div:nth-of-type(2)')]

# 가격 정제 함수
def clean_price(price_str):
  return int(re.sub(r'[^0-9]', '', price_str))

# 메인 실행 코드
prices = crawling_radio()
cleaned_prices = [clean_price(price) for price in prices if re.search(r'\d', price)]

with open('../../dataAnalysis/csv/radio광고단가.csv', 'w', newline='', encoding='cp949') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(['radio광고단가'])
  for price in cleaned_prices:
    writer.writerow([price])
print("radio광고단가.csv가 작성되었습니다.")
    

