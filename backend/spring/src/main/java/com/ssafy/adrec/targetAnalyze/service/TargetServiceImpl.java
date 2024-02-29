package com.ssafy.adrec.targetAnalyze.service;

import com.ssafy.adrec.area.repository.DongRepository;
import com.ssafy.adrec.member.service.MemberServiceImpl;
import com.ssafy.adrec.product.repository.ProductSmallRepository;
import com.ssafy.adrec.targetAnalyze.repository.TargetRepository;
import com.ssafy.adrec.targetAnalyze.request.TargetReq;
import com.ssafy.adrec.targetAnalyze.response.TargetAgeGetRes;
import com.ssafy.adrec.targetAnalyze.response.TargetGenderGetRes;
import lombok.RequiredArgsConstructor;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Service;

import java.util.*;

@Service
@RequiredArgsConstructor
public class TargetServiceImpl implements TargetService{

    public static final Logger logger = LoggerFactory.getLogger(MemberServiceImpl.class);

    private final TargetRepository targetRepository;
    private final ProductSmallRepository productSmallRepository;

    @Override
    public List<TargetGenderGetRes> getTargetGenderList(TargetReq targetReq){
        List<TargetGenderGetRes> list = new ArrayList<>();

        // sigunguId와 productSmallId가 일치하는 사람 인원 총 수
        Optional<Long> sumTotalOptional = targetRepository.sumTotalByDongIdInAndProductSmallId(targetReq.getSigunguId(), targetReq.getProductSmallId());

        if (sumTotalOptional.isPresent()) {
            Long sumTotal = sumTotalOptional.get();
            // 결과를 사용하는 코드
            // + gender 0인 사람의 총 수 / gender 1인 사람의 총 수 => 비율 Response에 담아주기
            Optional<Long> sumTotalWomenOptional = targetRepository.sumTotalByDongIdInAndProductSmallIdAndGender(targetReq.getSigunguId(), targetReq.getProductSmallId(), false);

            Long sumTotalWomen = 0L;
            if (sumTotalWomenOptional.isPresent()) {
                sumTotalWomen = sumTotalWomenOptional.get();
            }

            int valueWomen = Math.round((float) sumTotalWomen /sumTotal * 100);
            int valueMen = Math.round((float) (sumTotal-sumTotalWomen) / sumTotal * 100);
            list.add(new TargetGenderGetRes("0", String.valueOf(valueWomen)));
            list.add(new TargetGenderGetRes("1", String.valueOf(valueMen)));

        } else {
            // 결과가 없을 때 처리
            boolean dummy = true;

            List<Long> productSmallIds = productSmallRepository.findIdsByProductSmallId(targetReq.getProductSmallId());
            for (Long productSmallId : productSmallIds) {
                Optional<Long> sumTotalOtherOptional = targetRepository.sumTotalByDongIdInAndProductSmallId(targetReq.getSigunguId(), productSmallId);

                if (sumTotalOtherOptional.isPresent()) {
                    Long sumTotal = sumTotalOtherOptional.get();
                    // 결과를 사용하는 코드
                    // + gender 0인 사람의 총 수 / gender 1인 사람의 총 수 => 비율 Response에 담아주기
                    Optional<Long> sumTotalWomenOptional = targetRepository.sumTotalByDongIdInAndProductSmallIdAndGender(targetReq.getSigunguId(), productSmallId, false);
                    Long sumTotalWomen = 0L;
                    if (sumTotalWomenOptional.isPresent()) {
                        sumTotalWomen = sumTotalOtherOptional.get();
                    }

                    int valueWomen = Math.round((float) sumTotalWomen /sumTotal * 100);
                    int valueMen = Math.round((float) (sumTotal-sumTotalWomen) / sumTotal * 100);
                    list.add(new TargetGenderGetRes("0", String.valueOf(valueWomen)));
                    list.add(new TargetGenderGetRes("1", String.valueOf(valueMen)));

                    dummy = false;
                    break;
                }
            }

            if (dummy) {
                // 모든 반복문에서 Optional이 없을 때 출력
                list.add(new TargetGenderGetRes("0", "45"));
                list.add(new TargetGenderGetRes("1", "45"));
            }
        }


        return list;
    }

