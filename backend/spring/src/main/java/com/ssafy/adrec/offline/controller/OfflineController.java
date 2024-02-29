package com.ssafy.adrec.offline.controller;

import com.ssafy.adrec.offline.outdoor.Subway;
import com.ssafy.adrec.offline.outdoor.request.TargetReq;
import com.ssafy.adrec.offline.outdoor.response.BannerRes;
import com.ssafy.adrec.offline.outdoor.response.OutdoorRes;
import com.ssafy.adrec.offline.outdoor.response.SubwayRes;
import com.ssafy.adrec.offline.outdoor.service.OutdoorService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@RestController
@RequiredArgsConstructor
@RequestMapping("/offline")
@CrossOrigin(origins = "*")
public class OfflineController {
    private final OutdoorService outdoorService;

    @PostMapping("/outdoor/area")
    public ResponseEntity<?> getAreaList(@RequestBody TargetReq areaReq){
        Map<String, Object> resultMap = new HashMap<>();
        HttpStatus httpStatus = null;
        List<OutdoorRes> list = new ArrayList<>();
        list = outdoorService.getAreaList(areaReq);

        resultMap.put("msg", "장소 리스트 조회");
        
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


        return new ResponseEntity<Map<String, Object>>(resultMap, httpStatus);
    }

    @PostMapping("/outdoor/bus")
    public ResponseEntity<?> getBusList(@RequestBody TargetReq targetReq){
        Map<String, Object> resultMap = new HashMap<>();
        HttpStatus httpStatus = null;

        if (outdoorService.isGwangju(targetReq.getSigunguId())){
            resultMap.put("success", false);
            resultMap.put("msg", "광주 지역만 정류장 정보가 제공됩니다.");
            httpStatus = HttpStatus.BAD_REQUEST;
            return new ResponseEntity<Map<String, Object>>(resultMap, httpStatus);
        }


        List<OutdoorRes> list = new ArrayList<>();
        list = outdoorService.getBusList(targetReq);

        resultMap.put("msg", "정류장 리스트 조회");

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

        return new ResponseEntity<Map<String, Object>>(resultMap, httpStatus);
    }

    @GetMapping("/outdoor/subway")
    public ResponseEntity<?> getSubwayList() {
        Map<String, Object> resultMap = new HashMap<>();
        HttpStatus httpStatus = null;

        List<SubwayRes> list;
        list = outdoorService.getSubwayList();

        resultMap.put("msg", "지하철역 Top5 조회");

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

        return new ResponseEntity<Map<String, Object>>(resultMap, httpStatus);
    }

    @PostMapping("/outdoor/banner")
    public ResponseEntity<?> getBannerList(@RequestBody TargetReq targetReq) {
        Map<String, Object> resultMap = new HashMap<>();
        HttpStatus httpStatus = null;

        List<BannerRes> list = outdoorService.getBannerList(targetReq);

        resultMap.put("msg", "현수막 장소 조회");

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

        return new ResponseEntity<Map<String, Object>>(resultMap, httpStatus);
    }

}
