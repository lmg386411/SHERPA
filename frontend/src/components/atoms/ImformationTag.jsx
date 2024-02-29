import styled from "styled-components";

const Container = styled.div`
  border-radius: 100px;
  padding: 10px;
  background-color: #ebebeb;
  margin-right: 20px;
`;

function makeTag({ content }) {
  return <Container>{content}</Container>;
}

export default makeTag;
