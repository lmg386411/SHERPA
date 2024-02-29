package com.ssafy.adrec.area;
import lombok.*;

import javax.persistence.*;

@Entity
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
@Table(name = "dong")
public class Dong {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id")
    private Long id;

    @Column
    private String name;

    @ManyToOne
    @JoinColumn(name = "sigungu_id", referencedColumnName = "id")
    private Sigungu sigungu;

}
