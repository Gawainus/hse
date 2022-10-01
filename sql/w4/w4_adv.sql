select duedate::date, a.countryregioncode, sum(totaldue)
from salesorderheader s join address a on s.shiptoaddressid=a.addressid
group by duedate, a.countryregioncode
order by duedate;


select
    shipdate::date,
    a.countryregioncode country,
    count(distinct
          case when totaldue < 10000 then s.salesorderid else 0) as orders_with_10k
from salesorderheader s
         join address a
              on a.addressid = s.shiptoaddressid
group by a.countryregioncode
having count(distinct
             case when totaldue > 10000 then s.salesorderid else null end) >= 5;

select
    ps.productsubcategoryid psid, ps.name subcategory, pmain.productid pid, pmain.name product,
    count(distinct salesorderid) - (select avg(sc.ordercount)
                                    from
                                        (select count(distinct salesorderid) ordercount
                                         from salesorderdetail s
                                                  join product p on s.productid = p.productid
                                         where p.productsubcategoryid = ps.productsubcategoryid
                                         group by p.productid) sc) as difference
from salesorderdetail s
         join product pmain on s.productid=pmain.productid
         join productsubcategory ps on ps.productsubcategoryid=pmain.productsubcategoryid
group by ps."name", pmain.productid, pmain.name, ps.productsubcategoryid
order by 2, 4;


select
    extract(month from duedate ) as month,
    sum(taxamt) as tax_amount,
    round(100*sum(taxamt) / (select sum(s2.taxamt) from sales.salesorderheader s2
                             where duedate between '20130101' and '20130331')) as tax_share
from sales.salesorderheader s
where duedate between '20130101' and '20130331'
group by extract(month from duedate )
order by 1;

select sh.duedate,
       count(distinct sh.salesorderid) ordersnumber
from production.product p2
         join productsubcategory s1
              on p2.productsubcategoryid = s1.productsubcategoryid
         join sales.salesorderdetail d
              on d.productid = p2.productid
         join sales.salesorderheader sh
              on sh.salesorderid = d.salesorderid
where s1.name = 'Road Bikes'
  and sh.salesorderid in (select salesorderid
                          from sales.salesorderdetail s
                          where duedate between '20130101' and '20131231'
                          group by 1
                          having count(*) > 10)
  and sh.duedate between '20130101' and '20131231'
group by sh.duedate;

select p.name, rank() over (order by ) from sales.salesorderdetail as sd
 join production.product as p using (productid);

select productid, order_number, rank() over (order by order_number desc) from
(select distinct productid, count(*) over (partition by productid) as order_number
 from sales.salesorderdetail as sd) as data;

select productid, order_number, dense_rank() over (order by order_number desc) from
(select distinct productid, count(*) over (partition by productid) as order_number
from sales.salesorderdetail as sd) as data;

select productid, order_number, row_number() over (order by order_number desc) from
(select distinct productid, count(*) over (partition by productid) as order_number
from sales.salesorderdetail as sd) as data;

-- Find products, which have 5 greatest number of finished manufacturing orders in every quarter.
-- Exclude orders with scrapped items.
select * from(
select
    dense_rank() over (partition by quarter order by number_of_orders desc) as r,
    quarter,
    productid,
    number_of_orders
    from (
select count(*) as number_of_orders,
'' || date_part('y', w.enddate) || '_' || date_part('quarter', w.enddate) as quarter,
w.productid
from production.workorder as w
where scrappedqty = 0
group by 2, w.productid) data) as rating
where r <= 5;

-- Query to display year to date revenue in connection with cities of delivery, year and shipping date
select distinct extract(year from soh.shipdate) as year,
       a.city,
       soh.shipdate,
        sum(soh.subtotal) over (partition by extract(year from soh.shipdate), a.city order by soh.shipdate)
from sales.salesorderheader soh
join person.address a on a.addressid=soh.shiptoaddressid
order by 1, 2, 3;


-- query to display revenue of a previous 10 orders in connection with cities of delivery, year and shipping date
select
    city,
    date_part('y', shipdate) as ship_year,
    shipdate,
    sum(subtotal) over yr_city as total_YTD
from sales.salesorderheader as sh
join person.address a on a.addressid=sh.shiptoaddressid
window yr_city
    as (partition by city, date_part('y', shipdate)
    order by shipdate
    rows between 10 preceding and current row )
order by city, date_part('y', shipdate), shipdate;

-- find month-to-month changes in number of orders for each product category. Display the data in chronological order
select
    cate_name,
    subcate_name,
    year,
    mon,
    number_of_orders - lag(number_of_orders, 1) over (partition by cate_name, subcate_name order by year, mon desc) as diff
    from
