package com.ssafy.adrec.member;

import com.ssafy.adrec.product.ProductSmall;
import lombok.*;

import javax.persistence.*;

@Entity
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
@Table(name = "member")
public class Member {

    @Id
    @GeneratedValue
    @Column(name = "id")
    private Long id;

    @Column(nullable = false)
    private String name;

    @Column(nullable = false)
    private String email;

    @Column(nullable = false)
    private String pwd;

    @Column
    private String img;

    @ManyToOne
    @JoinColumn(name = "productSmall_id", referencedColumnName = "id")
    private ProductSmall productSmall;

    @Builder
    public Member(String name, String email, String pwd, String img, ProductSmall productSmall) {
        this.name = name;
        this.email = email;
        this.pwd = pwd;
        this.img = img;
        this.productSmall = productSmall;
    }

}
