select count(*) nr, c.clsid
from car c
 join class ON class.clsid = c.clsid
group by c.clsid;

select count(*) nr, c.clsid
from car c
         join res ON res.cid = c.cid
group by c.clsid;

select count(c.cid) nr, c.clsid
from car c
         join res ON res.cid = c.cid
group by c.clsid;

select count(clsid) nr, c.clsid
from car c
         join res ON res.cid = c.cid
group by c.clsid;

select count(*) nr, d.did , d."name"
from driver d
         join res ON res.did = d.did
group by d.did , d."name" order by 2;

select count(distinct c.cid) nr, d.did , d."name"
from car c
         join res ON res.cid = c.cid
         join driver d on d.did = res.cid
group by d.did , d."name" order by 2;

select count(distinct cid) nr, d.did , d."name"
from driver d
         join res ON res.did = d.did
group by d.did , d."name" order by 2;

select count(distinct *) nr, d.did , d."name"
from driver d
         join res ON res.did = d.did
group by d.did , d."name" order by 2;

select count(distinct c.cid) nr, d.did , d."name"
from car c
         join res ON res.cid = c.cid
         join driver d on d.did = res.did
group by d.did , d."name" order by 2;

select car.cid, car.make, sum(res.days)
from res, car
where res.cid = car.cid
group by car.make, car.cid;

select car.make, sum(days)
from res
         join car on res.cid = car.cid
group by car.make;

select car.cid, car.make, sum(days)
from res
join car on res.cid = car.cid
group by car.make;

select car.cid, car.make, sum(res.days)
from res
 join car on res.cid = car.cid
group by car.make, car.cid;

select car.cid, car.make, sum(res.days)
from res
 join car on res.cid = car.cid
group by car.make, car.cid, res.did;


select extract(year from res.start) yr,
       extract(month from res."start" ) m,
       c.make,
       avg(res.bid) as a
from res join car c on c.cid =res.cid
group by extract (year from res.start),
         extract(month from res."start" ), make;

select yr, m, c.make,
       avg(res.cnt) as a
from (
         select cid, count(*) as cnt, extract(year from res.start) yr,
                extract(month from res."start" ) m
         from res
         group by cid, extract(year from res.start), extract(month from res."start")
     ) res
         join car c
              on c.cid =res.cid
group by yr, m, make
order by yr, m, make;

select extract(year from res.start) yr,
       extract(month from res."start" ) m,
       c.make,
       avg(count(*)) as a
from res join car c on c.cid =res.cid
group by extract(year from res.start),
         extract(month from res."start" ), make;

select yr, m, c.make,
       avg(res.cnt) as a
from (
         select cid, count(*) as cnt, extract(year from res.start) yr,
                extract(month from res."start" ) m
         from res
         group by cid, extract(year from res.start), extract(month from res."start")
     ) res , car c
group by yr, m, make
order by yr, m, make;

select yr, m, c.make,
       avg(res.cnt) as a
from (
         select cid, count(*) as cnt,
                extract(year from res.start) yr,
                extract(month from res."start" ) m
         from res
         group by cid, extract(year from res.start), extract(month from res."start")
     ) res
         join car c on c.cid =res.cid
group by yr, m, make



select dt as date, count(rstart.*) as picked, count(rfinish.*) as dropped
from ((select start as dt from res) union (select finish from res)) as dts
left join res as rstart on dts.dt = rstart."start"
left join res as rfinish on dts.dt = rfinish.finish
group by dt;

create materialized view used_cars as
    select * from car where mileage > 50000;

select * from used_cars;



create role car_manager;
create user alex with password '123';
create user stacy with password '123';
grant car_manager to alex, stacy;
grant usage on schema public to car_manager;
grant select, update on car to car_manager;

create view v_cars_b as
select cid, make, year, mileage, clsid
from car where clsid = 'B';

select * from v_cars_b;