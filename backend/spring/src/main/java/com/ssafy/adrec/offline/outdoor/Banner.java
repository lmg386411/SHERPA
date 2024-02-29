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
@Table(name = "banner")
public class Banner {

    @Id
    @GeneratedValue
    @Column(name = "id")
    private Long id;

    @Column(nullable = false)
    private String name;

    @Column(nullable = false)
    private String address;

    @ManyToOne
    @JoinColumn(name = "dong_id", referencedColumnName = "id")
    private Dong dong;

    public Banner(String name, String address, Dong dong) {
        this.name = name;
        this.address = address;
        this.dong = dong;
    }

}
