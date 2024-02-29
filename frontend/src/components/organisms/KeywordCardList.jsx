import React, {useEffect, useState} from "react";
import styled from "styled-components";
import KeywordCard from "../atoms/KeywordCard";
import axios from "axios";
import { useSelector } from 'react-redux';

const PageContainer = styled.div``;
const CardGridBox = styled.div`
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-gap: 50px;
  justify-items: center;
  align-items: center;
  margin: 3px;
`;


function KeywordCardList() {

  const APPLICATION_SERVER_URL = 'https://j9c107.p.ssafy.io';

  const name = useSelector((state) => state.user.name);
  const [keyList, setKeyList] = useState([]);
  
  useEffect(() => {
    const getKeyword = async () => {
      try {
        const response = await axios.get(APPLICATION_SERVER_URL + `/api/mypage/keyword/${name}`);
        // if (response.data.success) {
        //   console.log(response.data);
        // // }
        // console.log("데이터",response);
        // console.log("데이터 행렬", response.data.data);
        setKeyList(response.data.data);
      } catch (error) {
        console.log('Error!!', error);
      }
    };
    getKeyword();
  }, [keyList]);


  return (
    <PageContainer>
      <div className="App">
        <CardGridBox>
          {
            keyList.map(function(a,i){
              return (<KeywordCard
                Date={a.recDate} key={i} key2={a.id} label={a.productSmall}
                keywordList = {a.keywordList}
              ></KeywordCard>)
            })
          }
        </CardGridBox>
      </div>
    </PageContainer>
  );
}

export default KeywordCardList;
