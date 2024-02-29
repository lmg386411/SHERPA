package com.ssafy.adrec.myPage.service;

import com.ssafy.adrec.area.Sigungu;
import com.ssafy.adrec.content.ContentKeyword;
import com.ssafy.adrec.content.ContentLike;
import com.ssafy.adrec.content.ContentRec;
import com.ssafy.adrec.keyword.KeywordLike;
import com.ssafy.adrec.keyword.KeywordRec;
import com.ssafy.adrec.media.MediaSub;
import com.ssafy.adrec.media.MediaType;
import com.ssafy.adrec.member.Member;
import com.ssafy.adrec.myPage.MediaRec;
import com.ssafy.adrec.myPage.request.MediaRecReq;
import com.ssafy.adrec.myPage.request.MyPageModifyPutReq;
import com.ssafy.adrec.myPage.request.MyProductModifyPutReq;
import com.ssafy.adrec.myPage.response.*;
import com.ssafy.adrec.product.ProductSmall;

import java.util.List;

public interface MyPageService {

    List<KeywordRecRes> getKeywordRecList(Long memberId);

    void deleteKeywordRec(KeywordRec keywordRec);

    void deleteKeywordLike(KeywordLike keywordLike);

    List<KeywordIdKeyword> getKeywordIdKeywordList(Long keywordRecId);

    // 회원 정보 수정
    Member modifyMember(MyPageModifyPutReq myPageModifyPutReq);

    // 품목 정보 수정
    Member modifyProduct(MyProductModifyPutReq myProductModifyPutReq);

    MediaRec saveMediaRec(MediaRecReq mediaRecReq, ProductSmall productSmall, Sigungu sigungu, Member member, MediaType mediaType);

    List<MediaRecRes> getMediaRecList(Long id);

    MediaRec getMediaRec(Long id);

    void deleteMediaRec(MediaRec mediaRec);

    MediaType getMediaType(Long id);
    MediaSub getMediaSub(Long id);

    List<String> getKeywordList(Member member, ProductSmall productSmall);

    List<ContentRecRes> getContentRecList(Long id);

    List<ContentDetailRes> getContentDetailResList(Long id, Long contentRecId);

    void deleteContentRec(ContentRec contentRec);

    void deleteContentKeyword(ContentKeyword contentKeyword);

    void deleteContentLike(ContentLike contentLike);
}
