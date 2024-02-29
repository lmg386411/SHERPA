import React, { useState } from "react";
import styled from "styled-components";
import Chip from '@mui/material/Chip';
import ClearIcon from '@mui/icons-material/Clear';
import { useDispatch, useSelector } from "react-redux";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { 
  setTarget, 
  setMedia,
  setRecommendedMedia,
  setSelectedPrice,
  setSelectedOnOffline,
  setSelectedBigRegion,
  setSelectedSmallRegion,
  setbigRegionName,
  setsmallRegionName 
} from "../../slices/resultSlice";
import { setProductSmall, setProductSmallName } from "../../slices/userSlice";

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

function MediaCard2({Date, label, isOnOff, budget, sigungu, key2}) {
  const dispatch = useDispatch(); 
  const navigate = useNavigate();

  const [gender, setGender] = useState(null);
  const [age, setAge] = useState(null);

  const name = useSelector((state) => state.user.name);
  const productSmallId = useSelector((state) => state.user.productSmall)
  const selectedSmallRegion = useSelector((state) => state.result.selectedSmallRegion)
  const selectedOnOffline = useSelector((state) => state.result.selectedOnOffline)
  const selectedPrice = useSelector((state) => state.result.selectedPrice)

  const APPLICATION_SERVER_URL = 'https://j9c107.p.ssafy.io';

  const APPLICATION_SPRING_SERVER_URL =
  process.env.NODE_ENV === 'production' ? 'https://j9c107.p.ssafy.io' : 'http://j9c107.p.ssafy.io:8080';

  const APPLICATION_FAST_SERVER_URL =
  process.env.NODE_ENV === 'production' ? 'https://j9c107.p.ssafy.io' : 'http://j9c107.p.ssafy.io:8000';

  const getMediaDetail = async () => {
    try {
      const response = await axios.get(APPLICATION_SERVER_URL + `/api/mypage/mediaRec/${name}/${key2}`);
      // if (response.data.success) {
      //   console.log(response.data);
      // // }
      console.log("데이터",response.data.data)
      dispatch(setSelectedPrice(response.data.data.budget))
      if (response.data.data.isOnOff === 0){
        dispatch(setSelectedOnOffline('online'))}
      else{
        dispatch(setSelectedOnOffline("offline"))}
      dispatch(setSelectedBigRegion(response.data.data.sidoId))
      dispatch(setSelectedSmallRegion(response.data.data.sigunguId))
      dispatch(setbigRegionName(response.data.data.sido))
      dispatch(setsmallRegionName(response.data.data.sigungu))
      dispatch(setProductSmallName(response.data.data.productSmall))
      dispatch(setProductSmall(response.data.data.productSmallId))
      // console.log("데이터 행렬", response.data.data);
    } catch (error) {
      console.log('Error!!', error);
    }
  };

  const getTargetDetail = async () => {
    const data = {
      productSmallId: productSmallId,
      sigunguId: selectedSmallRegion
    };

    console.log('productSmallId', data.productSmallId);
    console.log(typeof data.productSmallId);
    console.log('sigunguId', data.sigunguId);
    console.log(typeof data.sigunguId);
    try {
      const response = await axios.post(`${APPLICATION_SPRING_SERVER_URL}/api/target`, data, {
        headers: {
          'Content-Type': 'application/json'
        }
      });
      if (response.data.success) {
        console.log(response.data.data);
        dispatch(setTarget(response.data.data));
        if (response.data.data.recommend.gender === true) {
          setGender(1);
        } else {
          setGender(0);
        }
        console.log('추천값', response.data.data.recommend);
        console.log(gender);
        setAge(response.data.data.recommend.age);
        console.log(age);
      }
    } catch (error) {
      console.log('getTargetError!!', error.response ? error.response.data : error);
    }
  };

  function getResultDetail() {

    if (gender !== null && age !== null && selectedOnOffline === 'online') {
      navigate('/mediaResult/online');
    } else if (gender !== null && age !== null && selectedOnOffline === 'offline') {
      const getOffline = async () => {
        try {
          const response = await axios.post(`${APPLICATION_FAST_SERVER_URL}/fastapi/offline/total`, {
            productSmallId: productSmallId,
            sigunguId: selectedSmallRegion,
            gender: gender,
            age: age,
            budget: selectedPrice
          });
          if (response.data.success) {
            console.log('getOffline', response.data);
            dispatch(setMedia(response.data.data));

            const recommendMedia = response.data.data.recommend;
            dispatch(setRecommendedMedia(recommendMedia));
            console.log('추천매체', recommendMedia);

            if (recommendMedia === 'TV') {
              navigate('/mediaResult/tv');
            } else if (recommendMedia === '라디오') {
              navigate('/mediaResult/radio');
            } else if (recommendMedia === '인쇄') {
              navigate('/mediaResult/newspaper');
            } else if (recommendMedia === '버스' || recommendMedia === '현수막' || recommendMedia === '지하철') {
              navigate('/mediaResult/outdoor');
            }
          }
        } catch (error) {
          console.log('getOfflineError!!', error);
        }
      };
      getOffline();
    }
  }
  
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
        <UrlItem onClick={() => {
                  getMediaDetail();
                  setTimeout(getTargetDetail, 500);
                  setTimeout(getResultDetail, 1000);
                  }}>>>자세히 보기</UrlItem>
      </UrlBox>
    </Container>
  );
}

export default MediaCard2;
