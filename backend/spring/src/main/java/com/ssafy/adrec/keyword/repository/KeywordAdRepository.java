package com.ssafy.adrec.keyword.repository;


import com.ssafy.adrec.keyword.KeywordAd;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface KeywordAdRepository extends JpaRepository<KeywordAd, Long> {
    List<KeywordAd> findAllByProductSmall_Id(Long productSmallId);
}
