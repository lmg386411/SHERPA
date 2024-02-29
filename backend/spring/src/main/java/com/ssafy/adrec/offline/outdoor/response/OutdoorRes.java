package com.ssafy.adrec.offline.outdoor.response;

import lombok.Builder;
import lombok.Getter;

@Getter
public class OutdoorRes {
    String type;
    double ratio;
    int total;

    @Builder
    public OutdoorRes(String type, double ratio,int total) {
        this.type = type;
        this.ratio = ratio;
        this.total = total;
    }
}
