import React, { useState, useEffect, useLayoutEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

import styled from 'styled-components';
import MediaSelectOption from '../../organisms/MediaSelectOption';
import { TextField } from '@mui/material';
import Button from '../../atoms/Button';
import Select from '../../atoms/SelectOption';
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
} from '../../../slices/resultSlice';
import { setProductSmallName, setProductSmall, setProductMedium, setProductLarge } from '../../../slices/userSlice';

const APPLICATION_SPRING_SERVER_URL =
  process.env.NODE_ENV === 'production' ? 'https://j9c107.p.ssafy.io' : 'http://j9c107.p.ssafy.io:8080';

const APPLICATION_FAST_SERVER_URL =
  process.env.NODE_ENV === 'production' ? 'https://j9c107.p.ssafy.io' : 'http://j9c107.p.ssafy.io:8000';

const Container = styled.div`
  margin: 0 320px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
`;
const Box = styled.div`
  margin: 150px 0px 150px 0px;
`;
const Paragraph = styled.p`
  text-align: start;
`;
const RecommendSelect = styled.div`
  display: flex;
  flex-wrap: wrap;
  align-content: space-evenly;
  justify-content: space-between;
`;
const BudgetAdvertisement = styled.div`
  width: 45%;
  display: flex;
  justify-content: flex-start;
  flex-direction: column;
`;
const ChooseKindOfRecommend = styled.div`
  display: flex;
  width: 45%;
  flex-wrap: wrap;
  justify-content: center;
  flex-direction: column;
`;
const Buttons = styled.div`
  display: flex;
  justify-content: space-between;
`;
const Choosesido = styled.div`
  width: 40%;
`;
const Choosedong = styled.div`
  width: 45%;
`;

