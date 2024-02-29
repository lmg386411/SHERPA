package com.ssafy.adrec.keyword.service;

import com.ssafy.adrec.keyword.KeywordLike;
import com.ssafy.adrec.keyword.KeywordRec;
//import com.ssafy.adrec.keyword.response.KeywordRecRes;
import com.ssafy.adrec.keyword.response.KeywordRes;
import com.ssafy.adrec.member.Member;
import com.ssafy.adrec.product.ProductSmall;

import java.util.List;


public interface KeywordService {
    List<KeywordRes> getKeywordAdList(Long productSmallId);

    List<KeywordRes> getKeywordTrendList();

    KeywordRec getKeywordRec(Long keywordRecId);

    KeywordRec saveKeywordRec(Member member, ProductSmall productSmall);

    KeywordLike saveKeywordLike(String keyword, KeywordRec keywordRec);

    KeywordLike getKeywordLike (Long keywordLikeId);


}
