package com.ssafy.adrec.myPage.controller;

import com.ssafy.adrec.area.Sigungu;
import com.ssafy.adrec.area.service.AreaService;
import com.ssafy.adrec.content.ContentLike;
import com.ssafy.adrec.content.ContentRec;
import com.ssafy.adrec.content.service.ContentService;
import com.ssafy.adrec.keyword.KeywordLike;
import com.ssafy.adrec.keyword.KeywordRec;
import com.ssafy.adrec.keyword.request.KeywordLikeReq;
import com.ssafy.adrec.keyword.service.KeywordService;
import com.ssafy.adrec.media.MediaSub;
import com.ssafy.adrec.media.MediaType;
import com.ssafy.adrec.member.Member;
import com.ssafy.adrec.member.controller.MemberController;
import com.ssafy.adrec.member.service.MemberService;
import com.ssafy.adrec.myPage.MediaRec;
import com.ssafy.adrec.myPage.request.MediaRecReq;
import com.ssafy.adrec.myPage.request.MyPageModifyPutReq;
import com.ssafy.adrec.myPage.request.MyProductModifyPutReq;
import com.ssafy.adrec.myPage.response.*;
import com.ssafy.adrec.myPage.service.MyPageService;
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
@RequestMapping("/mypage")
@CrossOrigin(origins = "*")
public class MyPageController {
    public static final Logger logger = LoggerFactory.getLogger(MemberController.class);

    private final MyPageService myPageService;
    private final MemberService memberService;
    private final KeywordService keywordService;
    private final ProductService productService;
    private final AreaService areaService;
    private final ContentService contentService;

    @GetMapping("/keyword/{memberName}")
    public ResponseEntity<?> getKeywordRecList(@PathVariable("memberName") String memberName) {
        List<KeywordRecRes> list = new ArrayList<>();

        Map<String, Object> resultMap = new HashMap<>();
        HttpStatus httpStatus = null;
        resultMap.put("msg", "좋아요한 키워드 목록 조회");

        Member member = memberService.checkName(memberName);
        if (member == null) {
            resultMap.put("success", false);
            resultMap.put("msg", String.format("[%s]은/는 회원가입된 유저ID가 아닙니다.", memberName));
            httpStatus = HttpStatus.NOT_FOUND;
            return new ResponseEntity<Map<String, Object>>(resultMap, httpStatus);
        }

        list = myPageService.getKeywordRecList(member.getId());
        resultMap.put("success", true);
        resultMap.put("data", list);
        resultMap.put("count", list.size());
        httpStatus = HttpStatus.OK;

        return new ResponseEntity<>(resultMap, httpStatus);
    }

    @GetMapping("/keyword/rec/{memberName}/{keywordRecId}")
    public ResponseEntity<?> getKeywordRec(@PathVariable("memberName") String memberName, @PathVariable("keywordRecId") Long keywordRecId) {

        Map<String, Object> resultMap = new HashMap<>();
        HttpStatus httpStatus = null;
        resultMap.put("msg", "좋아요한 키워드 목록 상세 보기 ");

        Member member = memberService.checkName(memberName);
        if (member == null) {
            resultMap.put("success", false);
            resultMap.put("msg", String.format("[%s]은/는 회원가입된 유저ID가 아닙니다.", memberName));
            httpStatus = HttpStatus.NOT_FOUND;
            return new ResponseEntity<Map<String, Object>>(resultMap, httpStatus);
        }

        KeywordRec keywordRec = keywordService.getKeywordRec(keywordRecId);
        if (keywordRec == null) {
            resultMap.put("success", false);
            resultMap.put("msg", String.format("[%d]은/는 유효하지 않는 보관함ID입니다.", keywordRecId));
            httpStatus = HttpStatus.NOT_FOUND;
            return new ResponseEntity<Map<String, Object>>(resultMap, httpStatus);
        }

        List<KeywordIdKeyword> keywordIdKeywordList = myPageService.getKeywordIdKeywordList(keywordRecId);

        KeywordRecRes keywordRecRes = KeywordRecRes.builder()
                .id(keywordRec.getId())
                .recDate(keywordRec.getRecDate())
                .productSmall(keywordRec.getProductSmall().getSmall())
                .keywordList(keywordIdKeywordList)
                .build();

        resultMap.put("success", true);
        resultMap.put("data", keywordRecRes);
        resultMap.put("count", 1);
        httpStatus = HttpStatus.OK;

        return new ResponseEntity<>(resultMap, httpStatus);

    }


