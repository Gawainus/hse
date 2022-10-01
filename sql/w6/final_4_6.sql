delete from plan_data where quarterid like '2014%';

delete from plan_status where quarterid like '%2';

--insert into plan_status (quarterid, status, country)
select
    distinct
    '2013.2' as quarterid,
    'R' as status,
    co.countrycode as country
from company_sales cs
join customer cu on cs.cid = cu.customerid
join company co on co.cname = cu.companyname;


insert into plan_data
select
    'N' as versionid,
    country,
    '2014.' || quarter_yr as quarterid,
    categoryid as pcid,
    avg(salesamt)
from
(select
    cs.quarter_yr as quarter_yr,
    cs.categoryid as categoryid,
    co.countrycode as country,
    sum(salesamt) as salesamt
from
    company_sales cs
        join customer cu on cs.cid = cu.customerid
        join company co on co.cname = cu.companyname
where cs.ccls in ('A', 'B') and quarter_yr = '1'
group by cs.year, cs.quarter_yr, cs.categoryid, co.countrycode) as sum_comp
group by sum_comp.quarter_yr, sum_comp.categoryid, sum_comp.country;

-- copy
insert into plan_data
select
    'P' as versionid,
    country,
    quarterid,
    pcid,
    salesamt
from plan_data
where versionid = 'N' and quarterid = '2014.1';

-- set_lock
update plan_status
set status = 'L',
modifieddatetime = current_timestamp
where author in (select country from country_managers where username = current_user) and quarterid = '2014.1'
returning *;

-- 4.6.3
-- insert into plan_data
select
    'A' as status,
    pd.country as country,
    pd.quarterid as quarterid,
    pd.pcid as pcid,
    pd.salesamt as salesamt
from plan_data pd
left join plan_status ps on ps.quarterid = pd.quarterid and ps.country = pd.country
left join country_managers cm on pd.country = cm.country
where pd.quarterid = '2014.1'
and pd.versionid = 'P'
and ps.status = 'R'
and cm.username = 'kirill';


