package com.ssafy.adrec.keyword;

import com.ssafy.adrec.member.Member;
import com.ssafy.adrec.product.ProductSmall;
import lombok.*;

import javax.persistence.*;
import java.time.LocalDateTime;
import java.util.Date;

@Entity
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
@Table(name = "keywordRec")
public class KeywordRec {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id")
    private Long id;

    @Column(nullable = false)
    private LocalDateTime recDate;

    @ManyToOne
    @JoinColumn(name = "member_id", referencedColumnName = "id")
    private Member member;

    @ManyToOne
    @JoinColumn(name = "productSmall_id", referencedColumnName = "id")
    private ProductSmall productSmall;

    @Builder
    public KeywordRec(LocalDateTime recDate, Member member, ProductSmall productSmall) {
        this.recDate = recDate;
        this.member = member;
        this.productSmall = productSmall;
    }

}