    @DeleteMapping("/keyword/like/{memberName}/{keywordLikeId}")
    public ResponseEntity<?> deleteKeywordLike(@PathVariable("memberName") String memberName, @PathVariable("keywordLikeId") Long keywordLikeId) {

        Map<String, Object> resultMap = new HashMap<>();
        HttpStatus httpStatus = null;
        resultMap.put("msg", "좋아요한 키워드 삭제");


        Member member = memberService.checkName(memberName);
        if (member == null) {
            resultMap.put("success", false);
            resultMap.put("msg", String.format("[%s]은/는 회원가입된 유저ID가 아닙니다.", memberName));
            httpStatus = HttpStatus.NOT_FOUND;
            return new ResponseEntity<Map<String, Object>>(resultMap, httpStatus);
        }


        KeywordLike keywordLike = keywordService.getKeywordLike(keywordLikeId);
        if (keywordLike == null) {
            resultMap.put("success", false);
            resultMap.put("msg", String.format("[%d]은/는 유효하지 않는 좋아요 키워드ID입니다.", keywordLikeId));
            httpStatus = HttpStatus.NOT_FOUND;
            return new ResponseEntity<Map<String, Object>>(resultMap, httpStatus);
        }

        myPageService.deleteKeywordLike(keywordLike);

        resultMap.put("success", true);
        resultMap.put("data", String.format("[%s]키워드를 삭제하였습니다.", keywordLike.getKeyword()));
        resultMap.put("count", 1);
        httpStatus = HttpStatus.OK;

        return new ResponseEntity<>(resultMap, httpStatus);

    }

    @DeleteMapping("/keyword/rec/{memberName}/{keywordRecId}")
    public ResponseEntity<?> deleteKeywordRec(@PathVariable("memberName") String memberName, @PathVariable("keywordRecId") Long keywordRecId) {

        Map<String, Object> resultMap = new HashMap<>();
        HttpStatus httpStatus = null;
        resultMap.put("msg", "좋아요한 키워드 목록 삭제");


        Member member = memberService.checkName(memberName);
        if (member == null) {
            resultMap.put("success", false);
            resultMap.put("msg", String.format("[%s]은/는 회원가입된 유저ID가 아닙니다.", memberName));
            httpStatus = HttpStatus.NOT_FOUND;
            return new ResponseEntity<Map<String, Object>>(resultMap, httpStatus);
        }


        KeywordRec keywordRec = keywordService.getKeywordRec(keywordRecId);
        if (keywordRec == null) {
            resultMap.put("success", false);
            resultMap.put("msg", String.format("[%d]은/는 유효하지 않는 보관함ID입니다.", keywordRecId));
            httpStatus = HttpStatus.NOT_FOUND;
            return new ResponseEntity<Map<String, Object>>(resultMap, httpStatus);
        }

        myPageService.deleteKeywordRec(keywordRec);

        resultMap.put("success", true);
        resultMap.put("data", String.format("[%d]보관함을 삭제하였습니다.", keywordRecId));
        resultMap.put("count", 1);
        httpStatus = HttpStatus.OK;

        return new ResponseEntity<>(resultMap, httpStatus);

    }

    @GetMapping("/profile/{name}")
    public ResponseEntity<?> getMemberInfo(@PathVariable("name") String name) {
        Map<String, Object> resultMap = new HashMap<>();
        HttpStatus httpStatus = null;

        Member member = memberService.checkName(name);

        if (member == null) {
            resultMap.put("success", false);
            resultMap.put("msg", "해당 계정의 정보가 존재하지 않습니다.");
            httpStatus = HttpStatus.INTERNAL_SERVER_ERROR;
        } else {
            resultMap.put("data", member);
            resultMap.put("success", true);
            resultMap.put("msg", "회원 정보 조회 성공");
            httpStatus = HttpStatus.OK;
        }

        return new ResponseEntity<>(resultMap, httpStatus);
    }

