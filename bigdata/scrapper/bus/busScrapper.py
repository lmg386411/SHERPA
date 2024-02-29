from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

import time
import csv

# 크롬 드라이버 경로와 서비스 설정
driver_path = "data/chromedriver/chromedriver.exe"
service = Service(driver_path)

# 크롬 옵션 설정 (headless 모드 활성화)
chrome_options = Options()
chrome_options.add_argument("--headless")  # 브라우저 창을 표시하지 않음

# 웹 드라이버 시작
driver = webdriver.Chrome(service=service, options=chrome_options)

# 웹 페이지 열기
driver.get("https://bus.gwangju.go.kr/busmap/stationSearch#")

# 웹 페이지 로딩을 위해 몇 초 기다릴 수 있음 (선택 사항)
wait = WebDriverWait(driver, 3)  # 최대 3초 대기

data = {}


def process_bus_data(i):

    bus_id_xpath = '//*[@id="row' + \
        str(i)+'divStationGrid"]/div[3]'
    bus_id_element = driver.find_element(
        By.XPATH, bus_id_xpath)
    bus_id = bus_id_element.get_attribute("title")

    bus_xpath = '//*[@id="row' + \
        str(i)+'divStationGrid"]/div[4]'
    bus_element = driver.find_element(By.XPATH, bus_xpath)
    bus = bus_element.get_attribute("title")

    bus_key = bus_id+","+bus

    if bus_key in data[gu_element.text][doung_element.text]:
        if (data[gu_element.text][doung_element.text][bus_key] > 4):
            return True
        data[gu_element.text][doung_element.text][bus_key] += 1
    else:
        data[gu_element.text][doung_element.text][bus_key] = 0
    return False


click_delay = 0.05

# 클릭하고자 하는 요소 선택 (예: XPath를 사용한 예제)
xpath = '//*[@id="divTab2"]/a'
# element_to_click = driver.find_element_by_xpath(xpath)
element_to_click = driver.find_element(By.XPATH, xpath)

# 선택한 요소 클릭
element_to_click.click()
time.sleep(click_delay)

gu_select_xpath = '//*[@id="PAREA_ID"]'
driver.find_element(By.XPATH, gu_select_xpath).click()
time.sleep(click_delay)

for idx in range(2, 12):
    print("=====================")
    gu_xpath = '//*[@id="PAREA_ID"]/option['+str(idx)+']'
    gu_element = driver.find_element(By.XPATH, gu_xpath)
    gu_element.click()
    time.sleep(click_delay)
    data[gu_element.text] = {}
    print(gu_element.text)
    print("---------------------")
    doung_select_xpath = '//*[@id="AREA_ID"]'
    doung_select_element = driver.find_element(By.XPATH, doung_select_xpath)

    id = 1

    try:
        while True:
            doung_select_element.click()
            time.sleep(click_delay)

            doung_xpath = '//*[@id="AREA_ID"]/option['+str(id)+']'
            doung_element = driver.find_element(By.XPATH, doung_xpath)
            doung_element.click()
            time.sleep(click_delay)
            data[gu_element.text][doung_element.text] = {}
            print(doung_element.text)
            id += 1
            search_xpath = '//*[@id="divArea"]/ul/li[5]'
            driver.find_element(By.XPATH, search_xpath).click()
            time.sleep(click_delay)
            try:
                for i in range(3):
                    process_bus_data(i)

                scroll_up_xpath = '//*[@id="jqxScrollBtnUpverticalScrollBardivStationGrid"]/div'
                scroll_down_xpath = '//*[@id="jqxScrollBtnDownverticalScrollBardivStationGrid"]/div'
                scroll_up_element = driver.find_element(
                    By.XPATH, scroll_up_xpath)
                scroll_down_element = driver.find_element(
                    By.XPATH, scroll_down_xpath)

                while True:
                    scroll_up_element.click()
                    time.sleep(click_delay)
                    if process_bus_data(0):
                        break

                # 한 칸씩 스크롤
                while True:
                    is_break = False
                    for i in range(2, 4):
                        is_break = process_bus_data(i)
                    if is_break:
                        break
                    scroll_down_element.click()
                    time.sleep(click_delay)

            except Exception as e:
                pass

    except NoSuchElementException:
        pass

csv_data = [
    ["구", "동", "ARS_ID", "정류장"]
]

for gu_key, gu_value in data.items():
    gu = gu_key

    for dong_key, dong_value in gu_value.items():
        dong = dong_key

        for bus_key, bus_value in dong_value.items():

            keywords = [word.strip("' ").strip()
                        for word in bus_key.split(',')]
            list_data = []
            list_data.append(gu)
            list_data.append(dong)
            list_data.append(keywords[0])
            list_data.append(keywords[1])

            csv_data.append(list_data)

# CSV 파일로 저장
csv_filename = "data/bus/버스정류장_주소_데이터.csv"

# newline='' 옵션은 빈 줄을 추가하지 않도록 합니다.
with open(csv_filename, mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    for row in csv_data:
        writer.writerow(row)


# 웹 드라이버 종료
driver.quit()
