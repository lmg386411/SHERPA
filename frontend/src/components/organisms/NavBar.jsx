import { Link, useLocation } from "react-router-dom";
import React, { useState } from "react";
import styled, { css } from "styled-components";
import logo from "../../assets/img/logo.png";
import { useDispatch, useSelector } from "react-redux";
import { logoutUser } from "../../slices/userSlice";
import { setToken, setIsLogin } from "../../slices/userSlice";
import { PURGE } from "redux-persist";

const Container = styled.div`
  height: 100px;
  display: flex;
  justify-content: space-between;
  border-bottom: 1px solid #d9d9d9;
`;

const LeftBox = styled.div`
  height: 70px;
`;

const MiddleBox = styled.div`
  display: flex;
  flex-direction: row;
  align-items: center;
`;

const RightBox = styled.div`
  display: flex;
  flex-direction: row;
  align-items: center;
  margin-right: 30px;
`;

const ButtonStyle = css`
  width: 250px;
  height: 90px;
  background-color: white;
  border: 0px;
  font-size: 24px;
  text-decoration: none;
  color: black;
  padding: 10px;
  font-weight: bold;
`;

const MediaItem = styled(Link)`
  ${ButtonStyle}
  ${(props) =>
    props.to === useLocation().pathname && `border-bottom: 5px solid #3C486B;`}
`;

const KeywordItem = styled(Link)`
  ${ButtonStyle}
  ${(props) =>
    props.to === useLocation().pathname && `border-bottom: 5px solid #3C486B;`}
`;

const ContentItem = styled(Link)`
  ${ButtonStyle}
  ${(props) =>
    props.to === useLocation().pathname && `border-bottom: 5px solid #3C486B;`}
`;

const RightItem = styled.button`
  width: 110px;
  background-color: white;
  border: 0px;
  font-size: 16px;
`;
const ButtonFrame = styled.div`
  width: 250px;
`;

function MakeNavBar() {
  const isLogin = useSelector((state) => state.user.isLogin);
  const dispatch = useDispatch();

  const handleLogout = (e) => {
    e.stopPropagation();
    sessionStorage.removeItem("accessToken");
    dispatch(logoutUser());
    dispatch({ type: PURGE, key: "root", result: () => null });
    dispatch(setToken(null));
    dispatch(setIsLogin(false));
  };

  return (
    <Container>
      <Link to="/">
        <LeftBox>
          <img src={logo} alt="" width="100%" height="100%" />
        </LeftBox>
      </Link>
      <MiddleBox>
        <ButtonFrame>
          <MediaItem to="/mediaRecommend">매체 추천</MediaItem>
        </ButtonFrame>
        <ButtonFrame>
          <KeywordItem to="/keywordRecommend">키워드 추천</KeywordItem>
        </ButtonFrame>
        <ButtonFrame>
          <ContentItem to="/contentRecommend">컨텐츠 추천</ContentItem>
        </ButtonFrame>
      </MiddleBox>
      <RightBox>
        {isLogin ? (
          <RightBox>
            <RightItem onClick={handleLogout}>로그아웃</RightItem>
            <Link to="/mypage">
              <RightItem>마이페이지</RightItem>
            </Link>
          </RightBox>
        ) : (
          <RightBox>
            <Link to="/login">
              <RightItem>로그인</RightItem>
            </Link>
            <Link to="/signup">
              <RightItem>회원가입</RightItem>
            </Link>
          </RightBox>
        )}
      </RightBox>
    </Container>
  );
}

export default MakeNavBar;
