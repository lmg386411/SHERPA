package com.ssafy.adrec.product.service;

import com.ssafy.adrec.member.service.MemberServiceImpl;
import com.ssafy.adrec.product.ProductLarge;
import com.ssafy.adrec.product.ProductMedium;
import com.ssafy.adrec.product.ProductSmall;
import com.ssafy.adrec.product.ProductType;
import com.ssafy.adrec.product.repository.ProductLargeRepository;
import com.ssafy.adrec.product.repository.ProductMediumRepository;
import com.ssafy.adrec.product.repository.ProductSmallRepository;
import com.ssafy.adrec.product.response.ProductGetRes;
import lombok.RequiredArgsConstructor;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

@Service
@RequiredArgsConstructor
public class ProductServiceImpl implements ProductService {

    public static final Logger logger = LoggerFactory.getLogger(MemberServiceImpl.class);

    private final ProductLargeRepository productLargeRepository;
    private final ProductMediumRepository productMediumRepository;
    private final ProductSmallRepository productSmallRepository;

    // 품목 대,중,소분류 리스트
    @Override
    public List<ProductGetRes> getList(ProductType productType, Long id) {
        List<ProductGetRes> list = new ArrayList<>();

        switch (productType) {
            case LARGE:
                List<ProductLarge> productLarges = productLargeRepository.findAll();
                for (ProductLarge productLarge : productLarges) {
                    list.add(new ProductGetRes(productLarge.getId(), productLarge.getLarge()));
                }
                break;
            case MEDIUM:
                List<ProductMedium> productMediums = productMediumRepository.findAllByProductLarge_Id(id);
                for (ProductMedium productMedium : productMediums) {
                    list.add(new ProductGetRes(productMedium.getId(), productMedium.getMedium()));
                }
                break;
            case SMALL:
                List<ProductSmall> productSmalls = productSmallRepository.findAllByProductMedium_Id(id);
                for (ProductSmall productSmall : productSmalls) {
                    list.add(new ProductGetRes(productSmall.getId(), productSmall.getSmall()));
                }
                break;
        }

        return list;
    }

    // 품목 대, 중, 소분류 아이디 가져오기
    @Override
    public Long getProductId(ProductType productType, Long id) {
        Long productId = null;

        switch (productType) {
            case SMALL:
                Optional<ProductSmall> productSmall = productSmallRepository.findById(id);
                if (productSmall.isPresent()) {
                    productId = productSmall.get().getProductMedium().getId();
                }
                break;
            case MEDIUM:
                Optional<ProductMedium> productMedium = productMediumRepository.findById(id);
                if (productMedium.isPresent()) {
                    productId = productMedium.get().getProductLarge().getId();
                }
                break;
        }

        return productId;
    }

    @Override
    public ProductSmall getProductSmall (Long id){
        Optional<ProductSmall> productSmall = productSmallRepository.findById(id);
        if(productSmall.isEmpty()){
            return null;
        }

        return productSmall.get();
    }
    
}
