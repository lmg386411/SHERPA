package com.ssafy.adrec.member.service;

import com.ssafy.adrec.member.Member;
import com.ssafy.adrec.member.request.MemberLoginPostReq;
import com.ssafy.adrec.member.request.MemberSignupPostReq;

public interface MemberService {

    // 회원가입
    Member signup(MemberSignupPostReq memberSignupPostReq);

    // 아이디 중복 확인
    Member checkName(String name);

    // 이메일 중복 확인
    Member checkEmail(String email);

    // 로그인
    Member login(MemberLoginPostReq memberLoginPostReq);

}
