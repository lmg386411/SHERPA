package com.ssafy.adrec.targetAnalyze.repository;

import com.ssafy.adrec.targetAnalyze.Target;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import java.util.List;
import java.util.Optional;

public interface TargetRepository extends JpaRepository<Target, Long> {
//    List<Target> findAll();

    @Query("SELECT SUM(t.total) FROM Target t WHERE t.dong.id IN (SELECT d.id FROM Dong d WHERE d.sigungu.id = :sigunguId) AND t.productSmall.id = :productSmallId")
    Optional<Long> sumTotalByDongIdInAndProductSmallId(@Param("sigunguId") Long sigunguId, @Param("productSmallId") Long productSmallId);
//    Optional<Long> sumTotalByDongIdInAndProductSmallId(List<Long> dongIds, Long productSmallId);

    @Query("SELECT SUM(t.total) FROM Target t WHERE t.dong.id IN (SELECT d.id FROM Dong d WHERE d.sigungu.id = :sigunguId) AND t.productSmall.id = :productSmallId And t.gender = :gender")
    Optional<Long> sumTotalByDongIdInAndProductSmallIdAndGender(@Param("sigunguId") Long sigunguId, @Param("productSmallId") Long productSmallId, @Param("gender") boolean gender);
//    Optional<Long> sumTotalByDongIdInAndProductSmallIdAndGender(List<Long> dongIds, Long productSmallId, boolean gender);

//    Optional<Long> sumTotalByDongIdInAndProductSmallIdAndAge(List<Long> dongIds, Long productSmallId, int age);
    @Query("SELECT SUM(t.total) FROM Target t WHERE t.dong.id IN (SELECT d.id FROM Dong d WHERE d.sigungu.id = :sigunguId) AND t.productSmall.id = :productSmallId And t.age = :age")
    Optional<Long> sumTotalByDongIdInAndProductSmallIdAndAge(@Param("sigunguId") Long sigunguId, @Param("productSmallId") Long productSmallId, @Param("age") int age);

}
