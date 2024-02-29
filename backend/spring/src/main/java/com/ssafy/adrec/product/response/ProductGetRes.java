package com.ssafy.adrec.product.response;

import lombok.Getter;

@Getter
public class ProductGetRes {

    Long id;
    String product;

    public ProductGetRes(Long id, String product) {
        this.id = id;
        this.product = product;
    }

}
