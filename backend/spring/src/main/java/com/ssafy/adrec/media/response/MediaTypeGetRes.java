package com.ssafy.adrec.media.response;

import lombok.Getter;

@Getter
public class MediaTypeGetRes {

    Long id;
    String large;
    String medium;

    public MediaTypeGetRes(Long id, String large, String medium) {
        this.id = id;
        this.large = large;
        this.medium = medium;
    }
}
