package com.ssafy.adrec.jwt.service;

import com.ssafy.adrec.jwt.Token;

import java.util.Map;

public interface JwtService {

    // 주입받은 secret 값을 key 변수에 할당
    void afterPropertiesSet();

    // Signature 설정에 들어갈 key 생성
    Token create(String subject);

    // access token 가져옴
    Map<String, Object> get(String key);

    // 전달 받은 토큰이 제대로 생성된 것인지 확인
    boolean checkToken(String jwt);
}
