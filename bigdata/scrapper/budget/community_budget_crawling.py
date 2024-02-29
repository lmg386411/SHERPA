import pandas as pd
import numpy as np

# 파일 로드
input_path = "./budget_data/naver_da_pr.xlsx"
data = pd.read_excel(input_path, header=12)

# "기본 공시단가" 컬럼의 데이터에서 문자와 "," 제거
data['기본 공시단가'] = data['기본 공시단가'].astype(str).str.replace('[^0-9]', '', regex=True)

# 빈 문자열 및 100000 이하의 값을 제거
data = data[data['기본 공시단가'] != ""]
data['기본 공시단가'] = data['기본 공시단가'].astype(int)
data = data[data['기본 공시단가'] > 100000]

# 결과 저장
output_path = "../../dataAnalysis/csv/커뮤니티광고단가.csv"
data[['기본 공시단가']].to_csv(output_path, index=False, header=["커뮤니티광고단가"])
