package com.ssafy.adrec.area;

import lombok.*;

import javax.persistence.*;

@Entity
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
@Table(name = "sigungu")
public class Sigungu {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id")
    private Long id;

    @Column
    private String name;

    @ManyToOne
    @JoinColumn(name = "sido_id", referencedColumnName = "id")
    private Sido sido;
}
