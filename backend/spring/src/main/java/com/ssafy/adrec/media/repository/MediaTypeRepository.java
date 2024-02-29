package com.ssafy.adrec.media.repository;

import com.ssafy.adrec.media.MediaType;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;
import java.util.Optional;

public interface MediaTypeRepository extends JpaRepository<MediaType, Long> {
    List<MediaType> findAll();

    Optional<MediaType> findById(Long id);
}
