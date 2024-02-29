import React, { useState } from 'react';
import styled from 'styled-components';
import Chip from '@mui/material/Chip';
import ClearIcon from '@mui/icons-material/Clear';
import { Box, Modal, Typography } from '@mui/material';

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
const ChipBox = styled.div`
  text-align: center;
  margin: 20px;
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

function KeywordCard2() {
  const [open, setOpen] = useState(false);
  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);

  const handleDelete = () => {
    console.info('You clicked the delete icon.');
  };

  return (
    <Container>
      <IconContainer>
        <DateBox>2023년 9월 10일</DateBox>
        <ClearIcon></ClearIcon>
      </IconContainer>
      <TitleBox>
        점보도시락
        <br></br>
        진라면
        <br></br>
        컵누들
        <br></br>
        사리곰탕
      </TitleBox>
      <Chip label="#라면" />
      <UrlBox>
        <UrlItem onClick={handleOpen}>&gt;&gt; 키워드 더 보기</UrlItem>
      </UrlBox>

      <Modal
        open={open}
        onClose={handleClose}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
      >
        <Box sx={style}>
          <Chip label="#라면" />
          <Typography id="modal-modal-title" variant="h5" component="h1" align="center">
            키워드
          </Typography>
          <ChipBox>
            <Chip label="Deletable" variant="outlined" onDelete={handleDelete} />
          </ChipBox>
          <ChipBox>
            <Chip label="길게길게길게" variant="outlined" onDelete={handleDelete} />
          </ChipBox>
          <ChipBox>
            <Chip label="Deletable" variant="outlined" onDelete={handleDelete} />
          </ChipBox>
          <ChipBox>
            <Chip label="Deletable" variant="outlined" onDelete={handleDelete} />
          </ChipBox>
          <ChipBox>
            <Chip label="길게길게길게" variant="outlined" onDelete={handleDelete} />
          </ChipBox>
          <ChipBox>
            <Chip label="Deletable" variant="outlined" onDelete={handleDelete} />
          </ChipBox>
          <ChipBox>
            <Chip label="Deletable" variant="outlined" onDelete={handleDelete} />
          </ChipBox>
          <ChipBox>
            <Chip label="길게길게길게" variant="outlined" onDelete={handleDelete} />
          </ChipBox>
          <ChipBox>
            <Chip label="Deletable" variant="outlined" onDelete={handleDelete} />
          </ChipBox>
        </Box>
      </Modal>
    </Container>
  );
}

export default KeywordCard2;
