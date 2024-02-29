package com.ssafy.adrec.offline.outdoor.repository;

import com.ssafy.adrec.offline.outdoor.Subway;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;
import java.util.Optional;

public interface SubwayRepository extends JpaRepository<Subway, Long> {

    Optional<List<Subway>> findTop5ByOrderByTotalDesc();
    Optional<List<Subway>> findAllBy();

}
