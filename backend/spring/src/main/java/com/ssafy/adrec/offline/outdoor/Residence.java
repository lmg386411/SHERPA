package com.ssafy.adrec.offline.outdoor;

import com.ssafy.adrec.area.Dong;
import lombok.*;

import javax.persistence.*;

@Entity
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
@Table(name = "residence")
public class Residence {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id")
    private Long id;

    @Column(nullable = false)
    private boolean gender;


    @Column(nullable = false)
    private int age;


    @Column(nullable = false)
    private int total;

    @ManyToOne
    @JoinColumn(name = "dong_id", referencedColumnName = "id")
    private Dong dong;

    @Builder
    public Residence(boolean gender, int age, int total, Dong dong) {
        this.gender = gender;
        this.age = age;
        this.total = total;
        this.dong = dong;
    }
}
