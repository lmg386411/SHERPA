package com.ssafy.adrec.content.repository;

import com.ssafy.adrec.content.ContentLike;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;
import java.util.Optional;

public interface ContentLikeRepository extends JpaRepository<ContentLike, Long>   {

    List<ContentLike> findAllByContentRec_Id(Long contentRecId);

    Optional<ContentLike> findById(Long contentLikeId);
}
