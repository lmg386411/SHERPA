package com.ssafy.adrec.targetAnalyze;

import com.ssafy.adrec.area.Dong;
import com.ssafy.adrec.product.ProductSmall;
import lombok.*;

import javax.persistence.*;

@Entity
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
@Table(name = "target")
public class Target {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id")
    private Long id;

    @Column
    private boolean gender;

    @Column
    private int age;

    @Column
    private int total;

    @ManyToOne
    @JoinColumn(name = "productSmall_id", referencedColumnName = "id")
    private ProductSmall productSmall;

    @ManyToOne
    @JoinColumn(name = "dong_id", referencedColumnName = "id")
    private Dong dong;

}
