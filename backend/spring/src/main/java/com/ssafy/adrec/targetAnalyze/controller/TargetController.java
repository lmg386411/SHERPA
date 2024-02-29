package com.ssafy.adrec.targetAnalyze.controller;

import com.ssafy.adrec.member.controller.MemberController;
import com.ssafy.adrec.targetAnalyze.request.TargetReq;
import com.ssafy.adrec.targetAnalyze.response.TargetAgeGetRes;
import com.ssafy.adrec.targetAnalyze.response.TargetGenderGetRes;
import com.ssafy.adrec.targetAnalyze.service.TargetService;
import lombok.RequiredArgsConstructor;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.*;

@RestController
@RequiredArgsConstructor
@RequestMapping("/target")
@CrossOrigin(origins = "*")
public class TargetController {

    public static final Logger logger = LoggerFactory.getLogger(MemberController.class);

    private final TargetService targetService;

    @PostMapping
    public ResponseEntity<?> target(@RequestBody TargetReq targetReq) {
        List<TargetGenderGetRes> genderList = new ArrayList<>();
        List<TargetAgeGetRes> ageList = new ArrayList<>();

        List<TargetGenderGetRes> sortedGenderList = new ArrayList<>();
        List<TargetAgeGetRes> sortedAgeList = new ArrayList<>();

        Map<String, Object> resultMap = new HashMap<>();
        HttpStatus httpStatus = null;

        genderList = targetService.getTargetGenderList(targetReq);
        ageList = targetService.getTargetAgeList(targetReq);
        sortedGenderList = targetService.getTargetGenderList(targetReq);
        sortedAgeList = targetService.getTargetAgeList(targetReq);

        genderList.sort(Comparator.comparingInt(item -> Integer.parseInt(item.getGender())));
        ageList.sort(Comparator.comparingInt(item -> Integer.parseInt(item.getAge())));

        Map<String, Object> dataMap = new HashMap<>();
        dataMap.put("gender", genderList);
        dataMap.put("age", ageList);

        // 추천
        Map<String, Object> recommendMap = new HashMap<>();

        sortedGenderList.sort(Comparator.comparingInt(item -> Integer.parseInt(item.getValue())));
        Collections.reverse(sortedGenderList);
        if (!sortedGenderList.isEmpty()) {
            TargetGenderGetRes maxGender = sortedGenderList.get(0);

            if ( maxGender.getGender().equals("0") ){
                recommendMap.put("gender", false); // 여성
            }else{
                recommendMap.put("gender", true); // 남성
            }

        }

        sortedAgeList.sort(Comparator.comparingInt(item -> Integer.parseInt(item.getValue())));
        Collections.reverse(sortedAgeList);
        if (!sortedAgeList.isEmpty()) {
            TargetAgeGetRes maxAge = sortedAgeList.get(0);

            switch (maxAge.getAge()) {
                case "10":
                    recommendMap.put("age", 10);
                    break;
                case "20":
                    recommendMap.put("age", 20);
                    break;
                case "30":
                    recommendMap.put("age", 30);
                    break;
                case "40":
                    recommendMap.put("age", 40);
                    break;
                case "50":
                    recommendMap.put("age", 50);
                    break;
                case "60":
                    recommendMap.put("age", 60);
                    break;
                default:
                    recommendMap.put("age", 70);
                    break;
            }
        }
        dataMap.put("recommend", recommendMap);

        if (genderList.size() == 0 || ageList.size() == 0){
            resultMap.put("success", false);
            resultMap.put("msg", "해당 데이터가 없습니다.");
            httpStatus = HttpStatus.NOT_FOUND;
        } else{
            resultMap.put("success", true);
            resultMap.put("data", dataMap);
            resultMap.put("count", dataMap.size());
            resultMap.put("msg", "데이터를 성공적으로 불러왔습니다.");
            httpStatus = HttpStatus.OK;
        }

        return new ResponseEntity<>(resultMap, httpStatus);
    }


}