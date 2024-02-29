package com.ssafy.adrec.keyword.response;

import lombok.Builder;
import lombok.Getter;

import java.time.LocalDateTime;

@Getter
public class KeywordLikeRes {


    String keyword;
    String name;
    String productSmall;
    Long keywordRecId;

    @Builder
    public KeywordLikeRes(String keyword, String name, String productSmall, Long keywordRecId) {
        this.keyword = keyword;
        this.name = name;
        this.productSmall = productSmall;
        this.keywordRecId = keywordRecId;
    }
}
