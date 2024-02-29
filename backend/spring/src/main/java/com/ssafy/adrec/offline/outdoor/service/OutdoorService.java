package com.ssafy.adrec.offline.outdoor.service;

import com.ssafy.adrec.offline.outdoor.request.TargetReq;
import com.ssafy.adrec.offline.outdoor.response.BannerRes;
import com.ssafy.adrec.offline.outdoor.response.OutdoorRes;
import com.ssafy.adrec.offline.outdoor.response.SubwayRes;

import java.util.List;

public interface OutdoorService {
    List<OutdoorRes> getAreaList(TargetReq areaReq);
    List<OutdoorRes> getBusList(TargetReq targetReq);
    // 지하철 Top5
    List<SubwayRes> getSubwayList();
    // 현수막 장소
    List<BannerRes> getBannerList(TargetReq targetReq);
    boolean isGwangju(Long sigunguId);
}
