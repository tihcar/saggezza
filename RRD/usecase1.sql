use warehouse saggezza_wh_2;
use database demo_db;
use schema public;

insert into test values('B');
insert into test values('C');
insert into test values('D');
insert into test values('E');

update test
set A = 'A'
where A = 'z';
