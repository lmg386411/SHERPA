package com.ssafy.adrec.content.service;

import com.ssafy.adrec.content.ContentKeyword;
import com.ssafy.adrec.content.ContentLike;
import com.ssafy.adrec.content.ContentRec;
import com.ssafy.adrec.content.request.ContentRecListReq;
import com.ssafy.adrec.media.MediaSub;
import com.ssafy.adrec.media.MediaType;
import com.ssafy.adrec.member.Member;
import com.ssafy.adrec.product.ProductSmall;

import java.util.List;

public interface ContentService {
    ContentRec saveContentRec(ProductSmall productSmall, Member member, MediaType mediaType, MediaSub mediaSub, Long mediaTypeId);

    ContentKeyword saveContentKeyword(ContentRec contentRec, List<String> keywordList);

    ContentLike saveContentLike(ContentRec contentRec, List<ContentRecListReq> contentList);

    ContentRec getContentRec(Long contentRecId);

    ContentLike getContentLike(Long contentLikeId);
}
