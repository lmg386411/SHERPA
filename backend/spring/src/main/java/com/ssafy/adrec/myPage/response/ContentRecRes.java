package com.ssafy.adrec.myPage.response;

import com.ssafy.adrec.content.ContentKeyword;
import lombok.Builder;
import lombok.Getter;

import java.time.LocalDateTime;
import java.util.List;

@Getter
@Builder
public class ContentRecRes {

    Long id;
    LocalDateTime recDate;
    String productSmallId;
    Long mediaTypeId;

    List<ContentKeywordRes> keywordList;

}
