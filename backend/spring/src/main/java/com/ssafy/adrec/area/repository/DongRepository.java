package com.ssafy.adrec.area.repository;

import com.ssafy.adrec.area.Dong;
import com.ssafy.adrec.area.Sigungu;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface DongRepository extends JpaRepository<Dong, Long> {
    List<Dong> findAllBySigungu_Id(Long sigunguId);
}
