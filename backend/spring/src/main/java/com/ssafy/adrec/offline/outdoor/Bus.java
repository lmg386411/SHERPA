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
@Table(name = "bus")
public class Bus {

    @Id
    @GeneratedValue
    @Column(name = "id")
    private Long id;

    @Column(nullable = false)
    private String name;

    @Column(nullable = false)
    private int total;

    @ManyToOne
    @JoinColumn(name = "dong_id", referencedColumnName = "id")
    private Dong dong;

    @Builder
    public Bus(String name, int total, Dong dong) {
        this.name = name;
        this.total = total;
        this.dong = dong;
    }
}
