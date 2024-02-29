import styled from "styled-components";
import DoughnutChart from "../atoms/DoughnutChart";
import BarChart from "../atoms/PriceChart";

const Container = styled.div``;
const MainRecommendationBox = styled.div``;
const TitleItem = styled.div`
  font-size: 48px;
`;
const DescriptionItem = styled.div`
  text-align: right;
  margin: 100px 0px 10px 5px;
`;
const ChartItem = styled.div`
  border: 1px solid #bdbdbd;
  border-radius: 20px;
  display: flex;
  justify-content: center;
`;
const SubChartBox = styled.div`
  display: flex;
  justify-content: space-between;
  margin-top: 100px;
`;
const LeftChartItem = styled.div``;
const RightChartItem = styled.div``;
const LeftChartTitle = styled.div`
  font-size: 48px;
  width: 600px;
  margin-bottom: 50px;
`;
const RightChartTitle = styled.div`
  font-size: 48px;
  width: 600px;
  margin-bottom: 50px;
`;
const Border = styled.div`
  border: 1px solid #bdbdbd;
  border-radius: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 400px;
`;

function makeOfflineMediaRecommendation({
  mainDatas,
  subDatas,
  prices,
  recommendedMedia,
  mediaLabels,
  subMediaLabels,
  priceLabels,
}) {
  const fontSize = "32px";
  return (
    <Container>
      <MainRecommendationBox>
        <TitleItem>추천 매체는 {recommendedMedia} 입니다.</TitleItem>
        <DescriptionItem>
          품목별 광고 기반 결과와 광고 예산 기반을 합친 결과입니다.
        </DescriptionItem>
        <ChartItem>
          <DoughnutChart
            labels={mediaLabels}
            datas={mainDatas}
            width="50%"
            fontSize={fontSize}
          ></DoughnutChart>
        </ChartItem>
      </MainRecommendationBox>
      <SubChartBox>
        <LeftChartItem>
          <LeftChartTitle>품목 별 광고 기반</LeftChartTitle>
          <Border>
            <DoughnutChart
              labels={subMediaLabels}
              datas={subDatas}
              width="80%"
              fontSize={fontSize}
            ></DoughnutChart>
          </Border>
        </LeftChartItem>
        <RightChartItem>
          <RightChartTitle>광고 예산 기반</RightChartTitle>
          <Border>
            <BarChart
              labels={priceLabels}
              datas={prices}
              text="해당 가격은 최소 광고 비용 기준 입니다."
              width="80%"
            ></BarChart>
          </Border>
        </RightChartItem>
      </SubChartBox>
    </Container>
  );
}
export default makeOfflineMediaRecommendation;
