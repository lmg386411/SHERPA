package com.ssafy.adrec.myPage.request;

import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
public class MediaRecReq {
    String memberName;
    Long productSmallId;
    int budget;
    int inOnOff;
    Long sigunguId;
    Long mediaTypeId;


}
