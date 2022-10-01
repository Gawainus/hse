create materialized view mv_plan_fact_2014_q1 as
select
    plan.quarterid as quater,
    plan.country as country,
    categoryname,
    plan.salesamt - fact.salesamt as dev,
    (plan.salesamt - fact.salesamt) / plan.salesamt as dev_perc
from
(select
    year || '.' || quarter_yr as quarterid,
    countrycode,
    categoryid,
    name as categoryname,
    salesamt
from (
select
    year,
    quarter_yr,
    co.countrycode,
    cs.categoryid,
    pc.name,
    sum(cs.salesamt) as salesamt
from
    company_sales cs
join customer cu on cs.cid = cu.customerid
join company co on co.cname = cu.companyname
join productcategory pc on pc.productcategoryid = cs.categoryid
where year = '2013' and ccls in ('A', 'B')
group by year, quarter_yr, co.countrycode, cs.categoryid, pc.name) as data
where quarter_yr = 1) as fact
join (select
    country,
    quarterid,
    pcid,
    salesamt
from plan_data
where quarterid = '2014.1' and versionid = 'A') as plan
on fact.categoryid = plan.pcid and fact.countrycode = plan.country