export const MediaRecommendPage = () => {
  const dispatch = useDispatch();
  const navigate = useNavigate();

  // 분류 관련 변수
  const defaultSelectL = useSelector((state) => state.user.productLarge);
  const defaultSelectM = useSelector((state) => state.user.productMedium);
  const defaultSelectS = useSelector((state) => state.user.productSmall);
  const [selectDataL, setSelectDataL] = useState(defaultSelectL || null);
  const [selectDataM, setSelectDataM] = useState(defaultSelectM || null);
  const [selectDataS, setSelectDataS] = useState(defaultSelectS || null);
  const [dataL, setDataL] = useState([]);
  const [dataM, setDataM] = useState([]);
  const [dataS, setDataS] = useState([]);

  // 시/도 시/군/구 변수
  const [selectDataSido, setSelectDataSido] = useState(null);
  const [selectDataSigungu, setSelectDataSigungu] = useState(null);
  const [dataSido, setDataSido] = useState([]);
  const [dataSigungu, setDataSigungu] = useState([]);

  // 예산 및 온/오프라인
  const [selectedBudget, setSelectedBudget] = useState(0);
  const [selectedButton, setSelectedButton] = useState('online');
  const [gender, setGender] = useState(null);
  const [age, setAge] = useState(null);

  function getNames() {
    const targetSidoData = dataSido.find((data) => data.id === selectDataSido);
    const sidoName = targetSidoData ? targetSidoData.area : null;
    dispatch(setbigRegionName(sidoName));
    console.log('시도명', sidoName);
    const targetSigunguData = dataSigungu.find((data) => data.id === selectDataSigungu);
    const sigunguName = targetSigunguData ? targetSigunguData.area : null;
    dispatch(setsmallRegionName(sigunguName));
    console.log('시군구명', sigunguName);
    const targetProductData = dataS.find((data) => data.id === selectDataS);
    const productName = targetProductData ? targetProductData.product : null;
    dispatch(setProductSmallName(productName));
    console.log('품목명', productName);
  }
  function getResult() {
    getNames();
    dispatch(setSelectedPrice(selectedBudget));
    dispatch(setSelectedOnOffline(selectedButton));
    dispatch(setSelectedBigRegion(selectDataSido));
    dispatch(setSelectedSmallRegion(selectDataSigungu));
    dispatch(setProductSmall(selectDataS));
    dispatch(setProductMedium(selectDataM));
    dispatch(setProductLarge(selectDataL));

    if (gender !== null && age !== null && selectedButton === 'online') {
      navigate('/mediaResult/online');
    } else if (gender !== null && age !== null && selectedButton === 'offline') {
      const getOffline = async () => {
        console.log('정찬이형 파트 request selectDataS', selectDataS);
        console.log('정찬이형 파트 request selectDataSigungu', selectDataSigungu);
        console.log('정찬이형 파트 request gender', gender);
        console.log('정찬이형 파트 request age', age);
        console.log('정찬이형 파트 request selectedBudget', selectedBudget);
        try {
          const response = await axios.post(`${APPLICATION_FAST_SERVER_URL}/fastapi/offline/total`, {
            productSmallId: selectDataS,
            sigunguId: selectDataSigungu,
            gender: gender,
            age: age,
            budget: selectedBudget
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

  // 대분류, 중분류, 소분류 관련 effect들
  useLayoutEffect(() => {
    const getDataL = async () => {
      try {
        const response = await axios.get(APPLICATION_SPRING_SERVER_URL + `/api/product/L/0`);
        if (response.data.success) {
          console.log(response.data.data);
          setDataL(response.data.data);
        }
      } catch (error) {
        console.log('Error!!', error);
      }
    };

    getDataL();
  }, []);
  useEffect(() => {
    const selectedL = selectDataL !== null ? selectDataL : defaultSelectL;
    const getDataM = async () => {
      try {
        const response = await axios.get(APPLICATION_SPRING_SERVER_URL + `/api/product/M/${selectedL}`);
        if (response.data.success) {
          console.log(response.data.data);
          setDataM(response.data.data);
        }
      } catch (error) {
        console.log('Error!!', error);
      }
    };
    getDataM();
  }, [selectDataL, defaultSelectL]);
  useEffect(() => {
    const selectedM = selectDataM !== null ? selectDataM : defaultSelectM;
    const getDataS = async () => {
      try {
        const response = await axios.get(APPLICATION_SPRING_SERVER_URL + `/api/product/S/${selectedM}`);
        if (response.data.success) {
          console.log(response.data.data);
          setDataS(response.data.data);
        }
      } catch (error) {
        console.log('Error!!', error);
      }
    };

    getDataS();
  }, [selectDataM, defaultSelectM]);

  //  시/도, 시/군/구 effect
  useLayoutEffect(() => {
    const getSido = async () => {
      try {
        const response = await axios.get(`${APPLICATION_SPRING_SERVER_URL}/api/area/sido/0`);
        if (response.data.success) {
          // console.log(response.data.data);
          setDataSido(response.data.data);
        }
      } catch (error) {
        console.error('Error fetching initial data:', error);
      }
    };

    getSido();
  }, []);
  useEffect(() => {
    const getSigungu = async () => {
      try {
        const response = await axios.get(`${APPLICATION_SPRING_SERVER_URL}/api/area/sigungu/${selectDataSido}`);
        if (response.data.success) {
          console.log(response.data);
          setDataSigungu(response.data.data);
        }
      } catch (error) {
        console.log('Error!!', error);
      }
    };

    getSigungu();
  }, [selectDataSido]);

  // 광고 타겟층 분석 effect
  useEffect(() => {
    const getTarget = async () => {
      const data = {
        productSmallId: selectDataS,
        sigunguId: selectDataSigungu
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

    getTarget();
  }, [selectDataS, selectDataSigungu]);
  return (
    <Container>
      <h1>매체 추천</h1>
      <h3>광고품목에 적합한 매체를 추천해드립니다.</h3>
      <h3>품목</h3>
      <MediaSelectOption
        dataL={dataL}
        dataM={dataM}
        dataS={dataS}
        onSelectL={setSelectDataL}
        onSelectM={setSelectDataM}
        onSelectS={setSelectDataS}
        defaultSelectL={defaultSelectL}
        defaultSelectM={defaultSelectM}
        defaultSelectS={defaultSelectS}
      ></MediaSelectOption>
      <RecommendSelect>
        <BudgetAdvertisement>
          <Paragraph>내가 생각하는 광고 최대 예산</Paragraph>
          <TextField onChange={(e) => setSelectedBudget(Number(e.target.value))}></TextField>
        </BudgetAdvertisement>
        <ChooseKindOfRecommend>
          <Paragraph>온/오프라인</Paragraph>
          <Buttons>
            <Button
              onClick={() => setSelectedButton('online')}
              backgroundColor={selectedButton === 'online' ? '#3C486B' : 'white'}
              width="200px"
              height="50px"
              textColor={selectedButton === 'online' ? 'white' : '#3C486B'}
              fontSize="24px"
              border={selectedButton !== 'online' ? 'solid 1px' : 'none'}
            >
              온라인
            </Button>
            <Button
              onClick={() => setSelectedButton('offline')}
              backgroundColor={selectedButton === 'offline' ? '#3C486B' : 'white'}
              width="200px"
              height="50px"
              textColor={selectedButton === 'offline' ? 'white' : '#3C486B'}
              fontSize="24px"
              border={selectedButton !== 'offline' ? 'solid 1px' : 'none'}
            >
              오프라인
            </Button>
          </Buttons>
        </ChooseKindOfRecommend>
        <Choosesido>
          <Paragraph>광고 지역 선택</Paragraph>
          <Select data={dataSido} onSelect={setSelectDataSido} width="400px"></Select>
        </Choosesido>
        <Choosedong>
          <Paragraph>광고 상세 지역 선택</Paragraph>
          <Select data={dataSigungu} onSelect={setSelectDataSigungu} width="400px"></Select>
        </Choosedong>
      </RecommendSelect>
      <Box>
        <Button
          backgroundColor="#3C486B"
          width="300px"
          height="50px"
          textColor="white"
          fontSize="24px"
          onClick={(e) => getResult()}
        >
          추천받기
        </Button>
      </Box>
    </Container>
  );
};

export default MediaRecommendPage;
