package com.ssafy.adrec.myPage.response;

import lombok.Builder;
import lombok.Getter;

import java.time.LocalDateTime;

@Getter
@Builder
public class MediaRecRes {
    Long id;
    LocalDateTime recDate;
    int isOnOff;
    int budget;

    Long productSmallId;
    String productSmall;

    Long mediaTypeId;

    String sigungu;
    Long sigunguId;
    String sido;
    Long sidoId;
}
