package com.ssafy.adrec.myPage;

import com.ssafy.adrec.area.Sigungu;
import com.ssafy.adrec.keyword.KeywordRec;
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
@Table(name = "mediaRec")
public class MediaRec {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id")
    private Long id;

    @Column(nullable = false)
    private int budget;

    @Column(nullable = false, name = "is_on_off")
    private boolean isOnOff;

    @Column(nullable = false, name = "red_Date")
    private LocalDateTime recDate;

    @ManyToOne
    @JoinColumn(name = "member_id", referencedColumnName = "id")
    private Member member;

    @ManyToOne
    @JoinColumn(name = "sigungu_id", referencedColumnName = "id")
    private Sigungu sigungu;

    @ManyToOne
    @JoinColumn(name = "productSmall_id", referencedColumnName = "id")
    private ProductSmall productSmall;

    @ManyToOne
    @JoinColumn(name = "mediaType_id", referencedColumnName = "id")
    private MediaType mediaType;


}
