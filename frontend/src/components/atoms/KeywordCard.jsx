import React, { useState } from 'react';
import styled from 'styled-components';
import Chip from '@mui/material/Chip';
import ClearIcon from '@mui/icons-material/Clear';
import { Box, Modal, Typography } from '@mui/material';
import CancelIcon from '@mui/icons-material/Cancel';
import { useSelector } from 'react-redux';
import axios from 'axios';

const Container = styled.div`
  border: 1px solid #b5b5b5;
  border-radius: 5px;
  padding: 20px;
  width: 315px;
  height: 250px;
  text-align: left;
`;
const TitleBox = styled.div`
  font-size: 24px;
  margin-top: 15px;
  margin-bottom: 30px;
  height: 100px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
`;

const DateBox = styled.div`
  color: #3c486b;
`;

const UrlBox = styled.div`
  text-align: right;
`;
const UrlItem = styled.button`
  background-color: white;
  border: 1px solid white;
  color: #3c486b;
  text-decoration: none;
  font-size: 16px;
`;

const IconContainer = styled.div`
  display: flex;
  justify-content: space-between;
`;
const KeyBox = styled.div`
  display: flex;
  align-items: center;
  margin-top: 25px;
  margin-left: 25px;
`;

const style = {
  position: 'absolute',
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  width: 500,
  height: 500,
  bgcolor: 'background.paper',
  border: '1px solid #fff',
  borderRadius: 1,
  p: 4,
  padding: 7
};

function KeywordCard({ Date, label, keywordList, key2 }) {
  const [open, setOpen] = useState(false);
  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);

  const name = useSelector((state) => state.user.name);

  const APPLICATION_SERVER_URL = 'https://j9c107.p.ssafy.io';

  const deleteCard = async (e) => {
    e.preventDefault();
    // console.log(key2)
    const url = APPLICATION_SERVER_URL + '/api/mypage/keyword/rec/' + name + '/' + key2;
    try {
      const response = await axios.delete(url);
      // console.log("확인 결과 : ", response.data.success);
      // setidConfirm(response.data.success);
      // setIdHelper("사용가능한 닉네임 입니다");
      // console.log(idConfirm);
      // return "성공";
      console.log('삭제 성공', response);
      alert('삭제 성공하였습니다.');
    } catch (error) {
      console.error('에러메시지 :', error);
      return '실패';
    }
  };

  const deleteKey = (id) => async (e) => {
    e.preventDefault();
    // console.log(id)
    const url = APPLICATION_SERVER_URL + '/api/mypage/keyword/like/' + name + '/' + id;
    try {
      const response = await axios.delete(url);
      // console.log("확인 결과 : ", response.data.success);
      // setidConfirm(response.data.success);
      // setIdHelper("사용가능한 닉네임 입니다");
      // console.log(idConfirm);
      // return "성공";
      console.log('삭제 성공', response);
      alert('삭제 성공하였습니다.');
    } catch (error) {
      console.error('에러메시지 :', error);
      return '실패';
    }
  };

  return (
    <Container>
      <IconContainer>
        <DateBox>{Date.substring(0, 4) + '년 ' + Date.substring(5, 7) + '월 ' + Date.substring(8, 10) + '일'}</DateBox>
        <ClearIcon onClick={deleteCard}></ClearIcon>
      </IconContainer>
      <TitleBox>
        {keywordList.map(function (a, i) {
          return (
            <React.Fragment key={i}>
              {a.keyword}
              <br></br>
            </React.Fragment>
          );
        })}
      </TitleBox>
      <Chip label={`#${label}`} />
      <UrlBox>
        <UrlItem onClick={handleOpen}>&gt;&gt; 키워드 더보기</UrlItem>
      </UrlBox>

      <Modal
        open={open}
        onClose={handleClose}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
      >
        <Box sx={style} overflow="auto">
          <Chip label={`#${label}`} />
          <Typography fontSize={40} align="center">
            키워드
          </Typography>
          {keywordList.map(function (a, i) {
            return (
              <KeyBox key={i}>
                <Typography fontSize={24}>{a.keyword}</Typography>
                <CancelIcon fontSize="large" color="disabled" onClick={deleteKey(a.id)}></CancelIcon>
              </KeyBox>
            );
          })}
          {/* <KeyBox>
          <Typography fontSize={24}>
            톤업선크림
          </Typography>
          <CancelIcon fontSize="large" color="disabled"></CancelIcon>
          </KeyBox> */}
        </Box>
      </Modal>
    </Container>
  );
}

export default KeywordCard;
