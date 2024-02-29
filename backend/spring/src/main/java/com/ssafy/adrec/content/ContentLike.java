package com.ssafy.adrec.content;

import com.ssafy.adrec.keyword.KeywordRec;
import lombok.*;

import javax.persistence.*;

@Entity
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
@Table(name = "contentLike")
public class ContentLike {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id")
    private Long id;

    @Column(nullable = false)
    private String title;

    @Column(nullable = true)
    private String content;

    @ManyToOne
    @JoinColumn(name = "contentRec_id", referencedColumnName = "id")
    private ContentRec contentRec;
}
