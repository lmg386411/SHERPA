import React from "react";
import styled from "styled-components";
import Chip from '@mui/material/Chip';
import ClearIcon from '@mui/icons-material/Clear';
import { useSelector } from "react-redux";
import axios from "axios";

const Container = styled.div`
  border: 1px solid #b5b5b5;
  border-radius: 5px;
  padding: 20px;
  width: 315px;
  height: 250px;
  text-align: left;
`;
const TitleBox = styled.div`
  font-size: 22px;
  margin-top: 15px;
  margin-bottom: 30px;
  height: 100px;
`;

const DateBox = styled.div`
  color: #3C486B;
  `
const ChipBox = styled.div`

`
const UrlBox = styled.div`
  text-align: right;
`;
const UrlItem = styled.a`
  color: #3C486B;
  text-decoration: none;
`;

const IconContainer = styled.div`
  display: flex;
  justify-content: space-between;
`

function MediaCard({Date, label, isOnOff, budget, sigungu, key2}) {

  const name = useSelector((state) => state.user.name);

  const APPLICATION_SERVER_URL = 'https://j9c107.p.ssafy.io';
  
  const deleteMedCard = async (e) => {
    e.preventDefault();
    // console.log(key2)
    const url = APPLICATION_SERVER_URL +"/api/mypage/mediaRec/" + name +  "/" + key2;
    try {
      const response = await axios.delete(url);
      // console.log("확인 결과 : ", response.data.success);
      // setidConfirm(response.data.success);
      // setIdHelper("사용가능한 닉네임 입니다");
      // console.log(idConfirm);
      // return "성공";
      console.log("삭제 성공", response)
      alert("삭제 성공하였습니다.")
    } catch (error) {
      console.error("에러메시지 :", error);
      return "실패";
    }
  }
  
  return (
    <Container>
      <IconContainer>
      <DateBox>
        {Date.substring(0,4) + "년 " + Date.substring(5,7) + "월 " +Date.substring(8,10) + "일"}
      </DateBox>
      <ClearIcon onClick={deleteMedCard}></ClearIcon>
      </IconContainer>
      <TitleBox>
        {isOnOff === 0? "온라인" : "오프라인"} 매체 추천
        <br></br>
        예산 최대 {budget}원
        <br></br>
        {sigungu}
      </TitleBox>
      <ChipBox>
      <Chip label={`#${label}`} />
      </ChipBox>
      <UrlBox>
        <UrlItem>>>자세히 보기</UrlItem>
      </UrlBox>
    </Container>
  );
}

export default MediaCard;
