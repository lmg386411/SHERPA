package com.ssafy.adrec.product;

import lombok.*;

import javax.persistence.*;

@Entity
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
@Table(name = "productMedium")
public class ProductMedium {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id")
    private Long id;

    @Column
    private String medium;

    @ManyToOne
    @JoinColumn(name = "productLarge_id", referencedColumnName = "id")
    private ProductLarge productLarge;

}
