import React, { useEffect, useLayoutEffect, useState } from 'react';
import SelectAutoWidth from '../atoms/SelectOption';
import styled from 'styled-components';
import { TextField } from '@mui/material';
import InputAdornment from '@mui/material/InputAdornment';
import AccountCircle from '@mui/icons-material/AccountCircle';
import Button from '../atoms/Button'
import axios from 'axios';
import { useNavigate } from 'react-router-dom';


const ValidContainer = styled.div`
  display: flex; /* Flexbox 레이아웃 사용 */
  align-items: flex-start; /* 아이템을 왼쪽으로 정렬 */
  flex-direction: column;
 `

const ConfirmContainer = styled.div`
  display: flex;
  align-items: flex-end;
`

function SignUp() {
  const APPLICATION_SERVER_URL = 'https://j9c107.p.ssafy.io';
  const navigate = useNavigate();

  const [name, setName] = useState('');
  const [pwValue, setPwValue] = useState("");
  const [pw2Value, setPw2Value] = useState("");
  const [email, setEmail] = useState('');
  const [productSmall, SetProductSmall] = useState('');

  const [idHelper, setIdHelper] = useState("");
  const [pw2Helper, setPw2Helper] = useState("");
  const [eHelper, setEHelper] = useState("");

  const [idConfirm, setidConfirm] = useState(null);
  const [pwConfirm, setpwConfirm] = useState(null);
  const [eConfirm, seteConfirm] = useState(null);

  const [selectDataL, setSelectDataL] = useState(null);
  const [selectDataM, setSelectDataM] = useState(null);
  const [selectDataS, setSelectDataS] = useState(null);
  const [dataL, setDataL] = useState([]);
  const [dataM, setDataM] = useState([]);
  const [dataS, setDataS] = useState([]);

  useLayoutEffect(() => {
    const getDataL = async () => {
      try {
        const response = await axios.get(APPLICATION_SERVER_URL + `/api/product/L/0`);
        if (response.data.success) {
          console.log(response.data);
          setDataL(response.data.data);
        }
      } catch (error) {
        console.log('Error!!', error);
      }
    };

    getDataL();
  }, []);
  useEffect(() => {
    const getDataM = async () => {
      try {
        const response = await axios.get(APPLICATION_SERVER_URL + `/api/product/M/${selectDataL}`);
        if (response.data.success) {
          console.log(response.data);
          setDataM(response.data.data);
        }
      } catch (error) {
        console.log('Error!!', error);
      }
    };
    getDataM();
  }, [selectDataL]);
  useEffect(() => {
    const getDataS = async () => {
      try {
        const response = await axios.get(APPLICATION_SERVER_URL + `/api/product/S/${selectDataM}`);
        if (response.data.success) {
          console.log(response.data);
          setDataS(response.data.data);
        }
      } catch (error) {
        console.log('Error!!', error);
      }
    };

    getDataS();
  }, [selectDataM]);


  useEffect(() => {
    if (pwValue !== pw2Value && pw2Value !== "") {
      setPw2Helper("비밀번호가 일치하지 않습니다.");
      setpwConfirm(false);
    } else {
      setPw2Helper(" ");
      setpwConfirm(true);
    }
  }, [pwValue, pw2Value]);

 
    const addUser = async (e) => {
      e.preventDefault();

      if (pwConfirm&&pwValue&&name&&email&&idConfirm&&eConfirm) {
        const url = APPLICATION_SERVER_URL + "/api/member" ;
        const data = {
          name: name,
          email: email,
          pwd: pwValue,
          productSmall_id: selectDataS,
        };
        try {
          const response = await axios.post(url, data);
          console.log("가입여부:", response);
          alert('회원가입에 성공하셨습니다.');
          navigate('/')
        } catch (error) {
          console.log(error);
          alert("회원가입에 실패하셨습니다.")
        }
    };
  }

  async function checkName() {
    const url = APPLICATION_SERVER_URL + "/api/member/check/id/"+ name;
    try {
      const response = await axios.get(url);
      // console.log("확인 결과 : ", response.data.success);
      // setidConfirm(response.data.success);
      // setIdHelper("사용가능한 닉네임 입니다");
      // console.log(idConfirm);
      // return "성공";
      if (response.data.success) {
        setIdHelper('사용가능한 아이디입니다.');
        return setidConfirm(true);
      }
      setIdHelper('중복된 아이디입니다.');
      return setidConfirm(false);
    } catch (error) {
      console.error("에러메시지 :", error);
      return "실패";
    }
  }
  // useEffect(() => {
  //   if (!idConfirm && name !== "")
  //     setIdHelper("중복된 닉네임입니다");
  // }, [idConfirm]);


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

  return (
    <div className="form-container sign-up-container">
      <form action="#">
        <h1 className="form-title">회원가입</h1>

        <ValidContainer>
          <ConfirmContainer>
            <input className="idInput2" type="text" placeholder="아이디" value={name} onChange={(e) => { setName(e.target.value);}} required/>
            <Button backgroundColor="white"
              width="99px"
              height="56px"
              border="1px solid #3C486B"
              textColor="#3C486B"
              fontSize="16px"
              onClick={checkName}
            >
              중복 확인
            </Button>
          </ConfirmContainer>
          <p>{idHelper}</p>
        </ValidContainer>
        <ValidContainer>
          <input className="pwInput" type="password" placeholder="비밀번호" value={pwValue} onChange={(e) => { setPwValue(e.target.value);}} required/>
          <p></p>
        </ValidContainer>
        <ValidContainer>
          <input className="pwInput" type="password" placeholder="비밀번호 확인" value={pw2Value} onChange={(e) => { setPw2Value(e.target.value); }} required/>
          <p>{pw2Helper}</p>
        </ValidContainer>
        <ValidContainer>
          <ConfirmContainer>
            <input className="eInput" type="email" placeholder="이메일" value={email} onChange={(e) => { setEmail(e.target.value);}} required/> 
            <Button backgroundColor="white"
              width="99px"
              height="56px"
              border="1px solid #3C486B"
              textColor="#3C486B"
              fontSize="16px"
              onClick={checkMail}
            >
              중복 확인
            </Button>
          </ConfirmContainer>
          <p>{eHelper}</p>
        </ValidContainer>
        <div>
            <SelectAutoWidth data={dataL || []} onSelect={setSelectDataL}></SelectAutoWidth>
            <SelectAutoWidth data={dataM} onSelect={setSelectDataM}></SelectAutoWidth>
            <SelectAutoWidth data={dataS} onSelect={setSelectDataS}></SelectAutoWidth>
        </div>       
        <button className="form-button" onClick={addUser}>회원가입</button>
      </form>
    </div>
  );
}

export default SignUp;