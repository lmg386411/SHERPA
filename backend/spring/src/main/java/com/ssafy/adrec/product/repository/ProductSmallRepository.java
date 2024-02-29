package com.ssafy.adrec.product.repository;

import com.ssafy.adrec.product.ProductSmall;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import java.util.List;
import java.util.Optional;

public interface ProductSmallRepository extends JpaRepository<ProductSmall, Long> {

    Optional<ProductSmall> findById(Long id);
    List<ProductSmall> findAllByProductMedium_Id(Long ProductMedium_Id);

    @Query("SELECT s.id FROM ProductSmall s " +
            "JOIN ProductMedium m ON s.productMedium.id = m.id " +
            "JOIN ProductLarge l ON m.productLarge.id = l.id " +
            "WHERE l.id = " +
            "(SELECT l.id FROM ProductSmall s2 " +
            "JOIN ProductMedium m2 ON s2.productMedium.id = m2.id " +
            "JOIN ProductLarge l ON m2.productLarge.id = l.id " +
            "WHERE s2.id = :productSmallId)")
    List<Long> findIdsByProductSmallId(@Param("productSmallId") Long productSmallId);
    
}
