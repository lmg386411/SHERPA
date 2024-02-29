package com.ssafy.adrec.myPage.response;

import lombok.Builder;
import lombok.Getter;

@Getter
public class KeywordIdKeyword {

    private Long id;
    private String keyword;


    @Builder
    public KeywordIdKeyword(Long id, String keyword) {
        this.id = id;
        this.keyword = keyword;
    }
}
