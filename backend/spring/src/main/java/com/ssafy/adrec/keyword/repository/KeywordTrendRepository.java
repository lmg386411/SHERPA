package com.ssafy.adrec.keyword.repository;

import com.ssafy.adrec.keyword.KeywordTrend;
import org.springframework.data.jpa.repository.JpaRepository;

public interface KeywordTrendRepository  extends JpaRepository<KeywordTrend, Long> {
}
