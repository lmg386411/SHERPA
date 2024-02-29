package com.ssafy.adrec.jwt;

import lombok.Builder;
import lombok.Data;

@Data
public class Token {

    private String access;

    @Builder
    public Token(String access) {
        this.access = access;
    }

}
