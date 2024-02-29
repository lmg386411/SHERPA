import styled from "styled-components";
import mount from "../../assets/img/mount.png";

const Container = styled.div`
  margin-top: 100px;
`;
const TitleBox = styled.div`
  font-size: 64px;
`;
const ContentBox = styled.div`
  margin-top: 100px;
  display: flex;
`;
const DescriptionItem = styled.div`
  margin-left: 50px;
`;
const Description = styled.div`
  font-size: 32px;
  margin-top: 30px;
  text-align: start;
`;
const FirstDescription = styled.div`
  font-size: 32px;
  margin-top: 50px;
  text-align: start;
`;

function makeSherpaMean() {
  return (
    <Container>
      <TitleBox>어려웠던 광고 제작,</TitleBox>
      <TitleBox>저희 SHERPA가 도와드려요</TitleBox>
      <ContentBox>
        <img src={mount} alt="" />
        <DescriptionItem>
          <FirstDescription>SHERPA란?</FirstDescription>
          <Description>
            히말라야 산맥에서 등반을 할 때 등산객을 안내하고 보호하는 역할을
            하는 사람을 뜻합니다.
          </Description>
          <Description>
            저희는 셰르파처럼 어려워보이는 광고를 빅데이터와 AI 에 기반하여
            효율적인 광고 추천을 하자는 의미에서 서비스 명을 SHERPA라고
            지었습니디.
          </Description>
        </DescriptionItem>
      </ContentBox>
    </Container>
  );
}
export default makeSherpaMean;
