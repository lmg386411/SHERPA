package com.ssafy.adrec.media;


import lombok.*;

import javax.persistence.*;

@Entity
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
@Table(name = "mediaSub")
public class MediaSub {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id")
    private Long id;

    @Column
    private String small;

    @ManyToOne
    @JoinColumn(name = "mediaType_id", referencedColumnName = "id")
    private MediaType mediaType;
}
