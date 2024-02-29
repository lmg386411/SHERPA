package com.ssafy.adrec.area.service;

import com.ssafy.adrec.area.AreaType;
import com.ssafy.adrec.area.Dong;
import com.ssafy.adrec.area.Sido;
import com.ssafy.adrec.area.Sigungu;
import com.ssafy.adrec.area.repository.DongRepository;
import com.ssafy.adrec.area.repository.SidoRepository;
import com.ssafy.adrec.area.repository.SigunguRepository;
import com.ssafy.adrec.area.response.AreaGetRes;
import com.ssafy.adrec.member.service.MemberServiceImpl;
import com.ssafy.adrec.product.ProductSmall;
import com.ssafy.adrec.product.response.ProductGetRes;
import lombok.RequiredArgsConstructor;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

@Service
@RequiredArgsConstructor
public class AreaServiceImpl implements AreaService{
    public static final Logger logger = LoggerFactory.getLogger(MemberServiceImpl.class);

    private final SidoRepository sidoRepository;
    private final SigunguRepository sigunguRepository;
    private final DongRepository dongRepository;

    @Override
    public List<AreaGetRes> getList(AreaType areaType, Long id){
        List<AreaGetRes> list = new ArrayList<>();

        switch (areaType) {
            case SIDO:
                List<Sido> sidoList = sidoRepository.findAll();
                for (Sido sido : sidoList) {
                    list.add(new AreaGetRes(sido.getId(), sido.getName()));
                }
                break;
            case SIGUNGU:
                List<Sigungu> sigunguList = sigunguRepository.findAllBySido_Id(id);
                for (Sigungu sigungu : sigunguList) {
                    list.add(new AreaGetRes(sigungu.getId(), sigungu.getName()));
                }
                break;
            case DONG:
                List<Dong> dongList = dongRepository.findAllBySigungu_Id(id);
                for (Dong dong : dongList) {
                    list.add(new AreaGetRes(dong.getId(), dong.getName()));
                }
                break;
        }

        return list;

    }

    @Override
    public Sigungu getSigungu (Long id){
        Optional<Sigungu> sigungu = sigunguRepository.findById(id);
        if(sigungu.isEmpty()){
            return null;
        }

        return sigungu.get();
    }
}
