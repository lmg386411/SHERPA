package com.ssafy.adrec.product.controller;

import com.ssafy.adrec.member.controller.MemberController;
import com.ssafy.adrec.product.ProductType;
import com.ssafy.adrec.product.response.ProductGetRes;
import com.ssafy.adrec.product.service.ProductService;
import lombok.RequiredArgsConstructor;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@RestController
@RequiredArgsConstructor
@RequestMapping("/product")
@CrossOrigin(origins = "*")
public class ProductController {

    public static final Logger logger = LoggerFactory.getLogger(MemberController.class);

    private final ProductService productService;

    @GetMapping("/{type}/{id}")
    public ResponseEntity<?> getProductLargeList(@PathVariable("type") String type, @PathVariable("id") Long id) {
        List<ProductGetRes> list = new ArrayList<>();

        Map<String, Object> resultMap = new HashMap<>();
        HttpStatus httpStatus = null;

        switch (type) {
            case "L":
                list = productService.getList(ProductType.LARGE, id);
                resultMap.put("msg", "품목 대분류 리스트 조회");
                break;
            case "M":
                list = productService.getList(ProductType.MEDIUM, id);
                resultMap.put("msg", "품목 중분류 리스트 조회");
                break;
            case "S":
                list = productService.getList(ProductType.SMALL, id);
                resultMap.put("msg", "품목 소분류 리스트 조회");
                break;
        }

        if (list.size() == 0) {
            resultMap.put("success", false);
            resultMap.put("msg", "해당 데이터가 없습니다.");
            httpStatus = HttpStatus.NOT_FOUND;
        } else {
            resultMap.put("success", true);
            resultMap.put("data", list);
            resultMap.put("count", list.size());
            httpStatus = HttpStatus.OK;
        }

        return new ResponseEntity<>(resultMap, httpStatus);
    }

    @GetMapping("/{id}")
    public ResponseEntity<?> getProductId(@PathVariable("id") Long id) {
        Map<String, Object> resultMap = new HashMap<>();
        HttpStatus httpStatus = null;

        Long mediumId = productService.getProductId(ProductType.SMALL, id);
        Long largeId = productService.getProductId(ProductType.MEDIUM, mediumId);

        Map<String, Object> productIds = new HashMap<>();
        productIds.put("M", mediumId);
        productIds.put("L", largeId);

        resultMap.put("success", true);
        resultMap.put("data", productIds);
        resultMap.put("msg", "품목 대/중 아이디 조회");
        httpStatus = HttpStatus.OK;

        return new ResponseEntity<>(resultMap, httpStatus);
    }

}
