package com.ssafy.adrec.content.repository;

import com.ssafy.adrec.content.ContentKeyword;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface ContentKeywordRepository extends JpaRepository<ContentKeyword, Long>   {

    List<ContentKeyword> findAllByContentRec_Id(Long id);
}
