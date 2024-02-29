import React, { useEffect, useState } from "react";
import styled from "styled-components";
import ContentCard from "../atoms/ContentCardA";
import ContentCardB from "../atoms/ContentCardB";
import { useSelector } from "react-redux";
import axios from "axios";

const PageContainer = styled.div``;
const CardGridBox = styled.div`
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-gap: 50px;
  justify-items: center;
  align-items: center;
  margin: 3px;
`;

export default function ContentCardListB() {

  const APPLICATION_SERVER_URL = 'https://j9c107.p.ssafy.io';

  const name = useSelector((state) => state.user.name);
  const [contList, setContList] = useState([]);  

  useEffect(() => {
    const getCont = async () => {
      try {
        const response = await axios.get(APPLICATION_SERVER_URL + `/api/mypage/content/${name}`);
        // if (response.data.success) {
        //   console.log(response.data);
        // // }
        // console.log("데이터",response.data.data);
        // console.log("데이터 행렬", response.data.data);
        setContList(response.data.data);
      } catch (error) {
        console.log('Error!!', error);
      }
    };
    getCont();
  }, [contList]);

  console.log("contList",contList)

  return (
    <PageContainer>
      <div className="App">
        <CardGridBox>
          {
            contList.map((a, i) => {
              if (a.mediaTypeId !== 3 && a.mediaTypeId !== 4)
                return <ContentCard
                    date={a.recDate} key={a.id} key2={a.id} label={a.productSmallId} keywordList = {a.keywordList} mediaTypeId={a.mediaTypeId}></ContentCard>     
            })
          }
          {/* <ContentCard></ContentCard>
          <ContentCardB></ContentCardB> */}
        </CardGridBox>
      </div>
    </PageContainer>
  );

}