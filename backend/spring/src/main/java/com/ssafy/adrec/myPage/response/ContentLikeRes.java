package com.ssafy.adrec.myPage.response;

import lombok.Builder;
import lombok.Getter;

@Getter
@Builder
public class ContentLikeRes {

    Long id;
    String title;
    String content;

}
