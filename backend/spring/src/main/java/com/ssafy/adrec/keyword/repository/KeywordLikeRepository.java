package com.ssafy.adrec.keyword.repository;

import com.ssafy.adrec.keyword.KeywordLike;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;
import java.util.Optional;

public interface KeywordLikeRepository extends JpaRepository<KeywordLike, Long> {

    List<KeywordLike> findAllByKeywordRecId(Long keywordRecId);
    Optional<KeywordLike> findById (Long keywordLikeId);
}
