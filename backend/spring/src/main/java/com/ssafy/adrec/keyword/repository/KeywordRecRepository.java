package com.ssafy.adrec.keyword.repository;

import com.ssafy.adrec.keyword.KeywordRec;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;
import java.util.Optional;

public interface KeywordRecRepository  extends JpaRepository<KeywordRec, Long> {

    Optional<KeywordRec> findById(Long keywordRecId);

    List<KeywordRec>findAllBymember_Id(Long memberId);

    List<KeywordRec>findAllByMember_IdAndProductSmallId(Long memberId,Long ProductSmallId);

}
