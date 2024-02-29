import React from "react";
import styled from "styled-components";
import logo from "../../assets/img/logo.png";

const Container = styled.div`
  border: 1px solid #b5b5b5;
  border-radius: 5px;
  padding: 10px;
  width: 343px;
  height: 300px;
`;
const ImgBox = styled.div`
  width: 200px;
  height: 200px;
  justify-content: center;
  align-items: center;
  text-align: center;
`;
const TitleBox = styled.div`
  font-size: 24px;
  margin-bottom: 30px;
`;
const UrlBox = styled.div`
  text-align: right;
`;
const UrlItem = styled.a`
  color: #2196f3;
  text-decoration: none;
`;

function makeCard({ img, title, url }) {
  const imageSource = img ? img : logo;
  return (
    <Container>
      <ImgBox>
        <img
          src={imageSource}
          alt="이미지를 준비 중입니다."
          width={310}
          height={170}
        />
      </ImgBox>
      <TitleBox>{title}</TitleBox>
      <UrlBox>
        <UrlItem href={url}>더 알아보기</UrlItem>
      </UrlBox>
    </Container>
  );
}

export default makeCard;
