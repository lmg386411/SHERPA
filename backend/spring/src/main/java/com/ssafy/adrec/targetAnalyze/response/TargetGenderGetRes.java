package com.ssafy.adrec.targetAnalyze.response;

import lombok.Getter;

@Getter
public class TargetGenderGetRes {

    String gender;
    String value;

    public TargetGenderGetRes(String gender, String value){
        this.gender = gender;
        this.value = value;
    }
}
