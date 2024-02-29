package com.ssafy.adrec.keyword;

import com.ssafy.adrec.product.ProductSmall;
import lombok.*;

import javax.persistence.*;

@Entity
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
@Table(name = "adKeyword")
public class KeywordAd {
    @Id
    @GeneratedValue
    @Column(name = "id")
    private Long id;

    @Column(nullable = false)
    private String name;

    @Column(nullable = false)
    private int total;

    @ManyToOne
    @JoinColumn(name = "productSmall_id", referencedColumnName = "id")
    private ProductSmall productSmall;

    @Builder
    public KeywordAd(String name, int total, ProductSmall productSmall) {
        this.name = name;
        this.total = total;
        this.productSmall = productSmall;
    }
}
