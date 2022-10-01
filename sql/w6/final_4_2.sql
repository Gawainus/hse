-- 4.2
create materialized view product2 as
select
pc.productcategoryid as pcid,
p.productid as productid,
pc.name as pcname,
p.name as pname
from product p
join productcategory pc on pc.productcategoryid = p.productsubcategoryid;

select * from product2;

create materialized view country2 as
select distinct countryregioncode
from address;

grant select on product2 to planadmin, planmanager;
grant select on country2 to planadmin, planmanager;
