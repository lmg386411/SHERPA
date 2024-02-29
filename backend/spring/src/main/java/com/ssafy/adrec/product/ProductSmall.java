package com.ssafy.adrec.product;

import lombok.*;

import javax.persistence.*;

@Entity
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
@Table(name = "productSmall")
public class ProductSmall {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id")
    private Long id;

    @Column
    private String small;

    @Column
    private int code;

    @ManyToOne
    @JoinColumn(name = "productMedium_id", referencedColumnName = "id")
    private ProductMedium productMedium;

    @Builder
    public ProductSmall(String small, int code, ProductMedium productMedium) {
        this.small = small;
        this.code = code;
        this.productMedium = productMedium;
    }
}
