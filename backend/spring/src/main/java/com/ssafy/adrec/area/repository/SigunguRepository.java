package com.ssafy.adrec.area.repository;

import com.ssafy.adrec.area.Sigungu;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface SigunguRepository extends JpaRepository<Sigungu, Long> {
    List<Sigungu> findAllBySido_Id(Long sidoId);
}
