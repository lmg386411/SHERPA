package com.ssafy.adrec.area.repository;

import com.ssafy.adrec.area.Sido;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface SidoRepository extends JpaRepository<Sido, Long>  {
    List<Sido> findAll();
}
