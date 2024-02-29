import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import { userLogin, getUserInfo } from '../../slices/getLoginInfo';

function SignIn() {
  const [name, setName] = useState('');
  const [pwd, setPwd] = useState('');
  const isLogin = useSelector((state) => state.user.isLogin);
  const token = useSelector((state) => state.user.token);
  const dispatch = useDispatch();
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    const user = { name, pwd };
    if (name&&pwd){
    console.log(1)
    dispatch(userLogin(user))
      .then(() => {
        dispatch(getUserInfo(name));
        navigate('/');
      })
      .catch((error) => {});
    }
  };

  return (
    <div className="form-container sign-in-container">
      <form action="#">
        <h1 className="form-title">로그인</h1>

        <input className="idInput" type="id" placeholder="아이디" value={name} onChange={(e) => { setName(e.target.value);}} required/>
        <br />
        <br />
        <input className="pwInput" type="password" placeholder="비밀번호" value={pwd} onChange={(e) => { setPwd(e.target.value);}} required/>

        <br />
        <div class="pwd">
            <a className="find-password" href="#">비밀번호 찾기</a>
        </div>
        <br />
        <button className="form-button" onClick={handleSubmit}>로그인</button>
        
      </form>
    </div>
  );
}

export default SignIn;
