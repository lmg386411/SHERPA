package com.ssafy.adrec.myPage.request;

import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
public class MyProductModifyPutReq {

    String name;
    Long productSmall_id;

    @Builder
    public MyProductModifyPutReq(String name, Long productSmall_id) {
        this.name = name;
        this.productSmall_id = productSmall_id;
    }
    
}
