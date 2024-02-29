package com.ssafy.adrec.content.repository;

import com.ssafy.adrec.content.ContentRec;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;
import java.util.Optional;

public interface ContentRecRepository extends JpaRepository<ContentRec, Long>   {

    List<ContentRec> findAllByMember_Id(Long id);

    Optional<ContentRec> findById(Long id);

    Optional<ContentRec> findByMember_IdAndId(Long memberId, Long contentRecId);
}
