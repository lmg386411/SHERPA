package com.ssafy.adrec.offline.outdoor.response;

import lombok.Builder;
import lombok.Getter;

@Getter
public class BannerRes {

    int no;
    String address;
    String name;

    @Builder
    public BannerRes(int no, String address, String name) {
        this.no = no;
        this.address = address;
        this.name = name;
    }

}
