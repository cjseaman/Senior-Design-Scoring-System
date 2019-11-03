create database scoring_system;
create table judge (
	judge_email char(128) default '' not null,
	judge_name char(128) default '' not NULL,
    assigned_session_id int unsigned default 0 not null,
	primary key (judge_email)
);

create table review_session (
	session_id int unsigned default 0 not null,
    session_name char(128) default '' not null,
    session_location char(128) default '' not null,
    primary key (session_id)
);

create table project (
	project_id int unsigned default 0 not null,
    assigned_session_id int unsigned default 0 not null,
    project_name char(128) default '' not null,
    group_members text (512) not null,
    project_desc text(1024) not null,
	average_score int unsigned default 0 not null,
	primary key (project_id)
);

create table submission (
	project_id int unsigned default 0 not null,
    judge_email char (128) default '' not null,
    dp_a float default 0 not null,
    dp_b float default 0 not null,
    dp_c float default 0 not null,
    dp_d float default 0 not null,
    dp_e float default 0 not null,
    dp_f float default 0 not null,
    dp_g float default 0 not null,
    dp_h float default 0 not null,
    p_a float default 0 not null,
    p_b float default 0 not null,
    p_c float default 0 not null,
    p_d float default 0 not null,
	econ_consideration boolean default false not null,
    envi_consideration boolean default false not null,
    sust_consideration boolean default false not null,
    manu_consideration boolean default false not null,
    ethi_consideration boolean default false not null,
    heal_consideration boolean default false not null,
    soci_consideration boolean default false not null,
    poli_consideration boolean default false not null,
    comments text (2048) not null,
    primary key(project_id, judge_email)
);

create table experience (
	responder_email char(128) default '' not null,
	bioe boolean default false not null,
    civl boolean default false not null,
    coen boolean default false not null,
    elen boolean default false not null,
    mech boolean default false not null,
    inte boolean default false not null,
    q1 int unsigned default 0 not null,
    q2 int unsigned default 0 not null,
    q3 int unsigned default 0 not null,
    q4 int unsigned default 0 not null,
    q5 int unsigned default 0 not null,
    q6 int unsigned default 0 not null,
    q7 int unsigned default 0 not null,
    q8 int unsigned default 0 not null,
    q9 int unsigned default 0 not null,
    q10 int unsigned default 0 not null,
    q11 int unsigned default 0 not null,
    q12 int unsigned default 0 not null,
    comments text (2048) not null,
    primary key (responder_email)
);


