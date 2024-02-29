import pandas as pd

# 데이터를 DataFrame으로 로드
data = pd.read_excel('data/news/신문 데이터.xlsx', skiprows=[1])

prepare = {
    'gender': "여성",
    'age': '20대',
    'area': '대전/세종/충청'
}
# 유저 관심사 가중치 (예: 20대 여성 비율에 가중치 0.6을 부여)
user_weights = {
    "여성": 2.5,
    "20대": 2.0,
    "대전/세종/충청": 1  # 이 가중치는 사용자 관심에 따라 조정 가능
}

# 각 신문사의 점수 계산
scores = {}
for i in range(len(data["신문사"])):
    newspaper = data["신문사"][i]
    score = 0
    for feature, weight in user_weights.items():
        score += data[feature][i] * weight
    scores[newspaper] = score

# 가장 높은 점수를 가진 신문사 추천
recommended_newspaper = max(scores, key=scores.get)

print("여성 20대 공주 지역에서 추천하는 신문사:", recommended_newspaper)
print(scores)
