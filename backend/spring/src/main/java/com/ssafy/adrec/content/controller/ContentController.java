package com.ssafy.adrec.content.controller;

import com.ssafy.adrec.content.ContentKeyword;
import com.ssafy.adrec.content.ContentLike;
import com.ssafy.adrec.content.ContentRec;
import com.ssafy.adrec.content.request.ContentRecListReq;
import com.ssafy.adrec.content.request.ContentRecReq;
import com.ssafy.adrec.content.service.ContentService;
import com.ssafy.adrec.keyword.request.KeywordLikeReq;
import com.ssafy.adrec.keyword.service.KeywordService;
import com.ssafy.adrec.media.MediaSub;
import com.ssafy.adrec.media.MediaType;
import com.ssafy.adrec.media.MediaTypes;
import com.ssafy.adrec.media.service.MediaService;
import com.ssafy.adrec.member.Member;
import com.ssafy.adrec.member.controller.MemberController;
import com.ssafy.adrec.member.service.MemberService;
import com.ssafy.adrec.myPage.service.MyPageService;
import com.ssafy.adrec.product.ProductSmall;
import com.ssafy.adrec.product.service.ProductService;
import lombok.RequiredArgsConstructor;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@RestController
@RequiredArgsConstructor
@RequestMapping("/content")
@CrossOrigin(origins = "*")
public class ContentController {

    public static final Logger logger = LoggerFactory.getLogger(MemberController.class);

    private final MemberService memberService;
    private final ProductService productService;
    private final MediaService mediaService;
    private final ContentService contentService;
    private final MyPageService myPageService;

    @PostMapping("/save")
    public ResponseEntity<?> saveContent(@RequestBody ContentRecReq contentRecReq) {

        Map<String, Object> resultMap = new HashMap<>();
        HttpStatus httpStatus = null;

        resultMap.put("msg", "광고 컨텐츠 추천 결과 저장");

        String name = contentRecReq.getMemberName();
        Long productSmallId = contentRecReq.getProductSmallId();
        Long mediaTypeId = contentRecReq.getMediaTypeId();
        Long mediaSubId = contentRecReq.getMediaSubId();
        List<String> keywordList = contentRecReq.getKeywordList();
        List<ContentRecListReq> contentList = contentRecReq.getContentList();
//        System.out.println(contentRecReq);
//        System.out.println(contentRecReq.getContentList());
//        System.out.println("ContentController "+name+ " "+productSmallId+" "+mediaTypeId+" "+mediaSubId+" ");
//        System.out.println(Arrays.toString(new List[]{keywordList}));
//        System.out.println(Arrays.toString(new List[]{contentList}));

        Member member = memberService.checkName(name);
        if (member == null) {
            resultMap.put("success", false);
            resultMap.put("msg", String.format("[%s]은/는 회원가입된 유저ID가 아닙니다.",name));
            httpStatus = HttpStatus.NOT_FOUND;
            return new ResponseEntity<>(resultMap, httpStatus);

        }

        // contentRec 테이블에 productSmall, member, mediaType, mediaSub 보관
        ProductSmall productSmall = productService.getProductSmall(productSmallId);
        if(productSmall == null){
            resultMap.put("success", false);
            resultMap.put("msg", String.format("[%d]품목코드는 존재하지 않습니다.",productSmallId));
            httpStatus = HttpStatus.BAD_REQUEST;
            return new ResponseEntity<>(resultMap, httpStatus);
        }

        MediaType mediaType;
        MediaSub mediaSub = null;
        if(mediaTypeId == 6){
            mediaType = mediaService.getMediaType(mediaTypeId);
            mediaSub = mediaService.getMediaSub(mediaSubId);
        }else{
            mediaType = mediaService.getMediaType(mediaTypeId);
        }

        ContentRec contentRec = contentService.saveContentRec(productSmall, member, mediaType, mediaSub, mediaTypeId);

        // 키워드들은 따로 contentKeyword에 보관
        ContentKeyword contentKeyword = contentService.saveContentKeyword(contentRec, keywordList);

        // 문구들은 따로 contentLike에 보관
        ContentLike contentLike = contentService.saveContentLike(contentRec, contentList);

        resultMap.put("success", true);
        resultMap.put("msg", "광고 컨텐츠 추천 결과 저장을 성공적으로 진행했습니다.");
        httpStatus = HttpStatus.OK;
        return new ResponseEntity<>(resultMap, httpStatus);
    }

    @GetMapping("/keyword/{memberName}/{productSmallId}")
    public ResponseEntity<?> getKeywordList(@PathVariable("memberName") String memberName,@PathVariable("productSmallId") Long productSmallId){
        Map<String, Object> resultMap = new HashMap<>();
        HttpStatus httpStatus = null;

        Member member = memberService.checkName(memberName);
        if (member == null) {
            resultMap.put("success", false);
            resultMap.put("msg", String.format("[%s]은/는 회원가입된 유저ID가 아닙니다.",memberName));
            httpStatus = HttpStatus.NOT_FOUND;
            return new ResponseEntity<Map<String, Object>>(resultMap, httpStatus);

        }

        ProductSmall productSmall =productService.getProductSmall(productSmallId);
        if (productSmall == null) {
            resultMap.put("success", false);
            resultMap.put("msg", String.format("[%d]은/는 유요한 품목 코드가 아닙니다.",productSmallId));
            httpStatus = HttpStatus.NOT_FOUND;
            return new ResponseEntity<Map<String, Object>>(resultMap, httpStatus);
        }

        List<String> keywordList = myPageService.getKeywordList(member, productSmall);

        if (keywordList.size() == 0) {
            resultMap.put("success", false);
            resultMap.put("msg", "해당 데이터가 없습니다.");
            httpStatus = HttpStatus.NOT_FOUND;
        } else {
            resultMap.put("msg", "품목에 해당하는 좋아용한 키워드 목록 가져오기.");
            resultMap.put("success", true);
            resultMap.put("data", keywordList);
            resultMap.put("count", keywordList.size());
            httpStatus = HttpStatus.OK;
        }

        return new ResponseEntity<>(resultMap, httpStatus);


    }


}