    @PutMapping("/profile")
    public ResponseEntity<?> modifyMember(@RequestBody MyPageModifyPutReq myPageModifyPutReq) {
        Map<String, Object> resultMap = new HashMap<>();
        HttpStatus httpStatus = null;

        Member member = myPageService.modifyMember(myPageModifyPutReq);

        if (member == null) {
            resultMap.put("success", false);
            resultMap.put("msg", "회원 정보 수정 실패");
            httpStatus = HttpStatus.INTERNAL_SERVER_ERROR;
        } else {
            resultMap.put("success", true);
            resultMap.put("msg", "회원 정보 수정 성공");
            httpStatus = HttpStatus.OK;
        }

        return new ResponseEntity<>(resultMap, httpStatus);
    }

    @PutMapping("/product")
    public ResponseEntity<?> modifyProduct(@RequestBody MyProductModifyPutReq myProductModifyPutReq) {
        Map<String, Object> resultMap = new HashMap<>();
        HttpStatus httpStatus = null;

        Member member = myPageService.modifyProduct(myProductModifyPutReq);

        if (member == null) {
            resultMap.put("success", false);
            resultMap.put("msg", "품목 정보 수정 실패");
            httpStatus = HttpStatus.INTERNAL_SERVER_ERROR;
        } else {
            resultMap.put("success", true);
            resultMap.put("msg", "품목 정보 수정 성공");
            httpStatus = HttpStatus.OK;
        }

        return new ResponseEntity<>(resultMap, httpStatus);
    }

    @PostMapping("/save/mediaRec")
    public ResponseEntity<?> saveMediaRec(@RequestBody MediaRecReq mediaRecReq) {
        Map<String, Object> resultMap = new HashMap<>();
        HttpStatus httpStatus = null;

        if ((mediaRecReq.getInOnOff() != 0 && mediaRecReq.getInOnOff() != 1)) {
            resultMap.put("success", false);
            resultMap.put("msg", String.format("[inOnOff]의 값으로 [%d]은/는 잘못된 요청입니다. 온라인 여부는 0(온라인)또는 1(오프라인)로 전달해주세요.", mediaRecReq.getInOnOff()));
            httpStatus = HttpStatus.BAD_REQUEST;
            return new ResponseEntity<Map<String, Object>>(resultMap, httpStatus);

        }

        Member member = memberService.checkName(mediaRecReq.getMemberName());
        if (member == null) {
            resultMap.put("success", false);
            resultMap.put("msg", String.format("[%s]은/는 회원가입된 유저ID가 아닙니다.", mediaRecReq.getMemberName()));
            httpStatus = HttpStatus.NOT_FOUND;
            return new ResponseEntity<Map<String, Object>>(resultMap, httpStatus);

        }

        ProductSmall productSmall = productService.getProductSmall(mediaRecReq.getProductSmallId());
        if (productSmall == null) {
            resultMap.put("success", false);
            resultMap.put("msg", String.format("[%d]은/는 유요한 품목 코드가 아닙니다.", mediaRecReq.getProductSmallId()));
            httpStatus = HttpStatus.NOT_FOUND;
            return new ResponseEntity<Map<String, Object>>(resultMap, httpStatus);
        }

        Sigungu sigungu = areaService.getSigungu(mediaRecReq.getSigunguId());
        if (productSmall == null) {
            resultMap.put("success", false);
            resultMap.put("msg", String.format("[%d]은/는 유요한 시군구 코드가 아닙니다.", mediaRecReq.getSigunguId()));
            httpStatus = HttpStatus.NOT_FOUND;
            return new ResponseEntity<Map<String, Object>>(resultMap, httpStatus);
        }

        MediaType mediaType = myPageService.getMediaType(mediaRecReq.getMediaTypeId());
        if (mediaType == null) {
            resultMap.put("success", false);
            resultMap.put("msg", String.format("[%d]은/는 유요한 MediaType 코드가 아닙니다.", mediaRecReq.getMediaTypeId()));
            httpStatus = HttpStatus.NOT_FOUND;
            return new ResponseEntity<Map<String, Object>>(resultMap, httpStatus);
        }


        MediaRec mediaRec = myPageService.saveMediaRec(mediaRecReq, productSmall, sigungu, member, mediaType);

        if (mediaRec == null) {
            resultMap.put("success", false);
            resultMap.put("msg", "미디어추천 결과 저장 실패");
            httpStatus = HttpStatus.INTERNAL_SERVER_ERROR;
        } else {
            resultMap.put("success", true);
            resultMap.put("msg", "미디어추천 결과 저장 성공");
            httpStatus = HttpStatus.OK;
        }


        return new ResponseEntity<>(resultMap, httpStatus);

    }

