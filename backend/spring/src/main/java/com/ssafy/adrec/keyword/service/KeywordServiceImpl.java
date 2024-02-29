package com.ssafy.adrec.keyword.service;

import com.ssafy.adrec.area.service.AreaService;
import com.ssafy.adrec.keyword.KeywordAd;
import com.ssafy.adrec.keyword.KeywordLike;
import com.ssafy.adrec.keyword.KeywordRec;
import com.ssafy.adrec.keyword.KeywordTrend;
import com.ssafy.adrec.keyword.repository.KeywordAdRepository;
import com.ssafy.adrec.keyword.repository.KeywordLikeRepository;
import com.ssafy.adrec.keyword.repository.KeywordRecRepository;
import com.ssafy.adrec.keyword.repository.KeywordTrendRepository;
import com.ssafy.adrec.keyword.response.KeywordRes;
import com.ssafy.adrec.member.Member;
import com.ssafy.adrec.member.service.MemberServiceImpl;
import com.ssafy.adrec.product.ProductSmall;
import lombok.RequiredArgsConstructor;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

@Service
@RequiredArgsConstructor
public class KeywordServiceImpl implements KeywordService {
    public static final Logger logger = LoggerFactory.getLogger(MemberServiceImpl.class);

    private final KeywordAdRepository keywordAdRepository;
    private final KeywordTrendRepository keywordTrendRepository;
    private final KeywordRecRepository keywordRecRepository;
    private final KeywordLikeRepository keywordLikeRepository;

    @Override
    public List<KeywordRes> getKeywordAdList(Long productSmallId){
        List<KeywordRes> list = new ArrayList<>();

        List<KeywordAd> keywordAdList = keywordAdRepository.findAllByProductSmall_Id(productSmallId);
        for(KeywordAd keywordAd : keywordAdList){
            list.add(new KeywordRes(keywordAd.getName(), keywordAd.getTotal()));
        }

        return list;
    }

    @Override
    public List<KeywordRes> getKeywordTrendList(){
        List<KeywordRes> list = new ArrayList<>();

        List<KeywordTrend> keywordTrendList = keywordTrendRepository.findAll();
        for(KeywordTrend keywordTrend : keywordTrendList){
            list.add(new KeywordRes(keywordTrend.getName(), keywordTrend.getTotal()));
        }

        return list;
    }

    @Override
    public KeywordRec getKeywordRec(Long keywordRecId){

        Optional<KeywordRec> opKeywordRec = keywordRecRepository.findById(keywordRecId);
        return opKeywordRec.orElse(null);

    }

    @Override
    public KeywordRec saveKeywordRec(Member member, ProductSmall productSmall){
        LocalDateTime currentTime = LocalDateTime.now();
        KeywordRec keywordRec = KeywordRec.builder()
                .recDate(currentTime)
                .member(member)
                .productSmall(productSmall)
                .build();

        KeywordRec sevedKeywordRec = keywordRecRepository.save(keywordRec);
        return sevedKeywordRec;
    }

    @Override
    public KeywordLike saveKeywordLike(String keyword, KeywordRec keywordRec){
        KeywordLike keywordLike = KeywordLike.builder()
                .keyword(keyword)
                .keywordRec(keywordRec)
                .build();
        KeywordLike savedkeywordLike = keywordLikeRepository.save(keywordLike);
        return savedkeywordLike;
    }

    @Override
    public KeywordLike getKeywordLike(Long keywordLikeId){

        Optional<KeywordLike> keywordLike = keywordLikeRepository.findById(keywordLikeId);
        return keywordLike.orElse(null);

    }


}
