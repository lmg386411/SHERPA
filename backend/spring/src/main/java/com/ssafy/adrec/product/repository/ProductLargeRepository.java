package com.ssafy.adrec.product.repository;

import com.ssafy.adrec.product.ProductLarge;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface ProductLargeRepository extends JpaRepository<ProductLarge, Long> {

    List<ProductLarge> findAll();

}
