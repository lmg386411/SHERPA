package com.ssafy.adrec.offline.outdoor;

import lombok.*;

import javax.persistence.*;

@Entity
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
@Table(name = "subway")
public class Subway {

    @Id
    @GeneratedValue
    @Column(name = "id")
    private Long id;

    @Column(nullable = false)
    private String name;

    @Column(nullable = false)
    private int total;

    @Builder
    public Subway(String name, int total) {
        this.name = name;
        this.total = total;
    }

}
