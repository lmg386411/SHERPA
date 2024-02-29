package com.ssafy.adrec.myPage.request;

import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
public class MyPageModifyPutReq {

    String name;
    String email;
    String pwd;

    @Builder
    public MyPageModifyPutReq(String name, String email, String pwd) {
        this.name = name;
        this.email = email;
        this.pwd = pwd;
    }
}
