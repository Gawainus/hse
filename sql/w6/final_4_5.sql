-- 4.5
insert into company_sales
select
    cid,
    salesamt,
    year,
    quarter as quarter_yr,
    year || '.' || quarter as qr,
    categoryid,
    cls as ccls
from(
select
    c.customerid as cid,
    sum(sod.linetotal) as salesamt,
    date_part('y', soh.orderdate) as year,
    date_part('quarter', soh.orderdate) as quarter,
    p.pcid as categoryid
from customer c
    join salesorderheader soh on soh.customerid = c.customerid
    join salesorderdetail sod on soh.salesorderid = sod.salesorderid
    join product2 p on sod.productid = p.productid
where c.companyname is not null
group by c.customerid, year, quarter, p.pcid) as d1
join company_abc using (cid, year);
