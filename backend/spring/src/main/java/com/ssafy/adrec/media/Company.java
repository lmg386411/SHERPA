package com.ssafy.adrec.media;

import lombok.*;

import javax.persistence.*;

@Entity
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
@Table(name = "company")
public class Company {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id")
    private Long id;

    @Column
    String name;

    @Column
    String url;

    @Column(nullable = true)
    String img;

    @ManyToOne
    @JoinColumn(name = "mediaType_id", referencedColumnName = "id")
    private MediaType mediaType;

    @ManyToOne(optional = true)
    @JoinColumn(name = "mediaSub_id", referencedColumnName = "id")
    private MediaSub mediaSub;
}
