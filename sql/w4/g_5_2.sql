create database adventureworkslt;

create table tab
(
    index int not null primary key GENERATED ALWAYS AS IDENTITY,
    a int not null,
    n int not null
);

Delete from tab where a = 9;
Insert into tab (a, b) values (5, 1);
Insert into tab (a, b) values (9, 2);
Update tab set a = 4 + a where b = 1;

Update tab
set n = (select min(n) from tab)
where n < (select avg(n) from tab);

Update tab
    n = max(n)
where n >= avg(n),
    n = min(n)
where n < avg(n);

Update tab set n =
                   case when n >= (select avg(n) from tab)
                            then (select max(n) from tab) else (select min(n) from tab)
                       end;

Grant all privileges on tab to postgres;

CREATE TABLE tab2 (
    id integer primary key,
    a numeric(18,2) not null default (2),
    b numeric(18,2) null,
    c numeric(18,2) null
);

insert into tab2 values (10, 1, 2, 3), (10, 2, 3, 4);

insert into tab2 (id, a, b, c) select 2 b, 1 id, 2 c, 3 a;
insert into tab2 (a, b, c) values (1, 2, 3);
insert into tab2 (id, b, c) select 1, 2, 3;

create table tab2 (
                      id integer primary key,
                      a numeric(18,2) not null default (2),
                      b numeric(18,2) null,
                      c numeric(18,2) null
);
create table tab2_d (
                        id integer primary key,
                        t2_id integer null references tab2 (id),
                        d integer
);
insert into tab2 (id, a, b, c) values (1, 1, 2, 3), (2, 2, 2, 2);
insert into tab2_d values (1, 2, 1);


delete from tab2_d;
delete from tab2
where not exists (
        select 1 from tab2_d where tab2_d.t2_id=tab2.id
    );

truncate table tab2