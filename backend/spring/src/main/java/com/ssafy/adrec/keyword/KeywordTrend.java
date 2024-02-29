package com.ssafy.adrec.keyword;

import lombok.*;

import javax.persistence.*;

@Entity
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
@Table(name = "youtubeKeyword")
public class KeywordTrend {
    @Id
    @GeneratedValue
    @Column(name = "id")
    private Long id;

    @Column(nullable = false)
    private String name;

    @Column(nullable = false)
    private int total;

    @Builder
    public KeywordTrend(String name, int total) {
        this.name = name;
        this.total = total;
    }


}
