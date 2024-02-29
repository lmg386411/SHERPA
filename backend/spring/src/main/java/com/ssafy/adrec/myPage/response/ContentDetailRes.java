package com.ssafy.adrec.myPage.response;

import lombok.Builder;
import lombok.Getter;

import java.time.LocalDateTime;
import java.util.List;

@Getter
@Builder
public class ContentDetailRes {

    Long id;
    LocalDateTime recDate;
    String productSmallId;
    Long mediaTypeId;

    List<ContentKeywordRes> keywordList;

    List<ContentLikeRes> contentList;
}
