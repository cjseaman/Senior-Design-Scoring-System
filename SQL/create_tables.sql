create table judge (
	judge_email char(128) default '' not null,
	judge_name char(128) default '' not NULL,
	assigned_session_id int default 0 not null,
	primary key (judge_email)
);

create table review_session (
	session_id int default 0 not null,
	session_name char(128) default '' not null,
	session_location char(128) default '' not null,
	primary key (session_id)
);

create table project (
	project_id int default 0 not null,
	assigned_session_id int default 0 not null,
	project_name char(128) default '' not null,
	group_members text not null,
	project_desc text not null,
	average_score int default 0 not null,
	primary key (project_id)
);

create table scoringsystem_projecteval (
	project_id int default 0,
	judge_email char (128) default '',
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
	primary key(project_id)
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
