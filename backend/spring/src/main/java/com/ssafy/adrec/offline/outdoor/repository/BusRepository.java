package com.ssafy.adrec.offline.outdoor.repository;

import com.ssafy.adrec.area.Dong;
import com.ssafy.adrec.offline.outdoor.Bus;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface BusRepository extends JpaRepository<Bus, Long> {

    List<Bus> findAllByDong(Dong dong);

}
