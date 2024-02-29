import React from "react";
import styled from "styled-components";
import CardItem from "../atoms/ProducerCard";

const PageContainer = styled.div``;
const CardGridBox = styled.div`
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-gap: 50px;
  justify-items: center;
  align-items: center;
  margin: 3px;
`;
const TextBox = styled.div`
  font-size: 16px;
  text-align: right;
  margin: 0px 20px 10px 0px;
`;

function makeCardList({ cardDatas, description }) {
  return (
    <PageContainer>
      <div className="App">
        <TextBox>{description}</TextBox>
        <CardGridBox>
          {cardDatas.map((card, index) => (
            <CardItem
              key={index}
              img={card.img}
              title={card.title}
              url={card.url}
            />
          ))}
        </CardGridBox>
      </div>
    </PageContainer>
  );
}

export default makeCardList;
