package com.ssafy.adrec.targetAnalyze.request;

import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
public class TargetReq {

    Long productSmallId;
    Long sigunguId;

    @Builder
    public TargetReq(Long productSmallId, Long sigunguId){
        this.productSmallId = productSmallId;
        this.sigunguId = sigunguId;
    }
}
