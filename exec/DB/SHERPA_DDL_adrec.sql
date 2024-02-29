create table if not exists adrec.communityAge
(
    id    bigint auto_increment
        primary key,
    age   int         not null,
    name  varchar(80) not null,
    total int         not null,
    year  int         not null
);

create table if not exists adrec.communityArea
(
    id    bigint auto_increment
        primary key,
    area  varchar(80) not null,
    name  varchar(80) not null,
    total int         not null,
    year  int         not null
);

create table if not exists adrec.communityGender
(
    id     bigint auto_increment
        primary key,
    gender tinyint default 0 not null comment '0:여성, 1:남성',
    name   varchar(80)       not null,
    total  int               not null,
    year   int               not null
);

create table if not exists adrec.communityTheme
(
    id          bigint auto_increment
        primary key,
    theme       varchar(80)  not null,
    theme_sub   varchar(80)  not null,
    name_author varchar(80)  not null,
    url         text         not null,
    img         text         not null,
    title_post  varchar(255) null,
    text        text         null
);

create table if not exists adrec.hibernate_sequence
(
    next_val bigint null
);

create table if not exists adrec.mediaType
(
    id     bigint auto_increment
        primary key,
    large  varchar(80) not null,
    medium varchar(80) not null
);

create table if not exists adrec.mediaSub
(
    id           bigint auto_increment
        primary key,
    small        varchar(80) not null,
    mediaType_id bigint      not null,
    constraint FK_mediaType_TO_mediaSub_1
        foreign key (mediaType_id) references adrec.mediaType (id)
);

create table if not exists adrec.budget
(
    id           bigint auto_increment
        primary key,
    min_budget   int    not null,
    max_budget   int    not null,
    mediaType_id bigint not null,
    mediaSub_id  bigint null,
    constraint FK_mediaSub_TO_budget_1
        foreign key (mediaSub_id) references adrec.mediaSub (id),
    constraint FK_mediaType_TO_budget_1
        foreign key (mediaType_id) references adrec.mediaType (id)
);

create table if not exists adrec.company
(
    id           bigint auto_increment
        primary key,
    name         varchar(80) not null,
    url          text        not null,
    img          text        null,
    mediaType_id bigint      not null,
    mediaSub_id  bigint      null,
    constraint FK_mediaSub_TO_company_1
        foreign key (mediaSub_id) references adrec.mediaSub (id),
    constraint FK_mediaType_TO_company_1
        foreign key (mediaType_id) references adrec.mediaType (id)
);

create table if not exists adrec.mediaLikeAge
(
    id           bigint auto_increment
        primary key,
    age          int    not null,
    total        int    not null,
    mediaSub_id  bigint null,
    mediaType_id bigint not null,
    constraint FK_mediaSub_TO_mediaLikeAge_1
        foreign key (mediaSub_id) references adrec.mediaSub (id),
    constraint FK_mediaType_TO_mediaLikeAge_1
        foreign key (mediaType_id) references adrec.mediaType (id)
);

create table if not exists adrec.mediaLikeArea
(
    id           bigint auto_increment
        primary key,
    area         varchar(80) not null,
    total        int         not null,
    mediaSub_id  bigint      null,
    mediaType_id bigint      not null,
    constraint FK_mediaSub_TO_mediaLikeArea_1
        foreign key (mediaSub_id) references adrec.mediaSub (id),
    constraint FK_mediaType_TO_mediaLikeArea_1
        foreign key (mediaType_id) references adrec.mediaType (id)
);

create table if not exists adrec.mediaLikeGender
(
    id           bigint auto_increment
        primary key,
    gender       tinyint default 0 not null comment '0:여성, 1:남성',
    total        int               not null,
    mediaSub_id  bigint            null,
    mediaType_id bigint            not null,
    constraint FK_mediaSub_TO_mediaLikeGender_1
        foreign key (mediaSub_id) references adrec.mediaSub (id),
    constraint FK_mediaType_TO_mediaLikeGender_1
        foreign key (mediaType_id) references adrec.mediaType (id)
);

create table if not exists adrec.newsAge
(
    id    int auto_increment
        primary key,
    age   int         not null,
    name  varchar(80) not null,
    total int         not null
);

create table if not exists adrec.newsArea
(
    id    int auto_increment
        primary key,
    area  varchar(80) not null,
    name  varchar(80) not null,
    total int         not null
);

create table if not exists adrec.newsGender
(
    id     int auto_increment
        primary key,
    gender tinyint default 0 not null comment '0:여성, 1:남성',
    name   varchar(80)       not null,
    total  int               not null
);

create table if not exists adrec.newsThemeAge
(
    id    int auto_increment
        primary key,
    age   int         not null,
    theme varchar(80) not null,
    total int         not null
);

create table if not exists adrec.newsThemeArea
(
    id    int auto_increment
        primary key,
    area  varchar(80) not null,
    theme varchar(80) not null,
    total int         not null
);

create table if not exists adrec.newsThemeGender
(
    id     int auto_increment
        primary key,
    gender tinyint default 0 not null comment '0:여성, 1:남성',
    theme  varchar(80)       not null,
    total  int               not null
);

