package com.ssafy.adrec.myPage.response;

import com.ssafy.adrec.keyword.KeywordLike;
import lombok.Builder;
import lombok.Getter;

import java.time.LocalDateTime;
import java.util.List;

@Getter
public class KeywordRecRes {

    Long id;
    LocalDateTime recDate;
    String productSmall;
    List<KeywordIdKeyword> keywordList;

    @Builder
    public KeywordRecRes(Long id,LocalDateTime recDate, String productSmall, List<KeywordIdKeyword> keywordList) {
        this.id = id;
        this.recDate = recDate;
        this.productSmall = productSmall;
        this.keywordList = keywordList;
    }


}


