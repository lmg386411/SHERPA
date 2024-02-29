import React, { useState, useLayoutEffect, useEffect } from "react";
import { useSelector } from "react-redux";
import axios from "axios";
import RecommendTarget from "../../organisms/RecommendTarget";
import CommunityRecommendation from "../../organisms/CommunityRecommendation";
import BlogRecommendation from "../../organisms/ProducerCardList";
import SnsRecomendation from "../../organisms/SnsRecommendation";
import ProducerRecommendation from "../../organisms/ProducerCardList";
import {
  Container,
  TargetBox,
  Box,
  BlogTitle,
  Hr,
  SaveBox,
  ButtonBox,
} from "./OnlineRecommendation";
import { useNavigate } from "react-router-dom";
import Button from "../../atoms/Button";

const APPLICATION_FAST_SERVER_URL =
  process.env.NODE_ENV === "production"
    ? "https://j9c107.p.ssafy.io"
    : "http://j9c107.p.ssafy.io:8000";

const APPLICATION_SPRING_SERVER_URL =
  process.env.NODE_ENV === "production"
    ? "https://j9c107.p.ssafy.io"
    : "http://j9c107.p.ssafy.io:8080";

export const OnlineRecommendation = () => {
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
  const selectedItem = useSelector((state) => state.user.productSmallName);
  const description = `${selectedItem}에 알맞는 블로그 목록`;
  let target = "성별";
  if (gender === true) {
    target = "남성";
  } else {
    target = "여성";
  }
  const [recommendedCommunity, setRecommendedCommunity] = useState("");
  const [firstCommunityLabels, setFirstCommunityLabels] = useState([]);
  const [coummunityfirstDatas, setCoummunityfirstDatas] = useState([]);
  const [coummunitysecondDatas, setCoummunitysecondDatas] = useState([]);
  const [blogCardDatas, setBlogCardDatas] = useState([]);
  const [recommendedSns, setRecommendedSns] = useState("");
  const [snsLabels, setSnsLabels] = useState([]);
  const [snsFirstDatas, setSnsFirstDatas] = useState([]);
  const [snsSecondDatas, setSnsSecondDatas] = useState([]);
  const [producerCardDatas, setProducerCardDatas] = useState({});
  const [producerCardDatas2, setProducerCardDatas2] = useState({});
  const [showProducer, setShowProducer] = useState(false);
  const item = useSelector((state) => state.user.productSmall);
  const sido = useSelector((state) => state.result.selectedBigRegion);
  const sigunguId = useSelector((state) => state.result.selectedSmallRegion);
  const selectedPrice = useSelector((state) => state.result.selectedPrice);
  const onOff = useSelector((state) => state.result.selectedOnOffline);

  useLayoutEffect(() => {
    console.log(`NODE_ENV = ${process.env.NODE_ENV}`);
    console.log(APPLICATION_FAST_SERVER_URL);
    const recommendCommunity = async () => {
      try {
        const response = await axios.post(
          `${APPLICATION_FAST_SERVER_URL}/fastapi/online/community`,
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
        console.log("추천 커뮤니티 가져오기", response);
        setRecommendedCommunity(response.data.data.communityList_2022[0].type);
        const communityLabels = [];
        for (let i = 0; i < response.data.data.communityList_2022.length; i++) {
          if (response.data.data.communityList_2022[i]) {
            communityLabels.push(response.data.data.communityList_2022[i].type);
          } else {
            communityLabels.push(0);
          }
        }
        setFirstCommunityLabels(communityLabels);
        const coummunityfirstDatas = [];
        for (let i = 0; i < response.data.data.communityList_2022.length; i++) {
          if (response.data.data.communityList_2021[i]) {
            coummunityfirstDatas.push(
              response.data.data.communityList_2021[i].ratio
            );
          } else {
            coummunityfirstDatas.push(0);
          }
        }
        setCoummunityfirstDatas(coummunityfirstDatas);
        const coummunitysecondDatas = [];
        for (let i = 0; i < response.data.data.communityList_2022.length; i++) {
          if (response.data.data.communityList_2022[i]) {
            coummunitysecondDatas.push(
              response.data.data.communityList_2022[i].ratio
            );
          } else {
            coummunitysecondDatas.push(0);
          }
        }
        setCoummunitysecondDatas(coummunitysecondDatas);
      } catch (error) {
        console.log("추천 커뮤니티 오류", error);
      }
    };
    const detailCommunity = async () => {
      console.log("세부 커뮤니티 item", item);
      try {
        const response = await axios.post(
          `${APPLICATION_FAST_SERVER_URL}/fastapi/online/community/sub`,
          {
            productSmallId: item,
          }
        );
        console.log("세부 커뮤니티 가져오기", response);
        setBlogCardDatas(response.data.data);
      } catch (error) {
        console.log("세부 커뮤니티 오류", error);
      }
    };
    const recommendSns = async () => {
      try {
        const response = await axios.post(
          `${APPLICATION_FAST_SERVER_URL}/fastapi/online/sns`,
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
        console.log("sns 추천", response);
        setRecommendedSns(response.data.data.snsList_2022[0].type);
        const snsLabels = [];
        for (let i = 0; i < response.data.data.snsList_2022.length; i++) {
          if (response.data.data.snsList_2022[i]) {
            snsLabels.push(response.data.data.snsList_2022[i].type);
          } else {
            snsLabels.push(0);
          }
        }
        setSnsLabels(snsLabels);
        const snsFirstDatas = [];
        for (let i = 0; i < response.data.data.snsList_2021.length; i++) {
          if (response.data.data.snsList_2021[i]) {
            snsFirstDatas.push(response.data.data.snsList_2021[i].ratio);
          } else {
            snsFirstDatas.push(0);
          }
        }
        setSnsFirstDatas(snsFirstDatas);
        const snsSecondDatas = [];
        for (let i = 0; i < response.data.data.snsList_2022.length; i++) {
          if (response.data.data.snsList_2022[i]) {
            snsSecondDatas.push(response.data.data.snsList_2022[i].ratio);
          } else {
            snsSecondDatas.push(0);
          }
        }
        setSnsSecondDatas(snsSecondDatas);
      } catch (error) {
        console.log("sns 추천 오류", error);
      }
    };
    const linkproducer = async () => {
      try {
        const response = await axios.get(
          `${APPLICATION_SPRING_SERVER_URL}/api/media/company/1`
        );
        console.log("제작사", response);
        setProducerCardDatas(response.data.data);
      } catch (error) {
        console.log("제작사 오류", error);
      }
    };
    const linkproducer2 = async () => {
      try {
        const response = await axios.get(
          `${APPLICATION_SPRING_SERVER_URL}/api/media/company/2`
        );
        console.log("제작사", response);
        setProducerCardDatas2(response.data.data);
      } catch (error) {
        console.log("제작사 오류", error);
      }
    };
    recommendCommunity();
    detailCommunity();
    recommendSns();
    linkproducer();
    linkproducer2();
  }, []);

  useEffect(() => {
    const delayProducerRender = setTimeout(() => {
      setShowProducer(true);
    }, 2000);
    return () => clearTimeout(delayProducerRender);
  }, []);

  const save = async () => {
    console.log("저장api name", name);
    console.log("저장api item", item);
    console.log("저장api selectedPrice", selectedPrice);
    console.log("저장api onOff", onOff);
    console.log("저장api sigunguId", sigunguId);
    try {
      const response = await axios.post(
        `${APPLICATION_SPRING_SERVER_URL}/api/mypage/save/mediaRec`,
        {
          memberName: name,
          productSmallId: item,
          budget: selectedPrice,
          inOnOff: 0,
          sigunguId: sigunguId,
          mediaTypeId: 1,
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
        <CommunityRecommendation
          item={recommendedCommunity}
          firstDatas={coummunityfirstDatas}
          secondDatas={coummunitysecondDatas}
          target={target}
          labels={firstCommunityLabels}
        ></CommunityRecommendation>
      </Box>
      <Hr />
      <Box>
        <BlogTitle>추천하는 {recommendedCommunity} 입니다.</BlogTitle>
        <BlogRecommendation
          cardDatas={blogCardDatas}
          description={description}
        ></BlogRecommendation>
      </Box>
      <Hr />
      <Box>
        <SnsRecomendation
          labels={snsLabels}
          item={recommendedSns}
          firstDatas={snsFirstDatas}
          secondDatas={snsSecondDatas}
          target={target}
        ></SnsRecomendation>
      </Box>
      <Hr />
      <Box>
        <BlogTitle>커뮤니티 광고 제작사</BlogTitle>
        {showProducer && (
          <ProducerRecommendation cardDatas={producerCardDatas} />
        )}
        <BlogTitle>SNS 광고 제작사</BlogTitle>
        {showProducer && (
          <ProducerRecommendation cardDatas={producerCardDatas2} />
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
export default OnlineRecommendation;