create table if not exists adrec.productLarge
(
    id    bigint auto_increment
        primary key,
    large varchar(255) null
);

create table if not exists adrec.productMedium
(
    id              bigint auto_increment
        primary key,
    medium          varchar(255) null,
    productLarge_id bigint       null,
    constraint FKhmgsxm2fijv5c8nlxwcyyayla
        foreign key (productLarge_id) references adrec.productLarge (id)
);

create table if not exists adrec.productSmall
(
    id               bigint auto_increment
        primary key,
    code             int          null,
    small            varchar(255) null,
    productMedium_id bigint       null,
    constraint FKrgffctm40732dcnj4kvgws1m5
        foreign key (productMedium_id) references adrec.productMedium (id)
);

create table if not exists adrec.adKeyword
(
    id              bigint auto_increment
        primary key,
    name            varchar(80) not null,
    total           int         not null,
    productSmall_id bigint      not null,
    constraint FKc4utwv5cdbjy1mtbyj4w8cf7l
        foreign key (productSmall_id) references adrec.productSmall (id)
);

create table if not exists adrec.member
(
    id              bigint auto_increment
        primary key,
    email           varchar(255) not null,
    img             varchar(255) null,
    name            varchar(255) not null,
    pwd             varchar(255) not null,
    productSmall_id bigint       null,
    constraint FKs41rg3c6b71q63t5j15x6hb0r
        foreign key (productSmall_id) references adrec.productSmall (id)
);

create table if not exists adrec.contentRec
(
    id              bigint auto_increment
        primary key,
    rec_date        date   not null,
    productSmall_id bigint not null,
    member_id       bigint not null,
    mediaType_id    bigint not null,
    mediaSub_id     bigint null,
    constraint FK_mediaSub_TO_contentRec_1
        foreign key (mediaSub_id) references adrec.mediaSub (id),
    constraint FK_mediaType_TO_contentRec_1
        foreign key (mediaType_id) references adrec.mediaType (id),
    constraint FK_member_TO_contentRec_1
        foreign key (member_id) references adrec.member (id),
    constraint FK_productSmall_TO_contentRec_1
        foreign key (productSmall_id) references adrec.productSmall (id)
);

create table if not exists adrec.contentKeyword
(
    id            bigint auto_increment
        primary key,
    keyword       varchar(80) not null,
    contentRec_id bigint      not null,
    constraint FK_contentRec_TO_contentKeyword_1
        foreign key (contentRec_id) references adrec.contentRec (id)
);

create table if not exists adrec.contentLike
(
    id            bigint auto_increment
        primary key,
    title         text   not null,
    content       text   null,
    contentRec_id bigint not null,
    constraint FK_contentRec_TO_contentLike_1
        foreign key (contentRec_id) references adrec.contentRec (id)
);

create table if not exists adrec.keywordRec
(
    id              bigint auto_increment
        primary key,
    recDate         datetime(6) not null,
    member_id       bigint      null,
    productSmall_id bigint      null,
    constraint FKgpldh8dspjlu7eiuxhhss9c0d
        foreign key (member_id) references adrec.member (id),
    constraint FKmuwaui047kdof71112dg9hkln
        foreign key (productSmall_id) references adrec.productSmall (id)
);

create table if not exists adrec.keywordLike
(
    id            bigint auto_increment
        primary key,
    keyword       varchar(255) not null,
    keywordRec_id bigint       null,
    constraint FK36bhu6imqxkw4nfv3xmu83a8v
        foreign key (keywordRec_id) references adrec.keywordRec (id)
);

create table if not exists adrec.productMedia
(
    id              bigint auto_increment
        primary key,
    total           int    not null,
    mediaSub_id     bigint null,
    mediaType_id    bigint not null,
    productSmall_id bigint not null,
    like_per        int    not null,
    constraint FK_mediaSub_TO_productMedia_1
        foreign key (mediaSub_id) references adrec.mediaSub (id),
    constraint FK_mediaType_TO_productMedia_1
        foreign key (mediaType_id) references adrec.mediaType (id),
    constraint FK_productSmall_TO_productMedia_1
        foreign key (productSmall_id) references adrec.productSmall (id)
);

create table if not exists adrec.radioAge
(
    id    bigint auto_increment
        primary key,
    age   int         not null,
    total int         not null,
    genre varchar(80) not null
);

create table if not exists adrec.radioArea
(
    id    bigint auto_increment
        primary key,
    area  varchar(80) not null,
    total int         not null,
    genre varchar(80) not null
);

create table if not exists adrec.radioGender
(
    id     bigint auto_increment
        primary key,
    gender tinyint default 0 not null comment '0:여성, 1:남성',
    total  int               not null,
    genre  varchar(80)       not null
);

create table if not exists adrec.radioTime
(
    id         bigint auto_increment
        primary key,
    age        int               not null,
    is_weekday tinyint default 0 not null comment '0:주중, 1:주말',
    time       int               not null,
    total      int               not null
);

create table if not exists adrec.sido
(
    id   bigint auto_increment
        primary key,
    name varchar(80) not null
);

