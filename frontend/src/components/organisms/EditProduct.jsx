import React, { useEffect, useLayoutEffect, useState } from "react";
import Select from '../atoms/SelectOption'
import MakeButton from "../atoms/Button";
import styled from "styled-components";
import { useDispatch, useSelector } from "react-redux";
import axios from "axios";
import { getUserInfo } from "../../slices/getLoginInfo";

const APPLICATION_SPRING_SERVER_URL =
  process.env.NODE_ENV === 'production' ? 'https://j9c107.p.ssafy.io' : 'http://j9c107.p.ssafy.io:8080';

const APPLICATION_SERVER_URL = 'https://j9c107.p.ssafy.io';

const Container = styled.div`
  display: flex;
  flex-wrap: wrap;
  align-content: flex-start;
  justify-content: space-between;
  align-items: baseline;
  width: 470px;
  margin-top: 10px;
` 

function EditProduct() {

  const dispatch = useDispatch();

  const [selectDataL, setSelectDataL] = useState(null);
  const [selectDataM, setSelectDataM] = useState(null);
  const [selectDataS, setSelectDataS] = useState(null);
  const [dataL, setDataL] = useState([]);
  const [dataM, setDataM] = useState([]);
  const [dataS, setDataS] = useState([]);
  const defaultSelectL = useSelector((state) => state.user.productLarge);
  const defaultSelectM = useSelector((state) => state.user.productMedium);
  const defaultSelectS = useSelector((state) => state.user.productSmall);

  const name = useSelector((state) => state.user.name);

  
  const modifyProduct = async (e) => {
    e.preventDefault();

      const url = APPLICATION_SERVER_URL + "/api/mypage/product" ;
      const data = {
        name: name,
        productSmall_id: selectDataS,
      };
      try {
        const response = await axios.put(url, data);
        console.log("정보수정여부:", response);
        alert('품목수정에 성공하셨습니다.');
        dispatch(getUserInfo(name));
      } catch (error) {
        console.log(error);
        alert("품목수정에 실패하셨습니다.")
      }
  };


  useLayoutEffect(() => {
    // console.log(defaultSelectL);
    // console.log(defaultSelectM);
    // console.log(defaultSelectS);
    // console.log(APPLICATION_SPRING_SERVER_URL);

    const getDataL = async () => {
      try {
        const response = await axios.get(APPLICATION_SPRING_SERVER_URL + `/api/product/L/0`);
        if (response.data.success) {
          // console.log(response.data);
          setDataL(response.data.data);
        }
      } catch (error) {
        console.log('Error!!', error);
      }
    };

    getDataL();
  }, []);
  useEffect(() => {
    const selectedL = selectDataL !== null ? selectDataL : defaultSelectL;
    const getDataM = async () => {
      try {
        const response = await axios.get(APPLICATION_SPRING_SERVER_URL + `/api/product/M/${selectedL}`);
        if (response.data.success) {
          // console.log(response.data);
          setDataM(response.data.data);
        }
      } catch (error) {
        console.log('Error!!', error);
      }
    };
    getDataM();
  }, [selectDataL, defaultSelectL]);
  useEffect(() => {
    const selectedM = selectDataM !== null ? selectDataM : defaultSelectM;
    const getDataS = async () => {
      try {
        const response = await axios.get(APPLICATION_SPRING_SERVER_URL + `/api/product/S/${selectedM}`);
        if (response.data.success) {
          // console.log(response.data);
          setDataS(response.data.data);
        }
      } catch (error) {
        console.log('Error!!', error);
      }
    };

    getDataS();
  }, [selectDataM, defaultSelectM]);

    return (
      <Container>
        <Select data={dataL || []} onSelect={setSelectDataL} defaultSelect={defaultSelectL} />
        <Select data={dataM} onSelect={setSelectDataM} defaultSelect={defaultSelectM} />
        <Select data={dataS} onSelect={setSelectDataS} defaultSelect={defaultSelectS} />
      <MakeButton 
        width="118px"
        height="40px"
        backgroundColor="#3C486B"
        textColor="white"
        onClick={modifyProduct}
        >
            품목 수정
        </MakeButton>
      </Container>
    );
  }
  
  export default EditProduct;