(select pc.name as cate_name,
       ps.name as subcate_name,
       date_part('y', sh.duedate) as year,
       date_part('mon', sh.duedate) as mon,
       count(distinct salesorderid) as number_of_orders
from sales.salesorderheader as sh
join sales.salesorderdetail as sd using (salesorderid)
join production.product as p using (productid)
join production.productsubcategory as ps using (productsubcategoryid)
join production.productcategory as pc using (productcategoryid)
group by 1, 2, 3, 4) as data;

-- query that will show aggregated subtotal and its moving averages with 5 and 20-day length
-- and order date for 2013 in the individual customer segment (exclude orders made by companies).
select date_trunc('day', orderdate),
       round(avg(sum(subtotal ))
             over(order by date_trunc('day', orderdate ) rows between 4 preceding and current row)) as ma5,
       round(avg(sum(subtotal ))
             over(order by date_trunc('day', orderdate ) asc rows between 19 preceding and current row)) as ma20
from sales.salesorderheader h join sales.customer c using(customerid)
where extract(year from orderdate) = 2013 and c.storeid is null
group by date_trunc('day', orderdate)
order by 1;

select duedate::date,
       a.countryregioncode,
       sum(subtotal),
       sum(sum(subtotal))
       over (partition by extract(month from duedate)
           order by a.countryregioncode)
from sales.salesorderheader soh
         join address a
              on soh.shiptoaddressid = a.addressid
group by duedate, a.countryregioncode
order by 2, 1;

--G5-1
select
    cate_name,
    year,
    mon,
    coalesce(number_of_orders - lag(number_of_orders, 1) over (partition by cate_name order by year, mon), 0) as diff
from
    (select pc.name as cate_name,
            date_part('y', sh.duedate) as year,
            date_part('mon', sh.duedate) as mon,
            count(distinct salesorderid) as number_of_orders
     from sales.salesorderheader as sh
              join sales.salesorderdetail as sd using (salesorderid)
              join production.product as p using (productid)
              join production.productsubcategory as ps using (productsubcategoryid)
              join production.productcategory as pc using (productcategoryid)
     group by 1, 2, 3) as data
order by cate_name, year, mon;

SELECT duedate::date,
       a.countryregioncode,
       sum(totaldue) over (partition by duedate::date order by a.countryregioncode)
FROM sales.salesorderheader soh
         join address a on soh.shiptoaddressid=a.addressid

SELECT distinct ps.name,
                p.productid,
                p.name,
                count(sod.salesorderid) over (partition by ps.productsubcategoryid)
FROM sales.salesorderdetail sod
         join production.product p on sod.productid=p.productid
         join production.productsubcategory ps on p.productsubcategoryid=ps.productcategoryid;

select *
from
    (select
         extract('year' from h.duedate) as year, p."name" as productname, sum(d.orderqty) as total,
         rank() over(partition by extract('year' from h.duedate) order by sum(d.orderqty) desc)
     from production.product as p join sales.salesorderdetail as d on p.productid = d.productid join sales.salesorderheader as h on h.salesorderid = d.salesorderid
     group by extract('year' from h.duedate), p.name
    ) as data
where rank = 1;

--G5-1-9
select duedate::date,
       case when row_number() over(order by duedate::date) > 1
           and row_number() over(order by duedate::date desc) > 1
                then
                        avg(sum(orderqty))
                        over(order by duedate::date
                            rows between 1 preceding and 1 following)
            else null end
from sales.salesorderdetail sd
         join sales.salesorderheader sh
              on sd.salesorderid=sh.salesorderid
group by duedate::date;

select duedate::date,
       (sum(orderqty) + lag(sum(orderqty), 1) over(order by
           duedate::date) + lead(sum(orderqty), 1) over(order by duedate::date))/3
from sales.salesorderdetail sd
         join sales.salesorderheader sh
              on sd.salesorderid = sh.salesorderid
group by duedate::date;

select duedate::date,
       avg(sum(orderqty))
       over(order by duedate::date
           rows between 2 preceding and current row)
from sales.salesorderdetail sd
         join sales.salesorderheader sh
              on sd.salesorderid=sh.salesorderid
group by duedate::date

select duedate::date,
       case when row_number() over(order by duedate::date) > 1 then
                        avg(sum(orderqty))
                        over(order by duedate::date
                            rows between 1 preceding and 1 following)
            else null end
from sales.salesorderdetail sd
         join sales.salesorderheader sh
              on sd.salesorderid=sh.salesorderid
group by duedate::date

select duedate::date,
       avg(sum(orderqty)) over (order by duedate::date)
from sales.salesorderdetail sd
         join sales.salesorderheader sh
              on sd.salesorderid = sh.salesorderid
group by duedate::date;
