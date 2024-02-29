import React from 'react';
import styled from "styled-components";
import FixedInfo from '../../organisms/FixedInfo';
import user from '../../../assets/img/user.png';
import EditProduct from '../../organisms/EditProduct';
import BasicTabs from '../../organisms/Bucket';

const Container = styled.div`
  margin: 0 320px;
`;

const MyBox = styled.div`
  display: flex;
  justify-content: flex-start;
  margin-top: 100px;
  font-size: 48px;
  font-weight: bold;
`
const InfoBox = styled.div`
    display: flex;
    justify-content: space-between;
    margin-top: 30px;
`

const ImgBox = styled.img`
    width: 201px;
    height: 212px;
    border-radius: 4px;
    margin-top: 20px;
`

const MyBox2 = styled.div`
  display: flex;
  justify-content: flex-start;
  margin-top: 100px;
  margin-bottom: 10px;
  font-size: 48px;
  font-weight: bold;
`

function MyPage() {
  return (
    <Container>
        <MyBox>MyPage</MyBox>
        <InfoBox>
            <ImgBox src={user} alt="유저이미지"></ImgBox>
            <FixedInfo></FixedInfo>
            <EditProduct></EditProduct>
        </InfoBox>
        <MyBox2>보관함</MyBox2>
        <BasicTabs></BasicTabs>
    </Container>
    
    
  );
}

export default MyPage;