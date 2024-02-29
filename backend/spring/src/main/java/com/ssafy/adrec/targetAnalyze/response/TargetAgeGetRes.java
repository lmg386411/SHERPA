package com.ssafy.adrec.targetAnalyze.response;

import lombok.Getter;

@Getter
public class TargetAgeGetRes {
    String age;
    String value;

    public TargetAgeGetRes(String age, String value){
        this.age = age;
        this.value = value;
    }
}
