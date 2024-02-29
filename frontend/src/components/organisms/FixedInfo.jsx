import React, { useEffect, useState } from "react";
import ReadOnly from "../atoms/ReadOnly"
import MakeButton from "../atoms/Button";
import Box from '@mui/material/Box';
import Modal from '@mui/material/Modal';
import user from '../../assets/img/user.png';
import styled from "styled-components";
import ClearIcon from '@mui/icons-material/Clear';
import { useDispatch, useSelector } from "react-redux";
import axios from "axios";
import { getUserInfo } from "../../slices/getLoginInfo";

const ImgBox = styled.img`
    width: 201px;
    height: 212px;
    border-radius: 4px;
    margin-top: 15px;
    margin-bottom: 30px;
`

const ValidContainer = styled.div`
  display: flex; /* Flexbox 레이아웃 사용 */
  align-items: flex-start; /* 아이템을 왼쪽으로 정렬 */
  flex-direction: column;
 `

const ConfirmContainer = styled.div`
  display: flex;
  align-items: flex-end;
`

const IconContainer = styled.div`
  position: absolute;
  top: 20px;
  right: 20px;
`

const style = {
  position: 'absolute',
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  width: 656,
  height: 818,
  bgcolor: 'background.paper',
  border: '1px solid #fff',
  borderRadius: 1,
  p: 4,
};


function FixedInfo() {
  const APPLICATION_SERVER_URL = 'https://j9c107.p.ssafy.io';

  const dispatch = useDispatch();

  const [open, setOpen] = useState(false);
  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);
  const name = useSelector((state) => state.user.name);
  const email2 = useSelector((state) => state.user.email);

  const [pwValue, setPwValue] = useState("");
  const [pw2Value, setPw2Value] = useState("");
  const [email, setEmail] = useState('');

  const [pwConfirm, setpwConfirm] = useState(null);
  const [eConfirm, seteConfirm] = useState(null);

  const [pw2Helper, setPw2Helper] = useState("");
  const [eHelper, setEHelper] = useState("");

  useEffect(() => {
    if (pwValue !== pw2Value && pw2Value !== "") {
      setPw2Helper("비밀번호가 일치하지 않습니다.");
      setpwConfirm(false);
    } else {
      setPw2Helper(" ");
      setpwConfirm(true);
    }
  }, [pwValue, pw2Value]);

  const checkMail = async (e) => {
    e.preventDefault();
    const url = APPLICATION_SERVER_URL + "/api/member/check/email/"+ email;
    try {
      const response = await axios.get(url);
      // console.log("확인 결과 : ", response.data.success);
      // setidConfirm(response.data.success);
      // setIdHelper("사용가능한 닉네임 입니다");
      // console.log(idConfirm);
      // return "성공";
      if (response.data.success) {
        setEHelper('사용가능한 이메일입니다.');
        return seteConfirm(true);
      }
      setEHelper('중복된 이메일입니다.');
      return seteConfirm(false);
    } catch (error) {
      console.error("에러메시지 :", error);
      return "실패";
    }
  }

  const modifyUser = async (e) => {
    e.preventDefault();

    if (pwConfirm&&pwValue&&email&&eConfirm) {
      const url = APPLICATION_SERVER_URL + "/api/mypage/profile" ;
      const data = {
        name: name,
        email: email,
        pwd: pwValue,
      };
      try {
        const response = await axios.put(url, data);
        console.log("정보수정여부:", response);
        alert('정보수정에 성공하셨습니다.');
        dispatch(getUserInfo(name));
      } catch (error) {
        console.log(error);
        alert("정보수정에 실패하셨습니다.")
      }
  };
}


    return (
      <div className="fixedInfo">
       <ReadOnly label="UserName" defaultValue={name}></ReadOnly>
       <ReadOnly label="E-mail" defaultValue={email2}></ReadOnly>
       <MakeButton 
        width="116px"
        height="40px"
        backgroundColor="#3C486B"
        textColor="white"
        onClick={handleOpen}
        >
            정보 수정
        </MakeButton>

        <Modal
        open={open}
        onClose={handleClose}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
      >
        <Box sx={style}>
          <IconContainer>
            <ClearIcon onClick={handleClose}></ClearIcon>
          </IconContainer>
          <form>
            <h1>정보 수정</h1>
            <ImgBox src={user} alt="유저이미지"></ImgBox>
            <ValidContainer>
            <ConfirmContainer>
              <input className="e2Input" type="email" placeholder="이메일" value={email} onChange={(e) => { setEmail(e.target.value);}} required/> 
              <MakeButton backgroundColor="white"
                width="90px"
                height="56px"
                border="1px solid #3C486B"
                textColor="#3C486B"
                fontSize="16px"
                onClick = {checkMail}
              >
                중복 확인
              </MakeButton>
            </ConfirmContainer>
            <p>{eHelper}</p>
          </ValidContainer>
          <ValidContainer>
          <input className="pw2Input" type="password" placeholder="비밀번호" value={pwValue} onChange={(e) => { setPwValue(e.target.value);}} required/>
          <p></p>
        </ValidContainer>
        <ValidContainer>
          <input className="pw2Input" type="password" placeholder="비밀번호 확인" value={pw2Value} onChange={(e) => { setPw2Value(e.target.value); }} required/>
          <p>{pw2Helper}</p>
        </ValidContainer>
        <MakeButton 
          width="106px"
          height="59px"
          backgroundColor="#3C486B"
          textColor="white"
          fontSize="20px"
          onClick={modifyUser}
        >
            수정
        </MakeButton>
          </form>
        </Box>
      </Modal>

      </div>
    );
  }
  
  export default FixedInfo;