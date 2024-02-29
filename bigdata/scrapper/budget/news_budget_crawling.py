import fitz  # PyMuPDF
import pandas as pd
import re
import csv
import fitz

def extract_and_filter_prices_from_pdfs(pdf_files):
    # PDF 파일에서 텍스트 추출
    def extract_text_from_pdf(pdf_path):
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
        return text

    # 텍스트에서 광고료에 해당하는 숫자 추출
    def extract_prices_from_text(text):
        # 정규식을 사용하여 숫자 패턴 찾기 (콤마 포함)
        prices = re.findall(r'[\d,]+', text)
        # 숫자로 변환
        prices = [int(price.replace(',', '')) for price in prices if ',' in price and price.replace(',', '').isdigit()]
        return prices

    # PDF 파일에서 가격 추출
    def extract_prices_from_pdf(pdf_path):
        text = extract_text_from_pdf(pdf_path)
        return extract_prices_from_text(text)

    # 가격 리스트 생성 및 필터링
    all_prices = []
    for pdf_file in pdf_files:
        all_prices.extend(extract_prices_from_pdf(pdf_file))
    
    # 백만원 이하는 제거
    filtered_prices = [price for price in all_prices if price > 1000000]
    
    with open("../../dataAnalysis/csv/신문광고단가.csv", "w", newline="", encoding="cp949") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["신문광고단가"])  # Write the header
        for price in filtered_prices:
            writer.writerow([price])

# 파일 리스트에서 모든 가격 추출 및 필터링
pdf_files = ["./budget_data/동아일보_광고_단가표.pdf",
            "./budget_data/매일경제_광고_단가표.pdf",
            "./budget_data/조선일보_광고_단가표.pdf"]
filtered_prices_list = extract_and_filter_prices_from_pdfs(pdf_files)

print("신문광고단가.csv 작성완료 되었습니다." )

