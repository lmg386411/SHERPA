package com.ssafy.adrec.content.service;

import com.ssafy.adrec.content.ContentKeyword;
import com.ssafy.adrec.content.ContentLike;
import com.ssafy.adrec.content.ContentRec;
import com.ssafy.adrec.content.repository.ContentKeywordRepository;
import com.ssafy.adrec.content.repository.ContentLikeRepository;
import com.ssafy.adrec.content.repository.ContentRecRepository;
import com.ssafy.adrec.content.request.ContentRecListReq;
import com.ssafy.adrec.media.MediaSub;
import com.ssafy.adrec.media.MediaType;
import com.ssafy.adrec.member.Member;
import com.ssafy.adrec.member.repository.MemberRepository;
import com.ssafy.adrec.member.service.MemberServiceImpl;
import com.ssafy.adrec.product.ProductSmall;
import lombok.RequiredArgsConstructor;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;

@Service
@RequiredArgsConstructor
public class ContentServiceImpl implements ContentService {

    public static final Logger logger = LoggerFactory.getLogger(MemberServiceImpl.class);

    private final MemberRepository memberRepository;
    private final ContentRecRepository contentRecRepository;
    private final ContentKeywordRepository contentKeywordRepository;
    private final ContentLikeRepository contentLikeRepository;

    @Override
    public ContentRec saveContentRec(ProductSmall productSmall, Member member, MediaType mediaType, MediaSub mediaSub, Long mediaTypeId) {

        LocalDateTime currentTime = LocalDateTime.now();

        if (mediaTypeId == 6) {
            ContentRec contentRec = ContentRec.builder()
                    .recDate(currentTime)
                    .productSmall(productSmall)
                    .member(member)
                    .mediaType(mediaType)
                    .mediaSub(mediaSub)
                    .build();

            return contentRecRepository.save(contentRec);

        } else {
            ContentRec contentRec = ContentRec.builder()
                    .recDate(currentTime)
                    .productSmall(productSmall)
                    .member(member)
                    .mediaType(mediaType)
                    .build();

            return contentRecRepository.save(contentRec);
        }

    }

    @Override
    public ContentKeyword saveContentKeyword(ContentRec contentRec, List<String> keywordList) {

        ContentKeyword contentKeyword = null;
        for (String keyword : keywordList) {
            contentKeyword = ContentKeyword.builder()
                    .contentRec(contentRec)
                    .keyword(keyword)
                    .build();

            contentKeywordRepository.save(contentKeyword);
        }

        return contentKeyword;
    }

    @Override
    public ContentLike saveContentLike(ContentRec contentRec, List<ContentRecListReq> contentList) {

        ContentLike contentLike = null;
        for (ContentRecListReq contentRecListReq : contentList) {
            contentLike = ContentLike.builder()
                    .contentRec(contentRec)
                    .title(contentRecListReq.getTitle())
                    .content(contentRecListReq.getContent())
                    .build();

            contentLikeRepository.save(contentLike);
        }

        return contentLike;
    }

    @Override
    public ContentRec getContentRec(Long contentRecId){
        Optional<ContentRec> contentRec = contentRecRepository.findById(contentRecId);
        return contentRec.orElse(null);
    }

    @Override
    public ContentLike getContentLike(Long contentLikeId) {
        Optional<ContentLike> contentLike = contentLikeRepository.findById(contentLikeId);
        return contentLike.orElse(null);
    }


}
