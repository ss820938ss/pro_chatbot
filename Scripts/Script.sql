select user(), database();

grant all 
   on pro_chatbot.* 
   to 'user_pro_chatbot'@'localhost' identified by 'rootroot';

-- file 권한(backup, load) -- root만 권한 부여 가능
GRANT File 
   ON *.* 
   TO 'user_pro_chatbot'@'localhost';
  

CREATE SCHEMA pro_chatbot;
create database pro_chatbot;


  
DROP TABLE IF EXISTS pro_chatbot.cafe_member RESTRICT;

-- 회원
CREATE TABLE pro_chatbot.cafe_member (
	mem_no        INT          NOT NULL COMMENT '회원번호', -- 회원번호
	mem_email     VARCHAR(100) NOT NULL COMMENT '회원이메일', -- 회원이메일
	mem_passwd    CHAR(41)     NOT NULL COMMENT '비밀번호', -- 비밀번호
	mem_name      VARCHAR(100) NOT NULL COMMENT '이름', -- 이름
)
COMMENT '멤버';

-- 회원
ALTER TABLE pro_chatbot.cafe_member
	ADD CONSTRAINT PK_cafe_member -- 회원 기본키
		PRIMARY KEY (
			mem_no -- 회원번호
		);

-- 회원
select mem_no, mem_email, mem_passwd, mem_name from cafe_member;
insert into cafe_member values (null, 'test1@test.com', password(1234), '테스트1');	
	
	
	
DROP TABLE IF EXISTS pro_chatbot.cafe_menu RESTRICT;

-- 메뉴
CREATE TABLE pro_chatbot.cafe_menu (
	menu_no       INT          NOT NULL COMMENT '메뉴번호', -- 메뉴번호
	menu_name     VARCHAR(100) NOT NULL COMMENT '메뉴이름', -- 메뉴이름
	menu_price    INT     	   NOT NULL COMMENT '메뉴가격', -- 메뉴가격
	menu_kate 	  VARCHAR(100) NOT NULL COMMENT '메뉴종류', -- 메뉴종류
)
COMMENT '회원';

-- 메뉴
ALTER TABLE pro_chatbot.cafe_menu
	ADD CONSTRAINT PK_cafe_menu -- 회원 기본키
		PRIMARY KEY (
			men_no -- 회원번호
		);

-- 메뉴	
select menu_no, menu_name, menu_price, menu_kate from cafe_menu;
insert into cafe_menu values (null, '아메리카노', 2000, '커피');
insert into cafe_menu values (null, '카페라떼', 3000, '커피');
insert into cafe_menu values (null, '카라멜마끼아또', 4000, '커피');
insert into cafe_menu values (null, '에스프레소', 2000, '커피');
insert into cafe_menu values (null, '바닐라라떼', 3500, '커피');
insert into cafe_menu values (null, '딸기주스', 4000, '주스');
insert into cafe_menu values (null, '복숭아스무디', 4000, '주스');
insert into cafe_menu values (null, '캐모마일', 3000, '허브티');
insert into cafe_menu values (null, '라벤더', 3000, '허브티');
insert into cafe_menu values (null, '민트', 2000, '허브티');