    @GetMapping("/mediaRec/{memberName}")
    public ResponseEntity<?> getMediaRecList(@PathVariable("memberName") String memberName) {
        Map<String, Object> resultMap = new HashMap<>();
        HttpStatus httpStatus = null;
        resultMap.put("msg", "매체 추천 목록 조회");

        Member member = memberService.checkName(memberName);
        if (member == null) {
            resultMap.put("success", false);
            resultMap.put("msg", String.format("[%s]은/는 회원가입된 유저ID가 아닙니다.", memberName));
            httpStatus = HttpStatus.NOT_FOUND;
            return new ResponseEntity<Map<String, Object>>(resultMap, httpStatus);
        }
        List<MediaRecRes> mediaRecResList = myPageService.getMediaRecList(member.getId());

        if (mediaRecResList.size() == 0) {
            resultMap.put("success", false);
            resultMap.put("msg", "해당 데이터가 없습니다.");
            httpStatus = HttpStatus.NOT_FOUND;
        } else {
            resultMap.put("success", true);
            resultMap.put("data", mediaRecResList);
            resultMap.put("count", mediaRecResList.size());
            httpStatus = HttpStatus.OK;
        }


        return new ResponseEntity<>(resultMap, httpStatus);
    }

    @GetMapping("/mediaRec/{memberName}/{id}")
    public ResponseEntity<?> getMediaRec(@PathVariable("memberName") String memberName, @PathVariable("id") Long id) {
        Map<String, Object> resultMap = new HashMap<>();
        HttpStatus httpStatus = null;
        resultMap.put("msg", "매체 추천 목록 상세 조회");

        Member member = memberService.checkName(memberName);
        if (member == null) {
            resultMap.put("success", false);
            resultMap.put("msg", String.format("[%s]은/는 회원가입된 유저ID가 아닙니다.", memberName));
            httpStatus = HttpStatus.NOT_FOUND;
            return new ResponseEntity<Map<String, Object>>(resultMap, httpStatus);

        }

        MediaRec mediaRec = myPageService.getMediaRec(id);

        if (mediaRec == null) {
            resultMap.put("success", false);
            resultMap.put("msg", String.format("[%d]은/는 잘못된 매체 추천 결과 id 입니다.", id));
            httpStatus = HttpStatus.NOT_FOUND;

        } else if (mediaRec.getMember().getName().equals(memberName)) {
            int onOff = (mediaRec.isOnOff()) ? 1 : 0;
            Sigungu sigungu= mediaRec.getSigungu();
            MediaRecRes mediaRecRes = MediaRecRes.builder()
                    .id(mediaRec.getId())
                    .recDate(mediaRec.getRecDate())
                    .isOnOff(onOff)
                    .budget(mediaRec.getBudget())
                    .sigungu(sigungu.getName())
                    .sigunguId(sigungu.getId())
                    .sidoId(sigungu.getSido().getId())
                    .sido(sigungu.getSido().getName())
                    .productSmall(mediaRec.getProductSmall().getSmall())
                    .productSmallId(mediaRec.getProductSmall().getId())
                    .mediaTypeId(mediaRec.getMediaType().getId())
                    .build();

            resultMap.put("success", true);
            resultMap.put("data", mediaRecRes);
            resultMap.put("count", 1);
            httpStatus = HttpStatus.OK;

        } else {
            resultMap.put("success", false);
            resultMap.put("msg", String.format("[%d]은/는 [%s]유저의 매체추천 결과가 아닙니다.", id, memberName));
            httpStatus = HttpStatus.BAD_REQUEST;
        }


        return new ResponseEntity<>(resultMap, httpStatus);
    }

