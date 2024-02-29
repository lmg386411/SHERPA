package com.ssafy.adrec.offline.outdoor.service;

import com.ssafy.adrec.area.Dong;
import com.ssafy.adrec.area.Sigungu;
import com.ssafy.adrec.area.repository.DongRepository;
import com.ssafy.adrec.area.repository.SigunguRepository;
import com.ssafy.adrec.member.service.MemberServiceImpl;
import com.ssafy.adrec.offline.outdoor.Banner;
import com.ssafy.adrec.offline.outdoor.Bus;
import com.ssafy.adrec.offline.outdoor.Residence;
import com.ssafy.adrec.offline.outdoor.Subway;
import com.ssafy.adrec.offline.outdoor.repository.BannerRepository;
import com.ssafy.adrec.offline.outdoor.repository.BusRepository;
import com.ssafy.adrec.offline.outdoor.repository.ResidenceRepository;
import com.ssafy.adrec.offline.outdoor.repository.SubwayRepository;
import com.ssafy.adrec.offline.outdoor.request.TargetReq;
import com.ssafy.adrec.offline.outdoor.response.BannerRes;
import com.ssafy.adrec.offline.outdoor.response.OutdoorRes;
import com.ssafy.adrec.offline.outdoor.response.SubwayRes;
import lombok.RequiredArgsConstructor;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Optional;

@Service
@RequiredArgsConstructor
public class OutdoorServiceImpl implements OutdoorService {

    public static final Logger logger = LoggerFactory.getLogger(MemberServiceImpl.class);

    private final BusRepository busRepository;
    private final SigunguRepository sigunguRepository;
    private final ResidenceRepository residenceRepository;
    private final DongRepository dongRepository;
    private final SubwayRepository subwayRepository;
    private final BannerRepository bannerRepository;

    @Override
    public List<OutdoorRes> getAreaList(TargetReq targetReq){
        List<OutdoorRes> list = new ArrayList<>();
        boolean gender = (targetReq.getGender()== 1) ? true : false;
        int age = targetReq.getAge();
        Long sigunguId = targetReq.getSigunguId();


        List<Residence> residenceList = residenceRepository.findAllByAgeAndGenderAndDong_Sigungu_Id(age,gender,sigunguId);

        int allTotar = residenceList.stream()
                .mapToInt(Residence::getTotal)
                .sum();

        residenceList.sort(Comparator.comparingInt(Residence::getTotal).reversed());

        List<Residence> toplist = new ArrayList<>();
        int listSize = targetReq.getListSize();
        if (residenceList.size() <= listSize) {
            toplist = residenceList;
        }
        else{
            toplist = residenceList.subList(0, Math.min(listSize, residenceList.size()));
        }

        for(Residence residence : toplist){
            double d =(double)residence.getTotal()/allTotar;
            double ratio = d*100;

            OutdoorRes outdoorResDto = OutdoorRes.builder()
                    .type(residence.getDong().getName())
                    .total(residence.getTotal())
                    .ratio(Math.round(ratio * 100.0) / 100.0)
                    .build();
            list.add(outdoorResDto);
        }

        return list;
    }

    @Override
    public List<OutdoorRes> getBusList(TargetReq targetReq){
        List<OutdoorRes> list = new ArrayList<>();

        boolean gender = (targetReq.getGender()== 1) ? true : false;
        int age = targetReq.getAge();
        Long sigunguId = targetReq.getSigunguId();

        List<Residence> residenceList = residenceRepository.findAllByAgeAndGenderAndDong_Sigungu_Id(age,gender,sigunguId);
        Optional<Residence> residenceWithMaxTotal = residenceList.stream()
                .max(Comparator.comparingInt(Residence::getTotal));

        Dong dong = new Dong();
        if (residenceWithMaxTotal.isPresent()) {
            Residence residence = residenceWithMaxTotal.get();
            dong = residence.getDong();

        } else {
            return list;
        }

        List<Bus> busList = busRepository.findAllByDong(dong);
        int allTotar = busList.stream()
                .mapToInt(Bus::getTotal)
                .sum();

        busList.sort(Comparator.comparingInt(Bus::getTotal).reversed());

        List<Bus> toplist = new ArrayList<>();
        int listSize = targetReq.getListSize();
        if (busList.size() <= listSize) {
            toplist = busList;
        }
        else{
            toplist = busList.subList(0, Math.min(listSize, busList.size()));
        }

        for(Bus bus : toplist){
            double d =(double)bus.getTotal()/allTotar;
            double ratio = d*100;

            OutdoorRes outdoorResDto = OutdoorRes.builder()
                    .type(bus.getName())
                    .total(bus.getTotal())
                    .ratio(Math.round(ratio * 100.0) / 100.0)
                    .build();
            list.add(outdoorResDto);
        }

        return list;
    }

    @Override
    public List<SubwayRes> getSubwayList() {
        Optional<List<Subway>> optionalSubwayAllList = subwayRepository.findAllBy();

        int total = 0;
        if (optionalSubwayAllList.isPresent()) {
            List<Subway> list = optionalSubwayAllList.get();

            for(Subway subway : list) {
                total += subway.getTotal();
            }
        }

        List<SubwayRes> subwayResList = new ArrayList<>();
        Optional<List<Subway>> optionalSubwayList = subwayRepository.findTop5ByOrderByTotalDesc();
        if (optionalSubwayList.isPresent()) {
            List<Subway> list = optionalSubwayList.get();
            for (int i = 0; i < list.size(); i++) {
                Subway subway = list.get(i);
                SubwayRes subwayRes = new SubwayRes(i + 1, subway.getName(), Math.round((long) subway.getTotal() * 100 / total));
                subwayResList.add(subwayRes);
            }
        }

        return subwayResList;
    }

    @Override
    public List<BannerRes> getBannerList(TargetReq targetReq) {
        boolean gender = (targetReq.getGender()== 1) ? true : false;
        int age = targetReq.getAge();
        Long sigunguId = targetReq.getSigunguId();

        List<Residence> residenceList = residenceRepository.findAllByAgeAndGenderAndDong_Sigungu_Id(age,gender,sigunguId);
        Optional<Residence> residenceWithMaxTotal = residenceList.stream()
                .max(Comparator.comparingInt(Residence::getTotal));

        Dong dong = residenceWithMaxTotal.get().getDong();
        logger.debug("동 이름={}", residenceWithMaxTotal.get().getDong().getName());

        List<Banner> bannerList = bannerRepository.findAllByDong(dong);
        List<BannerRes> bannerResList = new ArrayList<>();
        for (int i = 0; i < bannerList.size(); i++) {
            Banner banner = bannerList.get(i);
            BannerRes bannerRes = BannerRes.builder()
                    .no(i + 1)
                    .address(banner.getAddress())
                    .name(banner.getName())
                    .build();

            bannerResList.add(bannerRes);
        }

        return bannerResList;
    }

    @Override
    public boolean isGwangju(Long sigunguId){
        boolean result = true;

        Optional<Sigungu> sigungu = sigunguRepository.findById(sigunguId);

        if (sigungu.isEmpty()){
            return result;
        }
        if (sigungu.get().getSido().getName().equals("광주")){
            result = false;
        }
        return result;
    }

}
