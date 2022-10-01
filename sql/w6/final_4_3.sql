-- 4.3
insert into company (cname, countrycode, city)
select
    c.companyname,
    a.countryregioncode,
    a.city
from customer c
join customeraddress ca on ca.customerid = c.customerid
join address a on ca.addressid = a.addressid
where c.companyname is not null;