    @DeleteMapping("/mediaRec/{memberName}/{id}")
    public ResponseEntity<?> deleteMediaRec(@PathVariable("memberName") String memberName, @PathVariable("id") Long id) {
        Map<String, Object> resultMap = new HashMap<>();
        HttpStatus httpStatus = null;

        Member member = memberService.checkName(memberName);
        if (member == null) {
            resultMap.put("success", false);
            resultMap.put("msg", String.format("[%s]은/는 회원가입된 유저ID가 아닙니다.", memberName));
            httpStatus = HttpStatus.NOT_FOUND;
            return new ResponseEntity<Map<String, Object>>(resultMap, httpStatus);

        }

        MediaRec mediaRec = myPageService.getMediaRec(id);

        if (mediaRec == null) {
            resultMap.put("success", false);
            resultMap.put("msg", String.format("[%d]은/는 잘못된 매체 추천 결과 id 입니다.", id));
            httpStatus = HttpStatus.NOT_FOUND;

        } else if (mediaRec.getMember().getName().equals(memberName)) {
            myPageService.deleteMediaRec(mediaRec);

            resultMap.put("success", true);
            resultMap.put("msg", String.format("[%d]id에 해당하는 매체추천 결과를 삭제하였습니다.", id));
            httpStatus = HttpStatus.OK;

        } else {
            resultMap.put("success", false);
            resultMap.put("msg", String.format("[%d]은/는 [%s]유저의 매체추천 결과가 아닙니다.", id, memberName));
            httpStatus = HttpStatus.BAD_REQUEST;
        }

        return new ResponseEntity<>(resultMap, httpStatus);
    }

    @GetMapping("/content/{memberName}")
    public ResponseEntity<?> getContentRecList(@PathVariable("memberName") String memberName) {

        Map<String, Object> resultMap = new HashMap<>();
        HttpStatus httpStatus = null;
        resultMap.put("msg", "컨텐츠 추천 목록 조회");

        Member member = memberService.checkName(memberName);
        if (member == null) {
            resultMap.put("success", false);
            resultMap.put("msg", String.format("[%s]은/는 회원가입된 유저ID가 아닙니다.", memberName));
            httpStatus = HttpStatus.NOT_FOUND;
            return new ResponseEntity<>(resultMap, httpStatus);

        }

        List<ContentRecRes> contentRecResList = myPageService.getContentRecList(member.getId());

        if (contentRecResList.size() == 0) {
            resultMap.put("success", false);
            resultMap.put("msg", "해당 데이터가 없습니다.");
            httpStatus = HttpStatus.NOT_FOUND;
        } else {
            resultMap.put("success", true);
            resultMap.put("data", contentRecResList);
            resultMap.put("count", contentRecResList.size());
            httpStatus = HttpStatus.OK;
        }


        return new ResponseEntity<>(resultMap, httpStatus);
    }

    @GetMapping("/content/rec/{memberName}/{ContentRecId}")
    public ResponseEntity<?> getContentRec(@PathVariable("memberName") String memberName, @PathVariable("ContentRecId") Long contentRecId) {

        Map<String, Object> resultMap = new HashMap<>();
        HttpStatus httpStatus = null;
        resultMap.put("msg", "좋아요한 컨텐츠 문구/시나리오 목록 상세 보기 ");

        Member member = memberService.checkName(memberName);
        if (member == null) {
            resultMap.put("success", false);
            resultMap.put("msg", String.format("[%s]은/는 회원가입된 유저ID가 아닙니다.", memberName));
            httpStatus = HttpStatus.NOT_FOUND;
            return new ResponseEntity<>(resultMap, httpStatus);
        }

        ContentRec contentRec = contentService.getContentRec(contentRecId);
        if (contentRec == null) {
            resultMap.put("success", false);
            resultMap.put("msg", String.format("[%d]은/는 유효하지 않는 보관함ID입니다.", contentRecId));
            httpStatus = HttpStatus.NOT_FOUND;
            return new ResponseEntity<>(resultMap, httpStatus);
        }

        List<ContentDetailRes> contentDetailResList = myPageService.getContentDetailResList(member.getId(), contentRecId);

        if (contentDetailResList.size() == 0) {
            resultMap.put("success", false);
            resultMap.put("msg", "해당 데이터가 없습니다.");
            httpStatus = HttpStatus.NOT_FOUND;
        } else {
            resultMap.put("success", true);
            resultMap.put("data", contentDetailResList);
            resultMap.put("count", contentDetailResList.size());
            httpStatus = HttpStatus.OK;
        }


        return new ResponseEntity<>(resultMap, httpStatus);

    }

