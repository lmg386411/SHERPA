package com.ssafy.adrec.keyword.request;

import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
public class KeywordLikeReq {
    String keyword;

    Long KeywordRecId;
    String memberName;
    Long productSmallId;

}