create table if not exists adrec.sigungu
(
    id      bigint auto_increment
        primary key,
    name    varchar(80) not null,
    sido_id bigint      not null,
    constraint FKer985a6prrkijv3rc5d551qc8
        foreign key (sido_id) references adrec.sido (id)
);

create table if not exists adrec.dong
(
    id         bigint auto_increment
        primary key,
    name       varchar(80) not null,
    sigungu_id bigint      not null,
    constraint FKaemqdr7ll5c80g4cdxn4aqc8t
        foreign key (sigungu_id) references adrec.sigungu (id)
);

create table if not exists adrec.banner
(
    id      bigint auto_increment
        primary key,
    name    varchar(80)  not null,
    address varchar(255) not null,
    dong_id bigint       not null,
    constraint FKntpo44bqoyidulgdy51q0rwo5
        foreign key (dong_id) references adrec.dong (id)
);

create table if not exists adrec.bus
(
    id      bigint auto_increment
        primary key,
    name    varchar(80) not null,
    total   int         not null,
    dong_id bigint      not null,
    constraint FK_dong_TO_bus_1
        foreign key (dong_id) references adrec.dong (id)
);

create table if not exists adrec.mediaRec
(
    id              bigint auto_increment
        primary key,
    budget          int         not null,
    is_on_off       tinyint     not null,
    red_Date        datetime(6) not null,
    member_id       bigint      not null,
    productSmall_id bigint      not null,
    sigungu_id      bigint      not null,
    mediaType_id    bigint      not null,
    mediaSub_id     bigint      null,
    constraint FK1qev7krbrbdqkmwm1216krulp
        foreign key (mediaType_id) references adrec.mediaType (id),
    constraint FKcap0xxbf4hpj48m9p0iyj09h1
        foreign key (sigungu_id) references adrec.sigungu (id),
    constraint FKgyyawycp0vj6x9g2cvpdh2gid
        foreign key (mediaSub_id) references adrec.mediaSub (id),
    constraint FKhkj34urpnqrs2620f39jr4mme
        foreign key (member_id) references adrec.member (id),
    constraint FKlh4p2idq8fi4o7a26s1cgcr71
        foreign key (productSmall_id) references adrec.productSmall (id)
);

create table if not exists adrec.residence
(
    id      bigint auto_increment
        primary key,
    gender  tinyint default 0 not null comment '0:여성, 1:남성',
    age     int               not null,
    total   int               not null,
    dong_id bigint            not null,
    constraint FKlyk1ok48lnt0jgfvcn4s57sr8
        foreign key (dong_id) references adrec.dong (id)
);

create table if not exists adrec.snsAge
(
    id    bigint auto_increment
        primary key,
    age   int         not null,
    name  varchar(80) not null,
    total int         not null,
    year  int         not null
);

create table if not exists adrec.snsArea
(
    id    bigint auto_increment
        primary key,
    area  varchar(80) not null,
    name  varchar(80) not null,
    total int         not null,
    year  int         not null
);

create table if not exists adrec.snsGender
(
    id     bigint auto_increment
        primary key,
    gender tinyint default 0 not null comment '0:여성, 1:남성',
    name   varchar(80)       not null,
    total  int               not null,
    year   int               not null
);

create table if not exists adrec.subway
(
    id    bigint auto_increment
        primary key,
    name  varchar(80) not null,
    total int         not null
);

create table if not exists adrec.target
(
    id              bigint auto_increment
        primary key,
    gender          tinyint default 0 not null comment '0:여성, 1:남성',
    age             int               not null,
    total           int               not null,
    productSmall_id bigint            not null,
    dong_id         bigint            not null,
    constraint FK_dong_TO_target_1
        foreign key (dong_id) references adrec.dong (id),
    constraint FK_productSmall_TO_target_1
        foreign key (productSmall_id) references adrec.productSmall (id)
);

create table if not exists adrec.tvAge
(
    id      bigint auto_increment
        primary key,
    age     int               not null,
    genre   varchar(80)       not null,
    is_free tinyint default 0 not null comment '0:지상파, 1:유료',
    total   int               not null
);

create table if not exists adrec.tvArea
(
    id      bigint auto_increment
        primary key,
    area    varchar(80)       not null,
    genre   varchar(80)       not null,
    is_free tinyint default 0 not null comment '0:지상파, 1:유료',
    total   int               not null
);

create table if not exists adrec.tvGender
(
    id      bigint auto_increment
        primary key,
    gender  tinyint default 0 not null comment '0:여성, 1:남성',
    genre   varchar(80)       not null,
    is_free tinyint default 0 not null comment '0:지상파, 1:유료',
    total   int               not null
);

create table if not exists adrec.tvTime
(
    id         bigint auto_increment
        primary key,
    age        int               not null,
    is_weekday tinyint default 0 not null comment '0:주중, 1:주말',
    time       int               not null,
    total      int               not null
);

create table if not exists adrec.youtubeKeyword
(
    id    int auto_increment
        primary key,
    name  varchar(80) not null,
    total int         not null
);

