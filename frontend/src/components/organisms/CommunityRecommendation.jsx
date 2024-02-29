import styled from "styled-components";
import Chart from "../atoms/DoubleChart";

const Container = styled.div``;
const TitleBox = styled.div`
  font-size: 48px;
`;
const ChartBox = styled.div`
  justify-content: center;
  margin-top: 100px;
`;
const Description = styled.div``;

function makeCommunityRecommendation({
  target,
  item,
  firstDatas,
  secondDatas,
  labels,
}) {
  const text = `광주 광역시에 거주하는 ${target}이 이용하는 커뮤니티 통계`;
  return (
    <Container>
      <TitleBox>추천하는 커뮤니티는 {item} 입니다.</TitleBox>
      <ChartBox>
        <Chart
          labels={labels}
          firstDatas={firstDatas}
          secondDatas={secondDatas}
        ></Chart>
        <Description>{text}</Description>
      </ChartBox>
    </Container>
  );
}
export default makeCommunityRecommendation;
