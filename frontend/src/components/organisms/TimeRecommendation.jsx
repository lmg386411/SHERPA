import styled from "styled-components";
import LineChart from "../atoms/LineChart";

const Container = styled.div``;
const Title = styled.div`
  font-size: 48px;
  margin-bottom: 100px;
`;

function makeTimeRecommendation({
  weekdaysDatas,
  weekendsDatas,
  description,
  recommendedtime,
}) {
  const labels = [
    "6시",
    "7시",
    "8시",
    "9시",
    "10시",
    "11시",
    "12시",
    "13시",
    "14시",
    "15시",
    "16시",
    "17시",
    "18시",
    "19시",
    "20시",
    "21시",
    "22시",
    "23시",
    "24시",
    "1시",
    "2시",
    "3시",
    "4시",
    "5시",
  ];
  return (
    <Container>
      <Title>추천하는 광고 시간은 주말 {recommendedtime}시 입니다.</Title>
      <LineChart
        labels={labels}
        weekdaysDatas={weekdaysDatas}
        weekendsDatas={weekendsDatas}
        text={description}
      ></LineChart>
    </Container>
  );
}
export default makeTimeRecommendation;
