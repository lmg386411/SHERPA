package com.ssafy.adrec.content;

import com.ssafy.adrec.media.MediaSub;
import com.ssafy.adrec.media.MediaType;
import com.ssafy.adrec.member.Member;
import com.ssafy.adrec.product.ProductSmall;
import lombok.*;

import javax.persistence.*;
import java.time.LocalDateTime;

@Entity
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
@Table(name = "contentRec")
public class ContentRec {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id")
    private Long id;

    @Column(nullable = false, name = "rec_date")
    private LocalDateTime recDate;

    @ManyToOne
    @JoinColumn(name = "productSmall_id", referencedColumnName = "id")
    private ProductSmall productSmall;

    @ManyToOne
    @JoinColumn(name = "member_id", referencedColumnName = "id")
    private Member member;

    @ManyToOne
    @JoinColumn(name = "mediaType_id", referencedColumnName = "id")
    private MediaType mediaType;

    @ManyToOne(optional = true)
    @JoinColumn(name = "mediaSub_id", referencedColumnName = "id")
    private MediaSub mediaSub;



}