    @DeleteMapping("/content/rec/{memberName}/{ContentRecId}")
    public ResponseEntity<?> deleteContentRec(@PathVariable("memberName") String memberName, @PathVariable("ContentRecId") Long contentRecId) {
        Map<String, Object> resultMap = new HashMap<>();
        HttpStatus httpStatus = null;
        resultMap.put("msg", "좋아요한 컨텐츠 목록 삭제");

        Member member = memberService.checkName(memberName);
        if (member == null) {
            resultMap.put("success", false);
            resultMap.put("msg", String.format("[%s]은/는 회원가입된 유저ID가 아닙니다.", memberName));
            httpStatus = HttpStatus.NOT_FOUND;
            return new ResponseEntity<>(resultMap, httpStatus);

        }

        ContentRec contentRec = contentService.getContentRec(contentRecId);

        if (contentRec == null) {

            resultMap.put("success", false);
            resultMap.put("msg", String.format("[%d]은/는 잘못된 컨텐츠 추천 결과 id 입니다.", contentRecId));
            httpStatus = HttpStatus.NOT_FOUND;

        } else if (contentRec.getMember().getName().equals(memberName)) {

            myPageService.deleteContentRec(contentRec);

            resultMap.put("success", true);
            httpStatus = HttpStatus.OK;

        } else {

            resultMap.put("success", false);
            resultMap.put("msg", String.format("[%d]은/는 [%s]유저의 컨텐츠 추천 결과가 아닙니다.", contentRecId, memberName));
            httpStatus = HttpStatus.BAD_REQUEST;

        }

        resultMap.put("success", true);
        resultMap.put("data", String.format("[%d]보관함을 삭제하였습니다.", contentRecId));
        resultMap.put("count", 1);
        httpStatus = HttpStatus.OK;

        return new ResponseEntity<>(resultMap, httpStatus);
    }

    @DeleteMapping("/content/like/{memberName}/{ContentLikeId}")
    public ResponseEntity<?> deleteContentLike(@PathVariable("memberName") String memberName, @PathVariable("ContentLikeId") Long contentLikeId) {

        Map<String, Object> resultMap = new HashMap<>();
        HttpStatus httpStatus = null;
        resultMap.put("msg", "좋아요한 컨텐츠(문구/시나리오) 삭제");

        Member member = memberService.checkName(memberName);
        if (member == null) {
            resultMap.put("success", false);
            resultMap.put("msg", String.format("[%s]은/는 회원가입된 유저ID가 아닙니다.", memberName));
            httpStatus = HttpStatus.NOT_FOUND;
            return new ResponseEntity<>(resultMap, httpStatus);
        }

        ContentLike contentLike = contentService.getContentLike(contentLikeId);
        if (contentLike == null) {
            resultMap.put("success", false);
            resultMap.put("msg", String.format("[%d]은/는 유효하지 않는 컨텐츠 ID입니다.", contentLikeId));
            httpStatus = HttpStatus.NOT_FOUND;
            return new ResponseEntity<>(resultMap, httpStatus);
        }

        myPageService.deleteContentLike(contentLike);

        resultMap.put("success", true);
        resultMap.put("data", String.format("[%s] 컨텐츠를 삭제하였습니다.", contentLike.getTitle()));
        resultMap.put("count", 1);
        httpStatus = HttpStatus.OK;

        return new ResponseEntity<>(resultMap, httpStatus);
    }


}