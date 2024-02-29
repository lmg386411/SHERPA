import styled from "styled-components";
import person from "../../assets/img/person.png";
import React from "react";
import { useNavigate } from "react-router-dom";

const Container = styled.div`
  margin-top: 200px;
`;
const TitleBox = styled.div`
  font-size: 64px;
`;
const ContentBox = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
`;
const ImgItem = styled.div`
  margin-top: 100px;
  display: flex;
`;
const TalkBubble = styled.div`
  font-size: 32px;
  position: relative;
  width: 500px;
  height: 200px;
  background: #ebebeb;
  color: #3c486b;
  border-radius: 20px;
  padding: 12px 12.8px;
  margin-bottom: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
  &:after {
    border-top: 60px solid #ebebeb;
    border-left: 0px solid transparent;
    border-right: 30px solid transparent;
    border-bottom: 0px solid transparent;
    content: "";
    position: absolute;
    top: 190px;
    left: 40%;
    border-radius: 20px;
  }
`;
const DescriptionItem = styled.div`
  font-size: 40px;
  margin-top: 50px;
  border: 1px solid #3c486b;
  border-radius: 10px;
  width: 1000px;
  padding: 50px;
`;
const Description = styled.div`
  margin-top: 10px;
`;
const Button = styled.button`
  width: 450px;
  height: 100px;
  font-size: 32px;
  margin-top: 100px;
  background-color: #3c486b;
  color: white;
  border-radius: 10px;
  padding: 0px 10px 0px 10px;
`;

function MakeIntroduceKeywordRecommendation() {
  const navigate = useNavigate();
  return (
    <Container>
      <TitleBox>광고 키워드 추천 받기</TitleBox>
      <ContentBox>
        <ImgItem>
          <img src={person} alt="" width={500} />
          <TalkBubble>광고 문구에는 무엇을 써야하지?</TalkBubble>
        </ImgItem>
        <DescriptionItem>
          <Description>광고 하고싶은 물품이나 서비스에 맞추어</Description>
          <Description>광고에 추가하면 효과적인 키워드를</Description>
          <Description>추천해 드립니다.</Description>
        </DescriptionItem>
      </ContentBox>
      <Button
        onClick={() => {
          navigate("/keywordRecommend");
        }}
      >
        광고 키워드 추천 바로가기
      </Button>
    </Container>
  );
}
export default MakeIntroduceKeywordRecommendation;
