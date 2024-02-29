use adrec;

delete from adrec.contentKeyword;
alter table adrec.contentKeyword auto_increment = 1;
delete from adrec.contentLike;
alter table adrec.contentLike auto_increment = 1;
delete from adrec.contentRec;
alter table adrec.contentRec auto_increment = 1;

-- 컨텐츠 추천 보관함 더미 데이터
INSERT INTO adrec.contentRec (rec_date, productSmall_id, member_id, mediaType_id, mediaSub_id) VALUES ( '2023-10-03', 2, 53, 3, null);
INSERT INTO adrec.contentRec ( rec_date, productSmall_id, member_id, mediaType_id, mediaSub_id) VALUES ( '2023-10-04', 2, 53, 5, null);
INSERT INTO adrec.contentRec (rec_date, productSmall_id, member_id, mediaType_id, mediaSub_id) VALUES ( '2023-10-04', 90, 53, 6, 3);
INSERT INTO adrec.contentRec (rec_date, productSmall_id, member_id, mediaType_id, mediaSub_id) VALUES ( '2023-10-04', 131, 53, 4, null);
INSERT INTO adrec.contentRec (rec_date, productSmall_id, member_id, mediaType_id, mediaSub_id) VALUES ( '2023-10-04', 123, 53, 2, null);

INSERT INTO adrec.contentKeyword (keyword, contentRec_id) VALUES ( '아름다운', 1);
INSERT INTO adrec.contentKeyword (keyword, contentRec_id) VALUES ( '단아한', 1);
INSERT INTO adrec.contentKeyword (keyword, contentRec_id) VALUES ( '한국', 2);
INSERT INTO adrec.contentKeyword (keyword, contentRec_id) VALUES ( '저렴한', 3);
INSERT INTO adrec.contentKeyword (keyword, contentRec_id) VALUES ( '가성비', 3);
INSERT INTO adrec.contentKeyword (keyword, contentRec_id) VALUES ( '친절한', 3);
INSERT INTO adrec.contentKeyword (keyword, contentRec_id) VALUES ( '편안한', 4);
INSERT INTO adrec.contentKeyword (keyword, contentRec_id) VALUES ( '대박', 4);
INSERT INTO adrec.contentKeyword (keyword, contentRec_id) VALUES ( '빠른', 5);
INSERT INTO adrec.contentKeyword (keyword, contentRec_id) VALUES ( '안전한', 5);
INSERT INTO adrec.contentKeyword (keyword, contentRec_id) VALUES ( '친절한', 5);
INSERT INTO adrec.contentKeyword (keyword, contentRec_id) VALUES ( '대박', 5);

INSERT INTO adrec.contentLike (title, content, contentRec_id) VALUES ( '아름다운 한복을 그대와 함께', '1. 아름다운 한복을 입고 걸어가는 사람이 있다.
2. 아름다운 노을이 지는 풍경이 배경에 있다.
3. 단아한 미소를 짓는 사람의 얼굴을 클로즈업한다.', 1);
INSERT INTO adrec.contentLike (title, content, contentRec_id) VALUES ( '단아한 한복을 입어보세요', '1. 단아한 한복을 입는 사람이 있다.
2. 여러 명의 사람들이 전부 다가온다.
3. 모두 어깨동무를 하면서 행복하게 웃는다.', 1);
INSERT INTO adrec.contentLike (title, content, contentRec_id) VALUES ( '아름다운 그대에게 단아한 그대에게', '1. 한옥이 있다.
2. 단아한 남자 한복을 입은 사람이 한옥의 마루에 앉아있다.
3. 그 남자는 부채질을 한다. 점점 얼굴로 클로즈업 된다.', 1);
INSERT INTO adrec.contentLike (title, content, contentRec_id) VALUES ( '한국적인 한복이 최고다', null, 2);
INSERT INTO adrec.contentLike (title, content, contentRec_id) VALUES ( '한국의 아름다움을 느껴보세요', null, 2);
INSERT INTO adrec.contentLike (title, content, contentRec_id) VALUES ( '한국의 것, 최고의 것, 한복', null, 2);
INSERT INTO adrec.contentLike (title, content, contentRec_id) VALUES ( '저렴한 가성비 마켓, 빙그레 마켓', null, 3);
INSERT INTO adrec.contentLike (title, content, contentRec_id) VALUES ( '친절한 비용, 친절한 직원이 함께합니다', null, 3);
INSERT INTO adrec.contentLike (title, content, contentRec_id) VALUES ( '대박! 편안한 스포츠 용품이 준비되어있습니다!!', '1. 한강 다리 아래에서 조깅하는 크루가 있다.
2. 시원한 바람을 맞으면서 조깅하는 사람을 클로즈업 한다.
3. 그 사람이 착용하고 있는 스포츠용품을 보여준다.
4. 로고를 함께 보여주면서 편안하다는 것을 강조한다.', 4);
INSERT INTO adrec.contentLike (title, content, contentRec_id) VALUES ( '빠르고 안전한 렌터카, 나이스 렌터카', null, 5);
INSERT INTO adrec.contentLike (title, content, contentRec_id) VALUES ( '안전한 보험 서비스가 완비된 나이스 렌터카로 오세요', null, 5);
INSERT INTO adrec.contentLike (title, content, contentRec_id) VALUES ( '친절한 직원이 도와드립니다. 나이스한 렌터카로 오세요', null, 5);
INSERT INTO adrec.contentLike (title, content, contentRec_id) VALUES ( '대박 안전한 나이스 렌터카', null, 5);
INSERT INTO adrec.contentLike (title, content, contentRec_id) VALUES ( '나이스 렌터카가 대박 안전하다', null, 5);
