package com.ssafy.adrec.media.repository;

import com.ssafy.adrec.media.MediaSub;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;
import java.util.Optional;

public interface MediaSubRepository extends JpaRepository<MediaSub, Long> {
    List<MediaSub> findAllByMediaType_Id(Long mediaTypeid);

    Optional<MediaSub> findById(Long id);
}
