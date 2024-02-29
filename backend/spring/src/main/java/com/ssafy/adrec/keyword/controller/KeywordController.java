package com.ssafy.adrec.keyword.controller;

import com.ssafy.adrec.keyword.KeywordLike;
import com.ssafy.adrec.keyword.KeywordRec;
import com.ssafy.adrec.keyword.request.KeywordLikeReq;
//import com.ssafy.adrec.keyword.response.KeywordRecRes;
import com.ssafy.adrec.keyword.response.KeywordLikeRes;
import com.ssafy.adrec.keyword.response.KeywordRes;
import com.ssafy.adrec.keyword.service.KeywordService;
import com.ssafy.adrec.member.Member;
import com.ssafy.adrec.member.controller.MemberController;
import com.ssafy.adrec.member.service.MemberService;
import com.ssafy.adrec.product.ProductSmall;
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
@RequestMapping("/keyword")
@CrossOrigin(origins = "*")
public class KeywordController {

    public static final Logger logger = LoggerFactory.getLogger(MemberController.class);

    private final KeywordService keywordService;
    private final MemberService memberService;
    private final ProductService productService;

    @GetMapping("/ad/{productSmallId}")
    public ResponseEntity<?> getKeywordAdList( @PathVariable("productSmallId") Long productSmallId){
        List<KeywordRes> list = new ArrayList<>();

        Map<String, Object> resultMap = new HashMap<>();
        HttpStatus httpStatus = null;

        list = keywordService.getKeywordAdList(productSmallId);
        resultMap.put("msg", "키워드 리스트 조회");

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

    @GetMapping("/trend")
    public ResponseEntity<?> getKeywordTrendList(){
        List<KeywordRes> list = new ArrayList<>();

        Map<String, Object> resultMap = new HashMap<>();
        HttpStatus httpStatus = null;

        list = keywordService.getKeywordTrendList();
        resultMap.put("msg", "트랜드 키워드 리스트 조회");

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

    @PostMapping("/like")
    public ResponseEntity<?> saveKeywordLike(@RequestBody KeywordLikeReq keywordLikeReq){
        Map<String, Object> resultMap = new HashMap<>();
        HttpStatus httpStatus = null;

        resultMap.put("msg", "키워드 좋아요");

        String keyword = keywordLikeReq.getKeyword();
        String name = keywordLikeReq.getMemberName();
        Long keywordRecId = keywordLikeReq.getKeywordRecId();
        Long productSmallId = keywordLikeReq.getProductSmallId();

        Member member = memberService.checkName(name);
        if (member == null) {
            resultMap.put("success", false);
            resultMap.put("msg", String.format("[%s]은/는 회원가입된 유저ID가 아닙니다.",name));
            httpStatus = HttpStatus.NOT_FOUND;
            return new ResponseEntity<Map<String, Object>>(resultMap, httpStatus);

        }

        if (keywordRecId == 0){
            //보관함을 생성하고
            ProductSmall productSmall = productService.getProductSmall(productSmallId);
            KeywordRec savedkeywordRec = keywordService.saveKeywordRec(member, productSmall);

            //키워드를 저장한다.
            KeywordLike keywordLike = keywordService.saveKeywordLike(keyword, savedkeywordRec);
            KeywordLikeRes keywordLikeRes = KeywordLikeRes.builder()
                    .keyword(keywordLike.getKeyword())
                    .name(savedkeywordRec.getMember().getName())
                    .keywordRecId(savedkeywordRec.getId())
                    .productSmall(savedkeywordRec.getProductSmall().getSmall())
                    .build();
            resultMap.put("success", true);
            resultMap.put("data", keywordLikeRes);
            resultMap.put("count", 1);
            httpStatus = HttpStatus.OK;

        }
        else{
            KeywordRec keywordRec = keywordService.getKeywordRec(keywordRecId);
            Long ki = keywordRec.getProductSmall().getId();

            if (keywordRec == null) {
                resultMap.put("success", false);
                resultMap.put("msg", String.format("[%d]은/는 유효하지 않는 보관함ID입니다.",keywordRecId));
                httpStatus = HttpStatus.NOT_FOUND;
            }
            else if(! keywordRec.getMember().getName().equals(name)){
                resultMap.put("success", false);
                resultMap.put("msg", String.format("[%s]유저는 [%d]보관함을 이용했던 유저가 아닙니다.",keywordRec.getMember().getName(),keywordRecId));
                httpStatus = HttpStatus.BAD_REQUEST;
            }
            else if(!ki.equals(productSmallId)){
                System.out.println(keywordRec.getProductSmall().getId());
                System.out.println( productSmallId);
                resultMap.put("success", false);
                resultMap.put("msg", String.format("[%d]품목코드는 [%d]보관함에 저장했던 품목 코드와 다릅니다.",productSmallId, keywordRecId));
                httpStatus = HttpStatus.BAD_REQUEST;
            }
            else{
                //키워드를 저장한다.
                KeywordLike keywordLike = keywordService.saveKeywordLike(keyword, keywordRec);
                KeywordLikeRes keywordLikeRes = KeywordLikeRes.builder()
                        .keyword(keywordLike.getKeyword())
                        .name(keywordRec.getMember().getName())
                        .keywordRecId(keywordRec.getId())
                        .productSmall(keywordRec.getProductSmall().getSmall())
                        .build();
                resultMap.put("success", true);
                resultMap.put("data", keywordLikeRes);
                resultMap.put("count", 1);
                httpStatus = HttpStatus.OK;
            }

        }
        return new ResponseEntity<Map<String, Object>>(resultMap, httpStatus);

    }


}
