
-- 4.4
select c.customerid, companyname, sum(soh.subtotal) as st
from customer c
         join salesorderheader soh on soh.customerid = c.customerid
where c.companyname is not null
group by c.customerid
order by st desc;

select c.customerid, companyname, date_part('y', soh.orderdate) as year,  sum(soh.subtotal) as st
from customer c
         join salesorderheader soh on soh.customerid = c.customerid
where c.companyname is not null
group by c.customerid, year
order by st desc;

select
    customerid,
    companyname,
    year,
    st,
    sum(st) over (partition by year rows between unbounded preceding and current row) srt
from (
         select c.customerid, companyname, date_part('y', soh.orderdate) as year,  sum(soh.subtotal) as st
         from customer c
                  join salesorderheader soh on soh.customerid = c.customerid
         where c.companyname is not null
         group by c.customerid, year
         order by st desc) as data
where year in ('2012', '2013');

insert into company_abc
select
    customerid as cid,
    st as salestotal,
    CASE
        WHEN srt <= (select 0.8 * sum(soh.subtotal) as s_a
                     from customer c
                              join salesorderheader soh on soh.customerid = c.customerid
                     where c.companyname is not null and year = date_part('y', soh.orderdate)) THEN 'A'
        WHEN srt <= (select 0.95 * sum(soh.subtotal) as s_b
                     from customer c
                              join salesorderheader soh on soh.customerid = c.customerid
                     where c.companyname is not null and year = date_part('y', soh.orderdate)) THEN 'B'
        ELSE 'C'
        END cls,
    year
from
    (select
         customerid,
         companyname,
         year,
         st,
         sum(st) over (partition by year rows between unbounded preceding and current row) srt
     from (
              select c.customerid, companyname, date_part('y', soh.orderdate) as year,  sum(soh.subtotal) as st
              from customer c
                       join salesorderheader soh on soh.customerid = c.customerid
              where c.companyname is not null
              group by c.customerid, year
              order by st desc) as data
     where year in ('2012', '2013')) as data2;
