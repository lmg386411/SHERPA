import React from "react";
import styled from "styled-components";
import { useNavigate } from "react-router-dom";

const Container = styled.div`
  margin-top: 200px;
`;
const TitleBox = styled.div`
  font-size: 64px;
  margin-bottom: 100px;
`;
const CardGridBox = styled.div`
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-gap: 50px;
  justify-items: center;
  align-items: center;
  margin: 3px;
`;
const CardItem = styled.div`
  border: 1px solid #b5b5b5;
  border-radius: 10px;
  padding: 20px;
  width: 380px;
  height: 380px;
  text-align: left;
  text-align: center;
  transition: border-color 0.3s ease-in-out;

  &:hover {
    border-color: #3c486b;
    animation: border-flash 5s;
  }

  @keyframes border-flash {
    0% {
      border-color: #3c486b;
    }
    50% {
      border-color: transparent;
    }
    100% {
      border-color: #3c486b;
    }
  }
`;
const DescroptionFrame = styled.div`
  margin: 130px 0px 80px 0px;
`;
const Description = styled.div`
  font-size: 32px;
`;
const Button = styled.button`
  width: 180px;
  height: 50px;
  color: white;
  background-color: #3c486b;
  font-size: 32px;
  border-radius: 10px;
  padding-bottom: 15px;
`;

function MakeIntroduceRecommendation() {
  const navigate = useNavigate();
  return (
    <Container>
      <TitleBox>대표 추천 기능</TitleBox>
      <CardGridBox>
        <CardItem>
          <DescroptionFrame>
            <Description>광고 대상 추천받기</Description>
            <Description>& 광고 매체 추천받기</Description>
          </DescroptionFrame>
          <Button
            onClick={() => {
              navigate("/mediaRecommend");
            }}
          >
            바로가기
          </Button>
        </CardItem>
        <CardItem>
          <DescroptionFrame>
            <Description>광고 키워드 추천받기</Description>
            <Description>& 트랜드 키워드 추천</Description>
          </DescroptionFrame>
          <Button
            onClick={() => {
              navigate("/keywordRecommend");
            }}
          >
            바로가기
          </Button>
        </CardItem>
        <CardItem>
          <DescroptionFrame>
            <Description>광고 문구 추천받기</Description>
            <Description>& 광고 콘텐츠 추천받기</Description>
          </DescroptionFrame>
          <Button
            onClick={() => {
              navigate("/contentRecommend");
            }}
          >
            바로가기
          </Button>
        </CardItem>
      </CardGridBox>
    </Container>
  );
}
export default MakeIntroduceRecommendation;
