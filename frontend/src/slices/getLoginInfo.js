import {
  setToken,
  setIsLogin,
  setIsLoginError,
  setIsValidToken,
  setEmail,
  setName,
  setProductSmall,
  setProductMedium,
  setProductLarge,
  setProductSmallName
} from './userSlice';

import axios from 'axios';



  
// 사용자 로그인 처리 함수
export const userLogin = (user) => async (dispatch) => {
  try {
    const APPLICATION_SERVER_URL = 'https://j9c107.p.ssafy.io';
    const response = await axios
      .post(APPLICATION_SERVER_URL + '/api/member/login', user)
      .then((response) => {
        console.log("로그인여부:",response)
        alert('로그인 성공');
        return response;
      })
      .catch(() => {
        alert('로그인 실패');
      });
    if (response.data.success === true) {
      const accessToken = response.data.accessToken;
      sessionStorage.setItem('accessToken', accessToken);
      dispatch(setToken(accessToken));
      dispatch(setIsLogin(true));
      dispatch(setIsLoginError(false));
      dispatch(setIsValidToken(true));
      dispatch(setName(user.name));
    } else {
      dispatch(setIsLogin(false));
      dispatch(setIsLoginError(true));
      dispatch(setIsValidToken(false));
    }
  } catch (error) {}
};



export const getUserInfo = (name) => async (dispatch) => {
  try {
    const APPLICATION_SERVER_URL = 'https://j9c107.p.ssafy.io';
    const response = await axios.get(APPLICATION_SERVER_URL + `/api/mypage/profile/${name}`);
    dispatch(setEmail(response.data.data.email));
    dispatch(setProductSmall(response.data.data.productSmall.id));
    dispatch(setProductMedium(response.data.data.productSmall.productMedium.id));
    dispatch(setProductLarge(response.data.data.productSmall.productMedium.productLarge.id));
    dispatch(setProductSmallName(response.data.data.productSmall.small));

    return ;
  } catch (error) {
    dispatch(setIsValidToken(false));
    return error;
  }
};
