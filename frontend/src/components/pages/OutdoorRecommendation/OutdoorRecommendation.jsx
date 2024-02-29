import React, { useEffect, useState, useLayoutEffect } from 'react';
import { useSelector } from 'react-redux';
import axios from 'axios';
import RecommendTarget from '../../organisms/RecommendTarget';
import OfflineMediaRecommendation from '../../organisms/OfflineMediaRecommendation';
import ChannelRecommendation from '../../organisms/ChannelRecommendation';
import ProducerRecommendation from '../../organisms/ProducerCardList';
import { Container, TargetBox, Box, Hr, ProducerTitleItem, ButtonBox } from './OutdoorRecommendation';
import Button from '../../atoms/Button';
import { useNavigate } from 'react-router-dom';

const APPLICATION_FAST_SERVER_URL =
  process.env.NODE_ENV === 'production' ? 'https://j9c107.p.ssafy.io' : 'http://j9c107.p.ssafy.io:8000';

const APPLICATION_SPRING_SERVER_URL =
  process.env.NODE_ENV === 'production' ? 'https://j9c107.p.ssafy.io' : 'http://j9c107.p.ssafy.io:8080';

export const OutdoorRecommendation = () => {
  const navigate = useNavigate();
  const name = useSelector((state) => state.user.name);
  const { kakao } = window;
  const ageDatas = useSelector((state) => state.result.target.age);
  const [ages, setAges] = useState([]);
  useLayoutEffect(() => {
    const newAges = [];
    for (let i = 0; i < ageDatas.length; i++) {
      if (ageDatas[i]) {
        newAges.push(ageDatas[i].value);
      } else {
        newAges.push(0);
      }
    }
    setAges(newAges);
  }, [ageDatas]);
  const male = useSelector((state) => state.result.target.gender[1].value);
  const female = useSelector((state) => state.result.target.gender[0].value);
  const gender = useSelector((state) => state.result.target.recommend.gender);
  const age = useSelector((state) => state.result.target.recommend.age);
  const mediaList = useSelector((state) => state.result.media.totalList);
  const [mediaLabels, setMediaLabels] = useState([]);
  const [mainDatas, setMainDatas] = useState([]);
  useLayoutEffect(() => {
    const mediaLabels = [];
    const mainDatas = [];
    for (let i = 0; i < mediaList.length; i++) {
      if (mediaList[i]) {
        mediaLabels.push(mediaList[i].name);
        mainDatas.push(mediaList[i].value);
      } else {
        mediaLabels.push(0);
        mainDatas.push(0);
      }
    }
    setMediaLabels(mediaLabels);
    setMainDatas(mainDatas);
  }, [mediaList]);
  const recommendedMedia = useSelector((state) => state.result.media.recommend);
  const bigRegion = useSelector((state) => state.result.bigRegionName);
  const smallRegion = useSelector((state) => state.result.smallRegionName);
  let target = '성별';
  if (gender === true) {
    target = '남성';
  } else {
    target = '여성';
  }
  const [subMediaLabels, setSubMediaLabels] = useState([]);
  const [subDatas, setSubDatas] = useState([]);
  const [priceLabels, setPriceLabels] = useState([]);
  const [prices, setPrices] = useState([]);
  const [producerCardDatas, setProducerCardDatas] = useState({});
  const [producerCardDatas2, setProducerCardDatas2] = useState({});
  const [producerCardDatas3, setProducerCardDatas3] = useState({});
  const [showProducer, setShowProducer] = useState(false);
  const [recommendedRegion, setRecommendedRegion] = useState('');
  const [regionLabels, setRegionLabels] = useState([]);
  const [regionDatas, setRegionDatas] = useState([]);
  const [busLabels, setBusLabels] = useState([]);
  const [busDatas, setBusDatas] = useState([]);
  const [subwayLabels, setSubwayLabels] = useState([]);
  const [subwayDatas, setSubwayDatas] = useState([]);
  const [addresses, setAddresses] = useState([]);
  const item = useSelector((state) => state.user.productSmall);
  const sigunguId = useSelector((state) => state.result.selectedSmallRegion);
  const selectedPrice = useSelector((state) => state.result.selectedPrice);

  useLayoutEffect(() => {
    console.log(`NODE_ENV = ${process.env.NODE_ENV}`);
    console.log(APPLICATION_FAST_SERVER_URL);
    const recommendMedia = async () => {
      try {
        console.log('서브 추천 api item', item);
        console.log('서브 추천 api sigunguId', sigunguId);
        console.log('서브 추천 api gender', gender);
        console.log('서브 추천 api age', age);
        const response = await axios.post(`${APPLICATION_FAST_SERVER_URL}/fastapi/offline/product`, {
          productSmallId: item,
          sigunguId: sigunguId,
          gender: gender,
          age: age
        });
        console.log('서브 추천 매체 가져오기', response);
        const subMediaLabels = [];
        for (let i = 0; i < response.data.data.mediaList.length; i++) {
          if (response.data.data.mediaList[i]) {
            subMediaLabels.push(response.data.data.mediaList[i].name);
          } else {
            subMediaLabels.push(0);
          }
          setSubMediaLabels(subMediaLabels);
        }
        const subDatas = [];
        for (let i = 0; i < response.data.data.mediaList.length; i++) {
          if (response.data.data.mediaList[i]) {
            subDatas.push(response.data.data.mediaList[i].value);
          } else {
            subDatas.push(0);
          }
          setSubDatas(subDatas);
        }
      } catch (error) {
        console.error('서브 추천 매체 가져오기 오류:', error);
      }
    };
    const recommendPrice = async () => {
      try {
        const response = await axios.post(`${APPLICATION_FAST_SERVER_URL}/fastapi/offline/budget`, {
          budget: selectedPrice
        });
        console.log('추천 가격 가져오기', response);
        const priceLabels = [];
        for (let i = 0; i < response.data.data.budgetList.length; i++) {
          if (response.data.data.budgetList[i]) {
            priceLabels.push(response.data.data.budgetList[i].name);
          } else {
            priceLabels.push(0);
          }
          setPriceLabels(priceLabels);
        }
        const prices = [];
        for (let i = 0; i < response.data.data.budgetList.length; i++) {
          if (response.data.data.budgetList[i]) {
            prices.push(response.data.data.budgetList[i].value * 0.0001);
          } else {
            prices.push(0);
          }
          setPrices(prices);
        }
      } catch (error) {
        console.error('추천 가격 가져오기 오류:', error);
      }
    };
    const linkproducer = async () => {
      try {
        const response = await axios.get(`${APPLICATION_SPRING_SERVER_URL}/api/media/company/6?mediaSubId=1`);
        console.log('제작사', response);
        setProducerCardDatas(response.data.data);
      } catch (error) {
        console.log('제작사 오류', error);
      }
    };
    const linkproducer2 = async () => {
      try {
        const response = await axios.get(`${APPLICATION_SPRING_SERVER_URL}/api/media/company/6?mediaSubId=2`);
        console.log('제작사', response);
        setProducerCardDatas2(response.data.data);
      } catch (error) {
        console.log('제작사 오류', error);
      }
    };
    const linkproducer3 = async () => {
      try {
        const response = await axios.get(`${APPLICATION_SPRING_SERVER_URL}/api/media/company/6?mediaSubId=3`);
        console.log('제작사', response);
        setProducerCardDatas3(response.data.data);
      } catch (error) {
        console.log('제작사 오류', error);
      }
    };
    const recommendRegion = async () => {
      try {
        const response = await axios.post(`${APPLICATION_SPRING_SERVER_URL}/api/offline/outdoor/area`, {
          listSize: 5,
          gender: Number(gender),
          age: age,
          sigunguId: sigunguId
        });
        console.log('장소 분석 가져오기', response);
        setRecommendedRegion(response.data.data[0].type);
        const regionLabels = [];
        const regionDatas = [];

        for (let i = 0; i < response.data.data.length; i++) {
          if (response.data.data[i]) {
            regionLabels.push(response.data.data[i].type);
            regionDatas.push(response.data.data[i].ratio);
          } else {
            regionLabels.push(0);
            regionDatas.push(0);
          }
        }
        setRegionLabels(regionLabels);
        setRegionDatas(regionDatas);
      } catch (error) {
        console.log('장소 분석 오류', error);
      }
    };
    const recommendBus = async () => {
      try {
        const response = await axios.post(`${APPLICATION_SPRING_SERVER_URL}/api/offline/outdoor/bus`, {
          listSize: 5,
          gender: Number(gender),
          age: age,
          sigunguId: sigunguId
        });
        console.log('버스 가져오기', response);
        const busLabels = [];
        const busDatas = [];

        for (let i = 0; i < response.data.data.length; i++) {
          if (response.data.data[i]) {
            busLabels.push(response.data.data[i].type);
            busDatas.push(response.data.data[i].ratio);
          } else {
            busLabels.push(0);
            busDatas.push(0);
          }
        }
        setBusLabels(busLabels);
        setBusDatas(busDatas);
      } catch (error) {
        console.log('버스 오류', error);
      }
    };
    const recommendSubway = async () => {
      try {
        const response = await axios.get(`${APPLICATION_SPRING_SERVER_URL}/api/offline/outdoor/subway`);
        console.log('지하철 역 가져오기', response);
        const subwayLabels = [];
        const subwayDatas = [];

        for (let i = 0; i < response.data.data.length; i++) {
          if (response.data.data[i]) {
            subwayLabels.push(response.data.data[i].station);
            subwayDatas.push(response.data.data[i].ratio);
          } else {
            subwayLabels.push(0);
            subwayDatas.push(0);
          }
        }
        setSubwayLabels(subwayLabels);
        setSubwayDatas(subwayDatas);
      } catch (error) {
        console.log('지하철 역 오류', error);
      }
    };
    const recommendOutdoor = async () => {
      try {
        const response = await axios.post(`${APPLICATION_SPRING_SERVER_URL}/api/offline/outdoor/banner`, {
          listSize: 5,
          gender: Number(gender),
          age: age,
          sigunguId: sigunguId
        });
        console.log('현수막 가져오기', response);
        const addresses = [];

        for (let i = 0; i < response.data.data.length; i++) {
          if (response.data.data[i]) {
            addresses.push(response.data.data[i].address);
          } else {
            addresses.push(0);
          }
        }
        setAddresses(addresses);
        console.log('주소 리스트', addresses);
      } catch (error) {
        console.log('현수막 오류', error);
      }
    };
    recommendMedia();
    recommendPrice();
    linkproducer();
    linkproducer2();
    linkproducer3();
    recommendRegion();
    recommendBus();
    recommendSubway();
    recommendOutdoor();
  }, []);

  useEffect(() => {
    const container = document.getElementById('myMap');
    const options = {
      center: new kakao.maps.LatLng(35.1595454, 126.8526012),
      level: 3
    };
    const map = new kakao.maps.Map(container, options);

    const geocoder = new kakao.maps.services.Geocoder();

    addresses.forEach((address) => {
      geocoder.addressSearch(address, function (result, status) {
        if (status === kakao.maps.services.Status.OK) {
          const coords = new kakao.maps.LatLng(result[0].y, result[0].x);

          new kakao.maps.Marker({
            map: map,
            position: coords
          });

          map.setCenter(coords);
        }
      });
    });
  }, [addresses]);

  useEffect(() => {
    const delayProducerRender = setTimeout(() => {
      setShowProducer(true);
    }, 2000);
    return () => clearTimeout(delayProducerRender);
  }, []);

  const save = async () => {
    try {
      const response = await axios.post(`${APPLICATION_SPRING_SERVER_URL}/api/mypage/save/mediaRec`, {
        memberName: name,
        productSmallId: item,
        budget: selectedPrice,
        inOnOff: 1,
        sigunguId: sigunguId,
        mediaTypeId: 6
      });
      console.log('저장 성공', response);
    } catch (error) {
      console.log('저장 오류', error);
    }
  };

  return (
    <Container>
      <TargetBox>
        <RecommendTarget datas={ages} target={target} age={age} male={male} female={female}></RecommendTarget>
      </TargetBox>
      <Hr />
      <Box>
        <OfflineMediaRecommendation
          mediaLabels={mediaLabels}
          subMediaLabels={subMediaLabels}
          priceLabels={priceLabels}
          mainDatas={mainDatas}
          subDatas={subDatas}
          prices={prices}
          recommendedMedia={recommendedMedia}
        ></OfflineMediaRecommendation>
      </Box>
      <Hr />
      <Box>
        <ChannelRecommendation
          title={`추천 드리는 지역은 ${recommendedRegion} 입니다.`}
          datas={regionDatas}
          labels={regionLabels}
          description={`${bigRegion} ${smallRegion}에 거주하는 ${target} 통계`}
        ></ChannelRecommendation>
      </Box>
      <Hr />
      <Box>
        <ChannelRecommendation
          title="버스 정류장 옥외 광고"
          datas={busDatas}
          labels={busLabels}
          description={`${recommendedRegion}에 있는 버스 정류장 승하차량 통계`}
        ></ChannelRecommendation>
      </Box>
      <Hr />
      <Box>
        {subwayLabels.length > 0 && (
          <ChannelRecommendation
            title="지하철 역 옥외 광고"
            datas={subwayDatas}
            labels={subwayLabels}
            description={`${bigRegion}에 있는 지하철 역 승하차량 통계`}
          ></ChannelRecommendation>
        )}
      </Box>
      <Hr />
      <Box>
        <ProducerTitleItem>현수막 옥외광고</ProducerTitleItem>
        <div
          id="myMap"
          style={{
            width: '100%',
            height: '600px'
          }}
        ></div>
      </Box>
      <Hr />
      <Box>
        <ProducerTitleItem>버스 정류장 옥외 광고 제작사</ProducerTitleItem>
        {showProducer && <ProducerRecommendation cardDatas={producerCardDatas} />}
      </Box>
      <Box>
        <ProducerTitleItem>지하철 역 옥외 광고 제작사</ProducerTitleItem>
        {showProducer && <ProducerRecommendation cardDatas={producerCardDatas2} />}
        <ProducerTitleItem>현수막 옥외 광고 제작사</ProducerTitleItem>
        {showProducer && <ProducerRecommendation cardDatas={producerCardDatas3} />}
      </Box>
      <ButtonBox>
        <Button
          backgroundColor="#3C486B"
          width="350px"
          height="80px"
          border="1px solid #3C486B"
          textColor="white"
          fontSize="24px"
          onClick={() => {
            save();
            navigate('/mypage');
          }}
        >
          보관함에 추가
        </Button>
        <Button
          backgroundColor="#3C486B"
          width="350px"
          height="80px"
          textColor="white"
          fontSize="24px"
          onClick={() => {
            navigate('/mediaRecommend');
          }}
        >
          다시 추천받기
        </Button>
      </ButtonBox>
    </Container>
  );
};

export default OutdoorRecommendation;
