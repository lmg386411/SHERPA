package com.ssafy.adrec.member.request;

import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
public class MemberLoginPostReq {

    String name;
    String pwd;

}
