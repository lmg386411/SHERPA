package com.ssafy.adrec.member.service;

import com.ssafy.adrec.member.Member;
import com.ssafy.adrec.member.repository.MemberRepository;
import com.ssafy.adrec.member.request.MemberLoginPostReq;
import com.ssafy.adrec.member.request.MemberSignupPostReq;
import com.ssafy.adrec.product.ProductSmall;
import com.ssafy.adrec.product.repository.ProductSmallRepository;
import lombok.RequiredArgsConstructor;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Service;

import java.util.Optional;

@Service
@RequiredArgsConstructor
public class MemberServiceImpl implements MemberService {

    public static final Logger logger = LoggerFactory.getLogger(MemberServiceImpl.class);

    private final MemberRepository memberRepository;
    private final ProductSmallRepository productSmallRepository;

    // 회원가입
    @Override
    public Member signup(MemberSignupPostReq memberSignupPostReq) {
        ProductSmall memberProductSmall = null;

        if (memberSignupPostReq.getProductSmall_id() != null) {
            Optional<ProductSmall> productSmall = productSmallRepository.findById(memberSignupPostReq.getProductSmall_id());
            if (productSmall.isPresent()) {
                memberProductSmall = productSmall.get();
            }
        }

        Member member = Member.builder()
                .name(memberSignupPostReq.getName())
                .email(memberSignupPostReq.getEmail())
                .pwd(memberSignupPostReq.getPwd())
                .productSmall(memberProductSmall)
                .build();

        Member saved = memberRepository.save(member);

        return saved;
    }

    // 아이디 중복 확인
    @Override
    public Member checkName(String name) {
        Optional<Member> member = memberRepository.findByName(name);

        if (member.isEmpty()) {
            return null;
        }

        return member.get();
    }

    // 이메일 중복 확인
    @Override
    public Member checkEmail(String email) {
        Optional<Member> member = memberRepository.findByEmail(email);

        if (member.isEmpty()) {
            return null;
        }

        return member.get();
    }

    // 로그인
    @Override
    public Member login(MemberLoginPostReq memberLoginPostReq) {
        Optional<Member> member = memberRepository.findByNameAndPwd(memberLoginPostReq.getName(), memberLoginPostReq.getPwd());

        if (member.isEmpty()) {
            return null;
        }

        return member.get();
    }
}