    @Override
    public List<TargetAgeGetRes> getTargetAgeList(TargetReq targetReq){
        List<TargetAgeGetRes> list = new ArrayList<>();

        // sigunguId와 productSmallId가 일치하는 사람 인원 총 수
        Optional<Long> sumTotalOptional = targetRepository.sumTotalByDongIdInAndProductSmallId(targetReq.getSigunguId(), targetReq.getProductSmallId());


        if (sumTotalOptional.isPresent()) {
            Long sumTotal = sumTotalOptional.get();
            // 결과를 사용하는 코드
            // + age 10인 사람 총 수 age 20인 사람 총 수 age 30인 사람 총 수 40,50,60,70인 사람 total => 비율
            List<Integer> ages = Arrays.asList(10, 20, 30, 40, 50, 60, 70);
            Map<Integer, Long> ageTotalMap = new HashMap<>();

            for (Integer age : ages) {
                Optional<Long> sumAgeTotalOptional = targetRepository.sumTotalByDongIdInAndProductSmallIdAndAge(targetReq.getSigunguId(), targetReq.getProductSmallId(), age);
                Long sumAgeTotal = sumAgeTotalOptional.orElse(0L);
                ageTotalMap.put(age, sumAgeTotal);
            }

            ageTotalMap.forEach((age, sumAgeTotal) -> {
                int valueAge = Math.round((float) sumAgeTotal / sumTotal * 100);
                list.add(new TargetAgeGetRes(String.valueOf(age), String.valueOf(valueAge)));
            });

        } else {
            // 결과가 없을 때 처리
            boolean dummy = true;

            List<Long> productSmallIds = productSmallRepository.findIdsByProductSmallId(targetReq.getProductSmallId());
            for (Long productSmallId : productSmallIds) {

                Optional<Long> sumTotalOtherOptional = targetRepository.sumTotalByDongIdInAndProductSmallId(targetReq.getSigunguId(), productSmallId);

                if (sumTotalOtherOptional.isPresent()) {

                    Long sumTotal = sumTotalOtherOptional.get();
                    // 결과를 사용하는 코드
                    // + age 10인 사람 총 수 age 20인 사람 총 수 age 30인 사람 총 수 40,50,60,70인 사람 total => 비율
                    List<Integer> ages = Arrays.asList(10, 20, 30, 40, 50, 60, 70);
                    Map<Integer, Long> ageTotalMap = new HashMap<>();

                    for (Integer age : ages) {
                        Optional<Long> sumAgeTotalOptional = targetRepository.sumTotalByDongIdInAndProductSmallIdAndAge(targetReq.getSigunguId(), productSmallId, age);
                        Long sumAgeTotal = sumAgeTotalOptional.orElse(0L);
                        ageTotalMap.put(age, sumAgeTotal);
                    }

                    ageTotalMap.forEach((age, sumAgeTotal) -> {
                        int valueAge = Math.round((float) sumAgeTotal / sumTotal * 100);
                        list.add(new TargetAgeGetRes(String.valueOf(age), String.valueOf(valueAge)));
                    });

                    dummy = false;
                    break;
                }
            }

            if (dummy) {
                // 모든 반복문에서 Optional이 없을 때 출력
                list.add(new TargetAgeGetRes("10", "15"));
                list.add(new TargetAgeGetRes("20", "20"));
                list.add(new TargetAgeGetRes("30", "15"));
                list.add(new TargetAgeGetRes("40", "15"));
                list.add(new TargetAgeGetRes("50", "15"));
                list.add(new TargetAgeGetRes("60", "10"));
                list.add(new TargetAgeGetRes("70", "10"));
            }
        }

        return list;
    }
}
