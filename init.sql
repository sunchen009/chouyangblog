
#创建articles表，存储blog文章
CREATE TABLE articles(
	aid				INT		AUTO_INCREMENT PRIMARY KEY	,
	title 			VARCHAR(20) ,
	content 		TEXT		,	
	posttime		DATETIME	,
	classid			INT			,
	tags			VARCHAR(50)	,
	pv				INT			,
	commentnumber 	INT			);



CREATE TABLE comments(
	
	cid				INT 	AUTO_INCREMENT	PRIMARY KEY	,
	aid				INT 		,
	posttime		DATETIME	,
	content			TEXT		,
	email			VARCHAR(50)	,
	username		VARCHAR(20)	);


CREATE TABLE classes(
	classid   INT AUTO_INCREMENT PRIMARY KEY,
	classname VARCHAR(20) );


CREATE TABLE  `app_chouyangbox`.`admins` (
`uid` INT NOT NULL AUTO_INCREMENT ,
`username` VARCHAR( 20 ) NOT NULL ,
`userpass` VARCHAR( 100 ) NOT NULL ,
PRIMARY KEY (  `uid` )
) ;


CREATE TABLE  sessions ( 
session_id char(128) UNIQUE NOT NULL, 
atime timestamp NOT NULL default current_timestamp, 
data text 
); 