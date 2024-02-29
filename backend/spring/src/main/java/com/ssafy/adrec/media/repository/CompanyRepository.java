package com.ssafy.adrec.media.repository;

import com.ssafy.adrec.media.Company;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface CompanyRepository extends JpaRepository<Company, Long> {

    List<Company> findAllByMediaType_Id(Long mediaTypeId);

    List<Company> findAllByMediaType_IdAndMediaSub_Id(Long mediaTypeId, Long mediaSubId);
}
