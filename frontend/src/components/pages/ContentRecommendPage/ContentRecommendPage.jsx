import React, { useState, useEffect, useLayoutEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import OpenAI from 'openai';

import styled from 'styled-components';
import Select from '../../atoms/SelectOption';
import MediaSelectOption from '../../organisms/MediaSelectOption';
import Button from '../../atoms/Button';
import { Box, Modal, Typography, TextField, Checkbox } from '@mui/material';
import { Chip } from '@mui/material';

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
const Paragraph = styled.p`
  text-align: center;
  font-size: 24px;
`;
const Title = styled.p`
  font-size: 32px;
  margin: 10px 20px 50px 0px;
  font-weight: 700;
`;
const Bunch = styled.div`
  margin: 100px 0px 20px 0px;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  align-content: center;
  justify-content: center;
`;
const Bundle = styled.div`
  margin: 0px 0px 30px 0px;
  width: 60%;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  align-content: center;
  justify-content: space-evenly;
`;
const Clouds = styled.div`
  display: flex;
  justify-content: space-evenly;
  flex-wrap: wrap;
`;
const ModalKeyword = styled.div`
  display: flex;
  justify-content: space-between;
  width : 70%
  border: 1px solid #b5b5b5;

  margin: 10px;

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

const RecKeyword = styled.div`
  margin: 5px 10px 100px 10px;
`;
const style = {
  position: 'absolute',
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  width: 600,
  height: 800,
  bgcolor: 'background.paper',
  border: '1px solid #fff',
  borderRadius: 1,
  p: 4,
  padding: 7
};

export const ContentRecommendPage = () => {
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
  const myName = useSelector((state) => state.user.name);

  // 좋아요한 키워드
  const [myKeywords, setMyKeywords] = useState([]);
  const [open, setOpen] = useState(false);
  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);

  // 키워드
  const [keywords, setKeywords] = useState([]);
  const [inputValue, setInputValue] = useState('');
  const [checkedKeywords, setCheckedKeywords] = useState([]);

  // 매체 리스트
  const [mediaList, setMediaList] = useState([]);
  const [mediaText, setMediaText] = useState([]);
  let [mediaTypeMedium, setMediaTypeMedium] = useState(null);
  let [mediaTypeSub, setMediaTypeSub] = useState(null);
  const [media, setMedia] = useState(null);
  const [category, setCategory] = useState({
    major: selectDataL,
    middle: selectDataM,
    minor: selectDataS
  });

  // Handler for text field change
  const handleInputChange = (event) => {
    setInputValue(event.target.value); // Update inputValue state with the text entered in the TextField
  };

  // Handler for button click
  const handleButtonClick = () => {
    if (inputValue.trim()) {
      // If inputValue is not empty or only whitespaces
      setKeywords([...keywords, inputValue]); // Add the inputValue to the keywords array
      setInputValue(''); // Clear the TextField
      console.log(keywords);
    }
  };

  const [phrase, setPhrase] = useState([]);
  const [scenario, setScenario] = useState([
    {
      title: '',
      content: ''
    }
  ]);

  useEffect(() => {
    function getMediaText() {
      const targetMediaData = mediaList.find((index) => index.id === media);
      const mediaText = targetMediaData ? targetMediaData.medium : null;
      setMediaText(mediaText);
      console.log('매체명', mediaText);
      console.log(mediaList);
      console.log(media);
      console.log(targetMediaData);
    }
    getMediaText();
  }, [media]);

  const saveAdRecommendation = async (scenarioToUse) => {
    if (media <= 5) {
      mediaTypeMedium = media;
      mediaTypeSub = null;
    } else if (media >= 6) {
      mediaTypeMedium = 6;
      mediaTypeSub = media - 5;
    }
    console.log('중분류', mediaTypeMedium);
    console.log('소분류', mediaTypeSub);

    console.log('광고 저장 로직', scenarioToUse);

    const data = {
      memberName: myName,
      productSmallId: selectDataS,
      mediaTypeId: mediaTypeMedium,
      mediaSubId: mediaTypeSub,
      keywordList: keywords,
      contentList: scenarioToUse
    };
    try {
      const response = await axios.post(`${APPLICATION_SPRING_SERVER_URL}/api/content/save`, data, {
        headers: {
          'Content-Type': 'application/json'
        }
      });
      if (response.data.success) {
        console.log(response.data.msg);
      }
    } catch (error) {
      console.log('saveAdRecommendation!!', error.response ? error.response.data : error);
    }
  };

  const getMyKeywords = async () => {
    try {
      const response = await axios.get(`${APPLICATION_SPRING_SERVER_URL}/api/content/keyword/${myName}/${selectDataS}`);
      if (response.data.success) {
        console.log('좋아요한 키워드', response.data.data);
        setMyKeywords(response.data.data);
        handleOpen();
      }
    } catch (error) {
      console.log('getMyKeywords!!', error.response ? error.response.data : error);
    }
  };

  const handleCheckboxChange = (keyword, isChecked) => {
    if (isChecked) {
      setCheckedKeywords((prev) => [...prev, keyword]);
    } else {
      setCheckedKeywords((prev) => prev.filter((k) => k !== keyword));
    }
  };

  const modalButtonClick = () => {
    setKeywords((prev) => [...prev, ...checkedKeywords]);
    setCheckedKeywords([]);
    handleClose();
    console.log(keywords);
  };

  const handleDelete = (keywordToDelete) => () => {
    setKeywords((keywords) => keywords.filter((keyword) => keyword !== keywordToDelete));
  };

  const changePhrase = () => {
    if (['TV', '라디오'].includes(mediaText) === true) {
      return scenario;
    }
    const newScenario = phrase.map((p) => ({
      title: p,
      content: ''
    }));
    console.log(newScenario);
    setScenario(newScenario);
    console.log('phrase를 scenario에 넣었어요', scenario);
    return newScenario;
  };

  async function getRecommend(media, keywords, category, setPhrase, setScenario) {
    const API_KEY = process.env.REACT_APP_API_KEY;
    const openai = new OpenAI({
      apiKey: API_KEY,
      dangerouslyAllowBrowser: true
    });
    // getMediaText();
    console.log(['TV', '라디오'].includes(mediaText));
    console.log(mediaText);
    setPhrase([]);
    setScenario([]);
    try {
      // media가 TV, 라디오인 경우
      if (['TV', '라디오'].includes(mediaText) === true) {
        console.log('시나리오 추천받는 중');
        const scenarioMessage = `나는 ${mediaText} 매체에서 광고하려고 합니다. 주요 키워드는 ${keywords.join(
          ', '
        )}입니다.
        광고의 업종은 ${category.major} > ${category.middle} > ${category.minor}입니다.
        음악의 경우 저작권이 없는 ncm 혹은 클래식을 위주로 해주세요. 
        예산의 경우 고려하지 않고 진행합니다. 
        광고 시나리오에는 반드시 각각 제목을 달고 '제목: 시나리오제목'의 형식으로 해주세요. 
        대사도 추가해서 작성해주세요.
        광고 시나리오 2개를 추천해주세요.`;

        const scenarioResponse = await openai.chat.completions.create({
          model: 'gpt-3.5-turbo',
          messages: [{ role: 'user', content: scenarioMessage }],
          temperature: 0.8,
          max_tokens: 3000,
          top_p: 1,
          frequency_penalty: 0.5,
          presence_penalty: 0.5
        });

        console.log(scenarioResponse.choices[0].message.content);
        // "제목:"이라는 문자열을 기준으로 시나리오들을 분리
        const scenarioStrings = scenarioResponse.choices[0].message.content.split('제목:').slice(1);

        // 각 시나리오 문자열을 처리하여 원하는 객체 형태로 변형
        const scenarios = scenarioStrings.map((s) => {
          const lines = s.trim().split('\n');
          const title = lines[0].replace(/["]/g, '').trim();
          const content = lines.slice(1).join('\n').replace('시나리오:\n', '').trim();
          return { title, content };
        });
        console.log(scenarios);
        setScenario(scenarios);

        // media가 TV, 라디오가 아닌 다른 경우
      } else {
        console.log('문구 추천받는 중');
        const phraseMessage = `나는 ${media} 매체에서 광고하려고 합니다. 주요 키워드는 ${keywords.join(
          ', '
        )}입니다. 광고의 업종은 ${category.major} > ${category.middle} > ${
          category.minor
        }입니다. 광고 문구 5개를 추천해주세요. 광고 문구의 경우 숫자를 통해 시작하지 않고 바로 문장이 시작되고 줄바꿈을 통해서 구분해주었으면해.`;

        const phraseResponse = await openai.chat.completions.create({
          model: 'gpt-3.5-turbo',
          messages: [{ role: 'user', content: phraseMessage }],
          temperature: 0.8,
          max_tokens: 1024,
          top_p: 1,
          frequency_penalty: 0.5,
          presence_penalty: 0.5
        });

        if (phraseResponse.created) {
          console.log(phraseResponse.choices[0].message.content);

          const receiveMessage = phraseResponse.choices[0].message.content;
          const processedPhrase = receiveMessage.split('\n').map((str) => str.replace(/^\d+\.\s*/, ''));
          setPhrase(processedPhrase);
          console.log(phrase);
        }
      }
    } catch (error) {
      console.error('Error getting recommendation:', error);
    }
  }

  // 대분류, 중분류, 소분류 관련 effect들
  useLayoutEffect(() => {
    const getDataL = async () => {
      try {
        const response = await axios.get(`${APPLICATION_SPRING_SERVER_URL}/api/product/L/0`);
        if (response.data.success) {
          console.log(response.data.data);
          setDataL(response.data.data);
        }
      } catch (error) {
        console.log('Error!!', error);
      }
    };
    const getMedia = async () => {
      try {
        const mediumResponse = await axios.get(`${APPLICATION_SPRING_SERVER_URL}/api/media/type/largeMedium/0`);
        const smallResponse = await axios.get(`${APPLICATION_SPRING_SERVER_URL}/api/media/type/small/6`);
        if (mediumResponse.data.success && smallResponse.data.success) {
          console.log(mediumResponse.data);
          console.log(smallResponse.data);
          const mediumMediaList = mediumResponse.data.data
            .map((item) => {
              return { id: item.id, medium: item.medium };
            })
            .slice(0, -1); // 옥외 제거

          // smallResponse에서 "type"을 "medium"으로 이름 변경
          const smallMediaList = smallResponse.data.data.map((item) => {
            return { medium: item.type };
          });

          // 두 리스트 합치기
          const combinedMediaList = [...mediumMediaList, ...smallMediaList];

          // 새로운 ID 부여
          const swappedMediaList = combinedMediaList.map((item, index) => {
            return { id: index + 1, medium: item.medium };
          });

          // console.log('수정된 리스트', swappedMediaList);

          // 수정된 데이터를 상태로 설정합니다.
          setMediaList(swappedMediaList);
        }
      } catch (error) {
        console.log('getTargetError!!', error.response ? error.response.data : error);
      }
    };

    getDataL();
    getMedia();
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

  return (
    <Container>
      <h1>광고 매체를 선택해주세요</h1>
      <Select data={mediaList} onSelect={setMedia} width="700px"></Select>
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
      <Bunch>
        <Title>키워드를 입력해주세요</Title>
        <Button
          backgroundColor="white"
          width="180px"
          height="50px"
          textColor="#3C486B"
          fontSize="16px"
          border="solid 1px"
          onClick={() => {
            getMyKeywords();
          }}
        >
          좋아요한 키워드+
        </Button>
      </Bunch>
      {
        <Modal
          open={open}
          onClose={handleClose}
          aria-labelledby="modal-modal-title"
          aria-describedby="modal-modal-description"
        >
          <Box sx={{ ...style, overflow: 'auto' }}>
            {myKeywords.map((keyword, index) => (
              <ModalKeyword key={index}>
                <Typography fontSize={24} align="left">
                  {keyword}
                </Typography>
                <Checkbox label={index} onChange={(e) => handleCheckboxChange(keyword, e.target.checked)} />
              </ModalKeyword>
            ))}
            <Box display="flex" justifyContent="center" mt={2}>
              <Button
                onClick={modalButtonClick}
                backgroundColor="#3C486B"
                width="250px"
                height="50px"
                textColor="white"
                fontSize="24px"
              >
                추천 키워드에 추가
              </Button>
            </Box>
          </Box>
        </Modal>
      }
      <Bundle>
        <TextField size="middle" value={inputValue} onChange={handleInputChange}></TextField>
        <Button
          backgroundColor="#3C486B"
          width="150px"
          height="50px"
          textColor="white"
          fontSize="24px"
          onClick={handleButtonClick}
        >
          추가
        </Button>
      </Bundle>
      <Bundle>
        <Clouds>
          {keywords.map((index) => {
            return (
              <RecKeyword>
                <Chip label={`#${index}`} onDelete={handleDelete(index)} />
              </RecKeyword>
            );
          })}
        </Clouds>
      </Bundle>
      <Button
        backgroundColor="#3C486B"
        width="400px"
        height="50px"
        textColor="white"
        fontSize="24px"
        onClick={() => {
          getRecommend(media, keywords, category, setPhrase, setScenario);
        }}
      >
        추천 결과 보기
      </Button>
      <div>
        <h2>광고 문구</h2>
        {phrase.map((p, index) => (
          <Typography fontSize={16} key={index}>
            {p}
          </Typography>
        ))}
        <h2>시나리오</h2>
        {scenario.map((item, index) => (
          <div key={index}>
            <Typography fontSize={24}>{item.title}</Typography>
            <Typography fontSize={16}>{item.content}</Typography>
          </div>
        ))}
        ;
      </div>
      <Button
        backgroundColor="#3C486B"
        width="400px"
        height="50px"
        textColor="white"
        fontSize="24px"
        onClick={() => {
          const newScenario = changePhrase();
          console.log(newScenario);
          saveAdRecommendation(newScenario);
          navigate('/mypage');
        }}
      >
        보관함에 추가
      </Button>
    </Container>
  );
};

export default ContentRecommendPage;
