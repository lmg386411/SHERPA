package com.ssafy.adrec.member.request;

import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
public class MemberSignupPostReq {

    String name;
    String email;
    String pwd;
    Long productSmall_id;

    @Builder
    public MemberSignupPostReq(String name, String email, String pwd, Long productSmall_id) {
        this.name = name;
        this.email = email;
        this.pwd = pwd;
        this.productSmall_id = productSmall_id;
    }
}
