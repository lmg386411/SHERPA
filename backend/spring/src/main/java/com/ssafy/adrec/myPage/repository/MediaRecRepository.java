package com.ssafy.adrec.myPage.repository;

import com.ssafy.adrec.myPage.MediaRec;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface MediaRecRepository  extends JpaRepository<MediaRec, Long> {
    List<MediaRec> findAllByMember_Id(Long id);
}
