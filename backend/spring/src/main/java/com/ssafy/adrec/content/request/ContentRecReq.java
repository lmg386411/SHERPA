package com.ssafy.adrec.content.request;

import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.web.bind.annotation.GetMapping;

import java.util.List;

@Data
@NoArgsConstructor
public class ContentRecReq {

    String memberName;
    Long productSmallId;
    Long mediaTypeId;
    Long mediaSubId;
    List<String> keywordList;
    List<ContentRecListReq> contentList;

}
