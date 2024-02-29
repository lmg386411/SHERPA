import React, { useState, useLayoutEffect, useEffect } from "react";
import { useSelector } from "react-redux";
import axios from "axios";
import RecommendTarget from "../../organisms/RecommendTarget";
import OfflineMediaRecommendation from "../../organisms/OfflineMediaRecommendation";
import ChannelRecommendation from "../../organisms/ChannelRecommendation";
import ProducerRecommendation from "../../organisms/ProducerCardList";
import {
  Container,
  TargetBox,
  Box,
  Hr,
  ProducerTitleItem,
  SaveBox,
  ButtonBox,
} from "./NewspaperRecommendation";
import Button from "../../atoms/Button";
import { useNavigate } from "react-router-dom";

const APPLICATION_FAST_SERVER_URL =
  process.env.NODE_ENV === "production"
    ? "https://j9c107.p.ssafy.io"
    : "http://j9c107.p.ssafy.io:8000";

const APPLICATION_SPRING_SERVER_URL =
  process.env.NODE_ENV === "production"
    ? "https://j9c107.p.ssafy.io"
    : "http://j9c107.p.ssafy.io:8080";

export const NewsPaperRecommendation = () => {
  const navigate = useNavigate();
  const name = useSelector((state) => state.user.name);
  const targetCheck = useSelector((state) => state.result.target);
  console.log("전역 target", targetCheck);
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
  const result = useSelector((state) => state.result.media);
  console.log("메인 매체 추천", result);
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
  let target = "성별";
  if (gender === true) {
    target = "남성";
  } else {
    target = "여성";
  }
  const [subMediaLabels, setSubMediaLabels] = useState([]);
  const [subDatas, setSubDatas] = useState([]);
  const [priceLabels, setPriceLabels] = useState([]);
  const [prices, setPrices] = useState([]);
  const [recommendedNewspaper, setRecommendedNewspaper] = useState("");
  const [newspaperLabels, setNewspaperLabels] = useState([]);
  const [newspaperDatas, setNewspaperDatas] = useState([]);
  const [recommendedNewspaperArea, setRecommendedNewspaperArea] = useState("");
  const [newspaperAreaLabels, setNewspaperAreaLabels] = useState([]);
  const [newspaperAreaDatas, setNewspaperAreaDatas] = useState([]);
  const [producerCardDatas, setProducerCardDatas] = useState({});
  const [showProducer, setShowProducer] = useState(false);
  const item = useSelector((state) => state.user.productSmall);
  const sido = useSelector((state) => state.result.selectedBigRegion);
  const sigunguId = useSelector((state) => state.result.selectedSmallRegion);
  const selectedPrice = useSelector((state) => state.result.selectedPrice);

  useLayoutEffect(() => {
    console.log(`NODE_ENV = ${process.env.NODE_ENV}`);
    console.log(APPLICATION_FAST_SERVER_URL);
    const recommendMedia = async () => {
      try {
        const response = await axios.post(
          `${APPLICATION_FAST_SERVER_URL}/fastapi/offline/product`,
          {
            productSmallId: item,
            sigunguId: sigunguId,
            gender: gender,
            age: age,
          }
        );
        console.log("호감도 매체 가져오기", response);
        const subMediaLabels = [];
        const subDatas = [];

        for (let i = 0; i < response.data.data.mediaList.length; i++) {
          if (response.data.data.mediaList[i]) {
            subMediaLabels.push(response.data.data.mediaList[i].name);
            subDatas.push(response.data.data.mediaList[i].value);
          } else {
            subMediaLabels.push(0);
            subDatas.push(0);
          }
        }
        setSubMediaLabels(subMediaLabels);
        setSubDatas(subDatas);
      } catch (error) {
        console.error("추천 매체 가져오기 오류:", error);
      }
    };
    const recommendPrice = async () => {
      try {
        const response = await axios.post(
          `${APPLICATION_FAST_SERVER_URL}/fastapi/offline/budget`,
          {
            budget: selectedPrice,
          }
        );
        console.log("추천 가격 가져오기", response);
        const priceLabels = [];
        const prices = [];

        for (let i = 0; i < response.data.data.budgetList.length; i++) {
          if (response.data.data.budgetList[i]) {
            priceLabels.push(response.data.data.budgetList[i].name);
            prices.push(response.data.data.budgetList[i].value * 0.0001);
          } else {
            priceLabels.push(0);
            prices.push(0);
          }
        }
        setPriceLabels(priceLabels);
        setPrices(prices);
      } catch (error) {
        console.error("추천 가격 가져오기 오류:", error);
      }
    };
    const recommendNewspaper = async () => {
      try {
        const response = await axios.post(
          `${APPLICATION_FAST_SERVER_URL}/fastapi/offline/news/newspaper`,
          {
            gender: {
              0: Number(targetCheck.gender[0].value),
              1: Number(targetCheck.gender[1].value),
            },
            age: {
              10: Number(ageDatas[0].value),
              20: Number(ageDatas[1].value),
              30: Number(ageDatas[2].value),
              40: Number(ageDatas[3].value),
              50: Number(ageDatas[4].value),
              60: Number(ageDatas[5].value),
              70: Number(ageDatas[6].value),
            },
            sidoId: 1,
          }
        );
        console.log(response);
        setRecommendedNewspaper(response.data.data.newsList[0].type);
        const newspaperLabels = [];
        const newspaperDatas = [];

        for (let i = 0; i < response.data.data.newsList.length; i++) {
          if (response.data.data.newsList[i]) {
            newspaperLabels.push(response.data.data.newsList[i].type);
            newspaperDatas.push(response.data.data.newsList[i].ratio);
          } else {
            newspaperLabels.push(0);
            newspaperDatas.push(0);
          }
        }
        setNewspaperLabels(newspaperLabels);
        setNewspaperDatas(newspaperDatas);
      } catch (error) {
        console.error("추천 신문 가져오기 오류:", error);
      }
    };
    const recommendNewspaperField = async () => {
      try {
        const response = await axios.post(
          `${APPLICATION_FAST_SERVER_URL}/fastapi/offline/news/field`,
          {
            gender: {
              0: Number(targetCheck.gender[0].value),
              1: Number(targetCheck.gender[1].value),
            },
            age: {
              10: Number(ageDatas[0].value),
              20: Number(ageDatas[1].value),
              30: Number(ageDatas[2].value),
              40: Number(ageDatas[3].value),
              50: Number(ageDatas[4].value),
              60: Number(ageDatas[5].value),
              70: Number(ageDatas[6].value),
            },
            sidoId: sido,
          }
        );
        console.log(response);
        setRecommendedNewspaperArea(response.data.data.newsThemeList[0].type);
        const newspaperAreaLabels = [];
        const newspaperAreaDatas = [];

        for (let i = 0; i < response.data.data.newsThemeList.length; i++) {
          if (response.data.data.newsThemeList[i]) {
            newspaperAreaLabels.push(response.data.data.newsThemeList[i].type);
            newspaperAreaDatas.push(response.data.data.newsThemeList[i].ratio);
          } else {
            newspaperAreaLabels.push(0);
            newspaperAreaDatas.push(0);
          }
        }
        setNewspaperAreaLabels(newspaperAreaLabels);
        setNewspaperAreaDatas(newspaperAreaDatas);
      } catch (error) {
        console.error("추천 신문 가져오기 오류:", error);
      }
    };
    const linkproducer = async () => {
      try {
        const response = await axios.get(
          `${APPLICATION_SPRING_SERVER_URL}/api/media/company/5`
        );
        console.log("제작사", response);
        setProducerCardDatas(response.data.data);
      } catch (error) {
        console.log("제작사 오류", error);
      }
    };
    recommendMedia();
    recommendPrice();
    recommendNewspaper();
    recommendNewspaperField();
    linkproducer();
  }, []);

  useEffect(() => {
    const delayProducerRender = setTimeout(() => {
      setShowProducer(true);
    }, 2000);
    return () => clearTimeout(delayProducerRender);
  }, []);

  const save = async () => {
    try {
      const response = await axios.post(
        `${APPLICATION_SPRING_SERVER_URL}/api/mypage/save/mediaRec`,
        {
          memberName: name,
          productSmallId: item,
          budget: selectedPrice,
          inOnOff: 1,
          sigunguId: sigunguId,
          mediaTypeId: 5,
        }
      );
      console.log("저장 성공", response);
    } catch (error) {
      console.log("저장 오류", error);
    }
  };

  return (
    <Container>
      <TargetBox>
        <RecommendTarget
          datas={ages}
          target={target}
          age={age}
          male={male}
          female={female}
        ></RecommendTarget>
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
          title={`추천 드리는 신문사는 ${recommendedNewspaper} 입니다.`}
          datas={newspaperDatas}
          labels={newspaperLabels}
          description={`${age}대 ${target}이 이용하는 신문사 통계`}
        ></ChannelRecommendation>
      </Box>
      <Box>
        <ChannelRecommendation
          title={`추천 드리는 신문 분야는 ${recommendedNewspaperArea} 입니다.`}
          datas={newspaperAreaDatas}
          labels={newspaperAreaLabels}
          description={`${age}대 ${target}이 이용하는 신문 분야 통계`}
        ></ChannelRecommendation>
      </Box>
      <Hr />
      <Box>
        <ProducerTitleItem>신문 광고 제작사</ProducerTitleItem>
        {showProducer && (
          <ProducerRecommendation cardDatas={producerCardDatas} />
        )}
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
            navigate("/mypage");
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
            navigate("/mediaRecommend");
          }}
        >
          다시 추천받기
        </Button>
      </ButtonBox>
    </Container>
  );
};

export default NewsPaperRecommendation;
