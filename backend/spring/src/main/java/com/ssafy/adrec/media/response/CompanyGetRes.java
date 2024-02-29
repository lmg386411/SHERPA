package com.ssafy.adrec.media.response;

import lombok.Getter;

@Getter
public class CompanyGetRes {

    String img;
    String title;
    String url;

    public CompanyGetRes(String img, String title, String url){
        this.img = img;
        this.title = title;
        this.url = url;
    }
}
