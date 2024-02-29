package com.ssafy.adrec.offline.outdoor.repository;

import com.ssafy.adrec.area.Dong;
import com.ssafy.adrec.offline.outdoor.Banner;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface BannerRepository extends JpaRepository<Banner, Long> {

    List<Banner> findAllByDong(Dong dong);
}
