import React, { useState, useEffect, useLayoutEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

import styled from 'styled-components';
import { Box, Modal, Typography } from '@mui/material';
import Chip from '@mui/material/Chip';
import MediaSelectOption from '../../organisms/MediaSelectOption';
import WordCloud from '../../atoms/WordCloud';

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
const Clouds = styled.div`
  display: flex;
  justify-content: space-evenly;
  flex-wrap: wrap;
`;
const Bundle = styled.div`
  margin: 0px 0px 0px 0px;
  width: 40%;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  align-content: center;
  justify-content: center;
`;
const RecKeword = styled.div`
  margin: 5px 10px 100px 10px;
`;
const style = {
  position: 'absolute',
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  width: 400,
  height: 400,
  bgcolor: 'background.paper',
  border: '1px solid #fff',
  borderRadius: 1,
  p: 4,
  padding: 7
};

export const KeywordRecommendPage = () => {
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
  const [selectDataSName, setSelectDataSName] = useState(null);
  const userName = useSelector((state) => state.user.name);
  const [keywordList, setKeywordList] = useState([]);

  // 워드 클라우드 변수
  const [adData, setAdData] = useState([]);
  const [trendData, setTrendData] = useState([]);
  const [showWordCloud, setShowWordCloud] = useState(false);
  const [keywordRecId, setKeywordRecId] = useState(0);
  // WordCloud를 보여줄지 결정하는 상태
  const [selectedWord, setSelectedWord] = useState(null);

  const [open, setOpen] = useState(false);
  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);

  const handleWordClick = (word) => {
    setSelectedWord(word);
    setOpen(true);

    const saveKeyword = async () => {
      console.log('키워드', selectedWord);
      console.log('키워드보관함', keywordRecId);
      console.log('유저', userName);
      console.log('소분류ID', selectDataS);
      const data = {
        keyword: selectedWord,
        keywordRecId: keywordRecId,
        memberName: userName,
        productSmallId: selectDataS
      };
      console.log(data);
      console.log(typeof data);
      console.log('키워드', data.keyword);
      console.log(typeof data.keyword);
      console.log('키워드보관함', data.keywordRecId);
      console.log(typeof data.keywordRecId);
      console.log('유저', data.memberName);
      console.log(typeof data.memberName);
      console.log('소분류ID', data.productSmallId);
      console.log(typeof data.productSmallId);
      try {
        const response = await axios.post(`${APPLICATION_SPRING_SERVER_URL}/api/keyword/like`, data, {
          headers: {
            'Content-Type': 'application/json'
          }
        });
        if (response.data.success) {
          console.log(response.data.data);
          setKeywordRecId(response.data.data.keywordRecId);
        }
      } catch (error) {
        console.log('saveKeyword!!', error.response ? error.response.data : error);
      }
    };

    saveKeyword();
  };

  const closeModal = () => {
    setSelectedWord(null);
    setOpen(false);
  };

  useEffect(() => {
    // 0.4초 후에 showWordCloud 상태를 true로 설정합니다.
    const timerId = setTimeout(() => setShowWordCloud(true), 400);

    // 컴포넌트가 언마운트되면 setTimeout을 클리어합니다.
    return () => clearTimeout(timerId);
  }, []);

  // 대분류, 중분류, 소분류 관련 effect들
  useLayoutEffect(() => {
    const getDataL = async () => {
      try {
        const response = await axios.get(`${APPLICATION_SPRING_SERVER_URL}/api/product/L/0`);
        if (response.data.success) {
          console.log('대분류!', response.data.data);
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
        const response = await axios.get(`${APPLICATION_SPRING_SERVER_URL}/api/product/M/${selectedL}`);
        if (response.data.success) {
          console.log('중분류!', response.data.data);
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
        const response = await axios.get(`${APPLICATION_SPRING_SERVER_URL}/api/product/S/${selectedM}`);
        if (response.data.success) {
          console.log('소분류!', response.data.data);
          setDataS(response.data.data);
        }
      } catch (error) {
        console.log('getDataS!!', error.response ? error.response.data : error);
      }
    };

    getDataS();
  }, [selectDataM, defaultSelectM]);

  useEffect(() => {
    const getAdKeyword = async () => {
      try {
        const adResponse = await axios.get(`${APPLICATION_SPRING_SERVER_URL}/api/keyword/ad/${selectDataS}`);
        if (adResponse.data.success) {
          console.log('기존광고 키워드', adResponse.data);

          // API 응답을 워드클라우드 형식으로 변환
          const words = adResponse.data.data;

          // 'total' 값이 큰 순서대로 정렬하고, 상위 N개만 선택
          const topNWords = words.sort((a, b) => b.total - a.total).slice(0, 40);

          const cloudData = {
            labels: topNWords.map((d) => d.name),
            datasets: [
              {
                label: '',
                data: topNWords.map((d) => d.total)
              }
            ]
          };
          setAdData(cloudData);
        }
      } catch (error) {
        console.log('getAdKeyword!!', error.adResponse ? error.adResponse.data : error);
      }
    };
    const getTrendKeyword = async () => {
      try {
        const trendResponse = await axios.get(`${APPLICATION_SPRING_SERVER_URL}/api/keyword/trend`);
        if (trendResponse.data.success) {
          console.log('트렌드 키워드', trendResponse.data);

          // API 응답을 워드클라우드 형식으로 변환
          const words = trendResponse.data.data;

          // 'total' 값이 큰 순서대로 정렬하고, 상위 N개만 선택
          const topNWords = words.sort((a, b) => b.total - a.total).slice(0, 40);

          const cloudData = {
            labels: topNWords.map((d) => d.name),
            datasets: [
              {
                label: '',
                data: topNWords.map((d) => d.total)
              }
            ]
          };

          setTrendData(cloudData);
        }
      } catch (error) {
        console.log('getTrendKeyword!!', error.trendResponse ? error.trendResponse.data : error);
      }
    };

    const getRecKeyword = async () => {
      const data = {
        productSmallId: selectDataS,
        memberName: userName,
        listSize: 10
      };
      try {
        const response = await axios.post(`${APPLICATION_FAST_SERVER_URL}/fastapi/keyword`, data, {
          headers: {
            'Content-Type': 'application/json'
          }
        });
        if (response.data.success) {
          console.log('맞춤형 키워드 추천', response.data);
          setKeywordList(response.data.data.keywordList);
        }
      } catch (error) {
        console.log('getRecKeyword!!', error.trendResponse ? error.trendResponse.data : error);
      }
    };
    console.log('광고 키워드 받아오는 중!!');
    // getAdKeyword와 getTrendKeyword 함수를 동시에 실행하고,
    // 두 함수의 결과를 모두 기다린 후에 getProductText와 getRecKeyword를 실행
    Promise.all([getAdKeyword(), getTrendKeyword()])
      .then(() => {
        getRecKeyword();
      })
      .catch((error) => {
        console.error('Error fetching ad or trend keywords:', error);
      });
  }, [selectDataS]);

  useEffect(() => {
    function getProductText() {
      console.log('소분류 리스트!', dataS);
      const targetMediaData = dataS.find((index) => index.id === selectDataS);
      console.log(targetMediaData);
      const productText = targetMediaData ? targetMediaData.product : null;
      setSelectDataSName(productText);
      console.log('품목명', productText);
    }
    getProductText();
  }, [dataS]);

  useEffect(() => {
    function getProductText() {
      console.log('소분류 리스트!', dataS);
      const targetMediaData = dataS.find((index) => index.id === selectDataS);
      console.log(targetMediaData);
      const productText = targetMediaData ? targetMediaData.product : null;
      setSelectDataSName(productText);
      console.log('품목명', productText);
    }
    getProductText();
  }, [selectDataSName]);

  return (
    <Container>
      <h1>광고 품목을 선택해 주세요</h1>
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
        width="200px"
      ></MediaSelectOption>
      <Clouds>
        <Bundle>
          <h1>광고 키워드</h1>
          {showWordCloud && <WordCloud data={adData} onWordClick={handleWordClick}></WordCloud>}
          {selectedWord && (
            <Modal
              open={open}
              onClose={handleClose}
              aria-labelledby="modal-modal-title"
              aria-describedby="modal-modal-description"
            >
              <Box sx={style} overflow="auto">
                <Typography fontSize={24} align="center">
                  선택하신 "{selectedWord}"이(가)
                </Typography>
                <Chip fontSize={24} label={`#${selectDataSName}`} />
                <Typography fontSize={24} align="center">
                  항목의 "좋아요" 키워드에 추가 되었습니다!
                </Typography>
              </Box>
            </Modal>
          )}
        </Bundle>
        <Bundle>
          <h1>트랜드 키워드</h1>
          {showWordCloud && <WordCloud data={trendData} onWordClick={handleWordClick}></WordCloud>}
          {selectedWord && (
            <Modal
              open={open}
              onClose={handleClose}
              aria-labelledby="modal-modal-title"
              aria-describedby="modal-modal-description"
            >
              <Box sx={style} overflow="auto">
                <Typography fontSize={40} align="center">
                  {selectedWord}이(가)
                  <Chip label={`#${selectDataSName}`} /> 의 "좋아요" 키워드에 추가 되었습니다!
                </Typography>
              </Box>
            </Modal>
          )}
        </Bundle>
      </Clouds>
      <h1>현재 다른 사용자가 선호하는 키워드를 보여드립니다.</h1>
      <Clouds>
        {keywordList.map((index) => {
          return (
            <RecKeword>
              <Chip label={`#${index.keyword}`} />
            </RecKeword>
          );
        })}
      </Clouds>
    </Container>
  );
};
export default KeywordRecommendPage;
