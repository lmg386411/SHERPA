package com.ssafy.adrec.media.controller;

import com.ssafy.adrec.media.MediaTypes;
import com.ssafy.adrec.media.response.CompanyGetRes;
import com.ssafy.adrec.media.response.MediaSubGetRes;
import com.ssafy.adrec.media.response.MediaTypeGetRes;
import com.ssafy.adrec.media.service.MediaService;
import com.ssafy.adrec.member.controller.MemberController;
import lombok.RequiredArgsConstructor;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.*;

@RestController
@RequiredArgsConstructor
@RequestMapping("/media")
@CrossOrigin(origins = "*")
public class MediaController {

    public static final Logger logger = LoggerFactory.getLogger(MemberController.class);

    private final MediaService mediaService;

    @GetMapping("/type/{type}/{id}")
    public ResponseEntity getMediaTypeList(@PathVariable("type") String type, @PathVariable("id") Long id){
        List<MediaTypeGetRes> mediaTypelist = new ArrayList<>();
        List<MediaSubGetRes> mediaSublist = new ArrayList<>();

        Map<String, Object> resultMap = new HashMap<>();
        HttpStatus httpStatus = null;

        switch (type){
            case "largeMedium":
                mediaTypelist = mediaService.getMediaTypeList(MediaTypes.MEDIATYPE, id);
                resultMap.put("msg", "매체유형 대분류, 중분류 조회");
                break;
            case "small":
                mediaSublist = mediaService.getMediaSubList(MediaTypes.MEDIASUB, id);
                resultMap.put("msg", "매체유형 소분류 조회");
                break;
        }

        switch (type){
            case "largeMedium":
                if (mediaTypelist.size() == 0) {
                    resultMap.put("success", false);
                    resultMap.put("msg", "해당 데이터가 없습니다.");
                    httpStatus = HttpStatus.NOT_FOUND;
                } else {
                    resultMap.put("success", true);
                    resultMap.put("data", mediaTypelist);
                    resultMap.put("count", mediaTypelist.size());
                    httpStatus = HttpStatus.OK;
                }
                break;
            case "small":
                if (mediaSublist.size() == 0) {
                    resultMap.put("success", false);
                    resultMap.put("msg", "해당 데이터가 없습니다.");
                    httpStatus = HttpStatus.NOT_FOUND;
                } else {
                    resultMap.put("success", true);
                    resultMap.put("data", mediaSublist);
                    resultMap.put("count", mediaSublist.size());
                    httpStatus = HttpStatus.OK;
                }
                break;
        }

        return new ResponseEntity<>(resultMap, httpStatus);
    }

    @GetMapping("/company/{mediaTypeId}")
    public ResponseEntity getCompanyList(@PathVariable("mediaTypeId") Long mediaTypeId,
                                         @RequestParam(value = "mediaSubId", required = false) Long mediaSubId) {
        List<CompanyGetRes> companylist = new ArrayList<>();

        Map<String, Object> resultMap = new HashMap<>();
        HttpStatus httpStatus = null;

        if (mediaSubId == null) {
            companylist = mediaService.getCompanyList(mediaTypeId, mediaSubId);
            resultMap.put("msg", "광고 제작사 조회");
        } else {
            companylist = mediaService.getCompanyList(mediaTypeId, mediaSubId);
            resultMap.put("msg", "옥외 광고 제작사 조회");
        }

        if (companylist.size() == 0) {
            resultMap.put("success", false);
            resultMap.put("msg", "해당 데이터가 없습니다.");
            httpStatus = HttpStatus.NOT_FOUND;
        } else {
            resultMap.put("success", true);
            resultMap.put("data", companylist);
            resultMap.put("count", companylist.size());
            httpStatus = HttpStatus.OK;
        }
        return new ResponseEntity<>(resultMap, httpStatus);
    }
}
