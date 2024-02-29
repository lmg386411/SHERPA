package com.ssafy.adrec.offline.outdoor.repository;

import com.ssafy.adrec.offline.outdoor.Residence;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;

public interface ResidenceRepository extends JpaRepository<Residence, Long> {

    List<Residence> findAllByAgeAndGenderAndDong_Sigungu_Id(int age, boolean gender, Long sigunguId);
}
