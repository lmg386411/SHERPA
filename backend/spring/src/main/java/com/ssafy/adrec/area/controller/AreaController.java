package com.ssafy.adrec.area.controller;

import com.ssafy.adrec.area.AreaType;
import com.ssafy.adrec.area.response.AreaGetRes;
import com.ssafy.adrec.area.service.AreaService;
import com.ssafy.adrec.member.controller.MemberController;
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
@RequestMapping("/area")
@CrossOrigin(origins = "*")
public class AreaController {
    public static final Logger logger = LoggerFactory.getLogger(MemberController.class);

    private final AreaService areaService;

    @GetMapping("/{type}/{id}")
    public ResponseEntity<?> getAreaList(@PathVariable("type") String type, @PathVariable("id") Long id) {
        List<AreaGetRes> list = new ArrayList<>();

        Map<String, Object> resultMap = new HashMap<>();
        HttpStatus httpStatus = null;

        switch (type) {
            case "sido":
                list = areaService.getList(AreaType.SIDO, id);
                resultMap.put("msg", "시도 리스트 조회");
                break;
            case "sigungu":
                list = areaService.getList(AreaType.SIGUNGU, id);
                resultMap.put("msg", "시군구 리스트 조회");
                break;
            case "dong":
                list = areaService.getList(AreaType.DONG, id);
                resultMap.put("msg", "동 리스트 조회");
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



}
