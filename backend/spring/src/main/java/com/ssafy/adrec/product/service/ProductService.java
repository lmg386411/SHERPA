package com.ssafy.adrec.product.service;

import com.ssafy.adrec.product.ProductSmall;
import com.ssafy.adrec.product.ProductType;
import com.ssafy.adrec.product.response.ProductGetRes;

import java.util.List;

public interface ProductService {

    // 품목 대,중,소분류 리스트
    List<ProductGetRes> getList(ProductType productType, Long id);

    // 품목 대, 중분류 아이디 가져오기
    Long getProductId(ProductType productType,Long id);

    ProductSmall getProductSmall (Long id);
    
}
