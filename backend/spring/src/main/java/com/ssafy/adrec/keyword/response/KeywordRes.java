package com.ssafy.adrec.keyword.response;

import lombok.Getter;

@Getter
public class KeywordRes {

    String name;
    int total;

    public KeywordRes(String name, int total) {
        this.name = name;
        this.total = total;
    }
}
