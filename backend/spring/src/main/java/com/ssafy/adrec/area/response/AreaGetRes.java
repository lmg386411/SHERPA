package com.ssafy.adrec.area.response;

import lombok.Getter;

@Getter
public class AreaGetRes {
    Long id;
    String area;

    public AreaGetRes(Long id, String area) {
        this.id = id;
        this.area = area;
    }
}
