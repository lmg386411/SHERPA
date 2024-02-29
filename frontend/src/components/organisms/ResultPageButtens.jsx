import React from "react";
import styled from "styled-components";
import Button from "../atoms/Button";
import { useNavigate } from "react-router-dom";

const Container = styled.div``;
const SaveBox = styled.div`
  display: flex;
  justify-content: space-evenly;
  margin: 150px 0px 30px 0px;
`;

function MakeButtons() {
  const navigate = useNavigate();
  return (
    <Container>
      <SaveBox>
        <Button
          backgroundColor="white"
          width="350px"
          height="80px"
          border="1px solid #3C486B"
          textColor="#3C486B"
          fontSize="24px"
        >
          보관함에 추가
        </Button>
        <Button
          backgroundColor="white"
          width="350px"
          height="80px"
          border="1px solid #3C486B"
          textColor="#3C486B"
          fontSize="24px"
        >
          PDF로 저장
        </Button>
      </SaveBox>
      <Button
        backgroundColor="#3C486B"
        width="890px"
        height="80px"
        textColor="white"
        fontSize="24px"
        onClick={() => {
          console.log(1);
          navigate("/mediaRecommend");
        }}
      >
        다시 추천받기
      </Button>
    </Container>
  );
}
export default MakeButtons;
