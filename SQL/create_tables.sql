create table scoringsystem_session (
	id serial,
	session_name char(128) default '',
	session_location char(128) default '',
	primary key (id)
);

create table scoringsystem_judge (
  judge_id serial,
	judge_email char(128) default '',
	judge_name char(128) default '',
	session_id int,
	password text,
	primary key (judge_id),
  foreign key (session_id) references scoringsystem_session(id)
);

create table scoringsystem_project (
  id serial,
	session_id int,
	project_name char(128) default '' ,
	group_members text ,
	project_desc text ,
	average_score int default 0 ,
	primary key (id),
  foreign key (session_id) references scoringsystem_session(id)
);

create table scoringsystem_projecteval (
	project_id int default 0,
	judge_email char (128) default '',
  session_id int,
	dp_a float default 0,
	dp_b float default 0,
	dp_c float default 0,
	dp_d float default 0,
	dp_e float default 0,
	dp_f float default 0,
	dp_g float default 0,
	dp_h float default 0,
	p_a float default 0,
	p_b float default 0,
	p_c float default 0,
	p_d float default 0,
	econ_consideration boolean default false,
	envi_consideration boolean default false,
	sust_consideration boolean default false,
	manu_consideration boolean default false,
	ethi_consideration boolean default false,
	heal_consideration boolean default false,
	soci_consideration boolean default false,
	poli_consideration boolean default false,
	comments char (512) default '',
	primary key(project_id),
  foreign key (session_id) references scoringsystem_session(id)
);

create table scoringsystem_judgeeval (
	judge_email char (128) default '',
  discipline char (5) default '',
	q1 int default 0,
	q2 int default 0,
	q3 int default 0,
	q4 int default 0,
	q5 int default 0,
	q6 int default 0,
	q7 int default 0,
	q8 int default 0,
	q9 int default 0,
	q10 int default 0,
	q11 int default 0,
	q12 int default 0,
	comments char (512) default '',
	primary key (judge_email)
);
