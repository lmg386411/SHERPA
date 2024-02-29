package com.ssafy.adrec.media.response;

import lombok.Getter;

@Getter
public class MediaSubGetRes {

    Long id;
    String type;

    public MediaSubGetRes(Long id, String type) {
        this.id = id;
        this.type = type;
    }
}
