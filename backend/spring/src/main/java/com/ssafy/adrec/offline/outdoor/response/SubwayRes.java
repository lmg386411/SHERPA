package com.ssafy.adrec.offline.outdoor.response;

import lombok.Builder;
import lombok.Getter;

@Getter
public class SubwayRes {

    int rank;
    String station;
    int ratio;

    @Builder
    public SubwayRes(int rank, String station, int ratio) {
        this.rank = rank;
        this.station = station;
        this.ratio = ratio;
    }

}
