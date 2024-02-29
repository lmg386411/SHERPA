import csv
import requests
from bs4 import BeautifulSoup

def parse_and_save_to_csv(table):
    
    # CSV 파일 작성
    with open("../../dataAnalysis/csv/TV광고단가.csv", "w", newline="", encoding="cp949") as csvfile:
        writer = csv.writer(csvfile)
        
        # CSV 헤더명
        writer.writerow(["TV광고단가"])
        
        rows = table.find_all("tr")[1:]  # Exclude header row
        for row in rows:
            data = [td.get_text(strip=True) for td in row.find_all("td")]
            
            # Filtering out the cells with only numbers and ","
            data = [cell.replace(",", "") for cell in data if cell.replace(",", "").isdigit()]
            
            # CSV 작성
            for cell in data:
                writer.writerow([cell])
    print("작성완료 되었습니다.")

def get_YTN():
  URL = "https://www.ytn.co.kr/business/tv_ad_2.php"
  response = requests.get(URL)

  # 페이지 내용을 파싱
  soup = BeautifulSoup(response.content, 'html.parser')

  # 지정된 style을 가진 모든 div 태그를 찾음
  div_tags = soup.find_all('div', style="position:relative;padding-bottom:20px")

  # 두 번째 div 태그를 선택
  second_div = div_tags[1]

  # 두 번째 div 바로 아래에 있는 table 태그를 찾음
  table = second_div.find_next('table', class_='table_navy')


  parse_and_save_to_csv(table)

def get_jisangpa():
    # Load the terrestrial rates
    with open("./budget_data/지상파_TV광고_단가.csv", "r", encoding="cp949") as src_file:
        reader = csv.reader(src_file)
        terrestrial_rates = list(reader)[1:]  # Exclude header
        
    # CSV에 지상파 광고 단가 추가
    with open("../../dataAnalysis/csv/TV광고단가.csv", "a", newline="", encoding="cp949") as dest_file:
        writer = csv.writer(dest_file)
        writer.writerows(terrestrial_rates)
    print("지상파 TV 광고 단가가 추가되었습니다.")

get_YTN()
get_jisangpa()