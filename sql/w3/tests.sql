select "language", countrycode code
from countrylanguage
where
        left(language, 1) = 'A'
  and percentage >= 30
  and isofficial = false;

--  Write a query to "world" database to find a country
--  with a gnp under 1% of the greatest GNP in the world.
--  The records should be sorted by continent in alphabetical order
--  and by gnp from greatest to lowest
select code, gnp, continent from country
where gnp < (select max(gnp) * 0.01 from country)
order by continent asc, gnp desc;

select * from
(select c.gnp * 0.01 gmax from country c order by gnp desc limit 1) as gpl
join
(select * from country) as ctry
on gpl.gmax > ctry.gnp
order by ctry.continent, ctry.gnp desc;


--which non-capital city has the least population in North America?
select * from
city
left join country c on city.countrycode = c.code
where city.id <> c.capital and continent = 'North America'
order by city.population asc;

select ci.population ord, ci."name"
from country c join city ci
    on c.code = ci.countrycode
    and ci.id <> c.capital
where continent = 'North America';

select * from city where name = 'South Hill';
select * from country where code = 'AIA';
select *, *, * from city where name = 'South Hill';

select * from city as ci
left join country co on ci.countrycode = co.code
where co.population = 80;

select id, id+1, id+2 from (select * from city ) as m where 1=0;
select id, id+1, id+2 from city as m where 1=0;
select "id", "name" from city;
select m.*, m.* from city as m;
select 'Id', 'name' from city m;

select * from country
where
        left(localname, 3) = left(name, 3)
  and name like 'L%'
  and length(name) > 10;

-- Write a query to "world" database to find country
-- with surface area under 200 000 which has the greatest number of people
-- who speak English. Type the country's name into the text box.
select c.name from
country c
left join countrylanguage cl
on c.code = cl.countrycode
where c.surfacearea < 200000 and cl.language = 'English'
order by c.population desc
limit 10;

select * from countrylanguage where countrycode = 'JPN';

-- country has more than 4 words in its local name
-- and has area per capita > 0.02
select c.code, c.name, name_wc, surfacearea, population  from
country c
left join
(select code, array_length(regexp_split_to_array(localname, '\s'), 1) name_wc
 from country) as cc
on c.code = cc.code
where cc.name_wc > 4
and population <> 0
and c.surfacearea / c.population > 0.02;

select * from country
where
        left(localname, 3) = left(name, 3)
  and name like 'L%'
  and length(name) > 10;

-- find out which world’s capital has the least population
select ci.name from
country c
    left join
city as ci
on c.capital = ci.id
order by ci.population asc;

select
    name countryname,
    name cityname,
    to_char(100.0 * ct.population / c.population, '90D99') p_share
from country c
         join city ct
              on c.code = ct.countrycode
where
        c.population > 0
  and c.continent = 'North America'
  and c.continent = 'Africa'
  and 1.0 * ct.population / c.population >= 0.5;

-- Find out what 10 countries are closest to Argentina as per the following criterion:
-- C = ABS((GNP% + APC%) - (GNP_Argentina% + APC_Argentina%) )
-- GNP% - GNP of a country in percent out of to the biggest possible GNP in the world.
-- APC% - APC of a country in percent out of to the biggest possible APC in the world.
-- APC – SurfaceArea/Population. It is the area per one citizen.

select gnp_final.code, apc_final.name, gnp_per, apc_per
-- cache the result
into temp table gnp_apc
from
-- calculate GNP
(select cnt.code, cnt.gnp/gmax_tbl.gmax gnp_per from
    (select c.gnp gmax from country c order by gnp desc limit 1) as gmax_tbl
        join
    (select code, gnp from country) as cnt
    on gmax_tbl.gmax >= cnt.gnp) as gnp_final
join
-- calculate APC
(select apc_tbl.name, apc_tbl.code, apc_tbl.apc/apc_max_tbl.apc apc_per from
    (select apc from
        (select surfacearea/population apc from country where population > 0)
            as apc_tbl order by apc desc limit 1) as apc_max_tbl
        join
    (select code, name, surfacearea/population apc from country where population > 0)
        as apc_tbl
    on apc_max_tbl.apc >= apc_tbl.apc) as apc_final
on gnp_final.code = apc_final.code;

select name, code, abs(gnp_per + apc_per - gnp_per_arg - apc_per_arg) c
from gnp_apc
cross join (
    select gnp_per gnp_per_arg, apc_per apc_per_arg from gnp_apc where code = 'ARG'
) as tbl_arg
order by c asc limit 10;

select *
from
(select name, lifeexpectancy lexp_fr from country
--     where governmentform = 'Federal Republic' order by lifeexpectancy desc limit 1
full join
 (select lifeexpectancy from country
 where governmentform = 'Federal Republic' order by lifeexpectancy desc limit 1)) as fed_rep;

select governmentform, lifeexpectancy gle
from country
where governmentform in ('Federal Republic') and lifeexpectancy is not null
order by gle desc;

select governmentform, lifeexpectancy gle
from country
where  governmentform in ('Republic') and lifeexpectancy is not null
order by gle desc;

select governmentform, lifeexpectancy gle
from country
where  governmentform in ('Republic') and lifeexpectancy is not null
order by gle asc;


select gle_tbl.governmentform, gle_tbl.gle, lle_wrap.lle from (
select * from (
select  governmentform, lifeexpectancy gle
from country
where governmentform in ('Federal Republic') and lifeexpectancy is not null
order by gle desc limit 1) as fr
union
select * from (
select governmentform, lifeexpectancy gle
from country
where  governmentform in ('Republic') and lifeexpectancy is not null
order by gle desc limit 1) as r
union
select * from (select 'Others', lifeexpectancy gle
from country
where  governmentform not in ('Federal Republic', 'Republic') and lifeexpectancy is not null
order by gle desc limit 1) as other) as gle_tbl
join(
select * from (select * from (
    select  governmentform, lifeexpectancy lle
    from country
    where governmentform in ('Federal Republic') and lifeexpectancy is not null
    order by lle asc limit 1) as fr
union
select * from (
                  select governmentform, lifeexpectancy lle
                  from country
                  where  governmentform in ('Republic') and lifeexpectancy is not null
                  order by lle asc limit 1) as r
union
select * from (select 'Others', lifeexpectancy lle
               from country
               where  governmentform not in ('Federal Republic', 'Republic') and lifeexpectancy is not null
               order by lle asc limit 1) as other) as lle_tbl) as lle_wrap
on gle_tbl.governmentform = lle_wrap.governmentform;

-- transposed

select fr.Indicator, fr."Federal republic", r."Republic", other."Others" from (
select 'GLE' Indicator, lifeexpectancy "Federal republic"
from country
where governmentform in ('Federal Republic') and lifeexpectancy is not null
order by lifeexpectancy desc limit 1) as fr
join (
    select 'GLE' Indicator, lifeexpectancy "Republic"
    from country
    where governmentform in ('Republic') and lifeexpectancy is not null
    order by lifeexpectancy desc limit 1) as r
on fr.Indicator = r.Indicator
join (
    select 'GLE' Indicator, lifeexpectancy "Others"
    from country
    where governmentform not in ('Federal republic', 'Republic') and lifeexpectancy is not null
    order by lifeexpectancy desc limit 1) as other
     on fr.Indicator = other.Indicator
union
select fr.Indicator, fr."Federal republic", r."Republic", other."Others" from (
select 'LLE' Indicator, lifeexpectancy "Federal republic"
from country
where governmentform in ('Federal Republic') and lifeexpectancy is not null
order by lifeexpectancy asc limit 1) as fr
join (
    select 'LLE' Indicator, lifeexpectancy "Republic"
    from country
    where governmentform in ('Republic') and lifeexpectancy is not null
    order by lifeexpectancy asc limit 1) as r
       on fr.Indicator = r.Indicator
  join (
    select 'LLE' Indicator, lifeexpectancy "Others"
    from country
    where governmentform not in ('Federal republic', 'Republic') and lifeexpectancy is not null
    order by lifeexpectancy asc limit 1) as other
   on fr.Indicator = other.Indicator;


select fr.Indicator, fr."Federal republic", r."Republic", other."Others" from (
                                                                                  select 'GLE' Indicator, lifeexpectancy "Federal republic"
                                                                                  from country
                                                                                  where governmentform in ('Federal Republic') and lifeexpectancy is not null
                                                                                  order by lifeexpectancy desc limit 1) as fr
                                                                                  join (
    select 'GLE' Indicator, lifeexpectancy "Republic"
    from country
    where governmentform in ('Republic') and lifeexpectancy is not null
    order by lifeexpectancy desc limit 1) as r
                                                                                       on fr.Indicator = r.Indicator
                                                                                  join (
    select 'GLE' Indicator, lifeexpectancy "Others"
    from country
    where governmentform not in ('Federal republic', 'Republic') and lifeexpectancy is not null
    order by lifeexpectancy desc limit 1) as other
                                                                                       on fr.Indicator = other.Indicator
union
select fr.Indicator, fr."Federal republic", r."Republic", other."Others" from (
                                                                                  select 'LLE' Indicator, lifeexpectancy "Federal republic"
                                                                                  from country
                                                                                  where governmentform in ('Federal Republic') and lifeexpectancy is not null
                                                                                  order by lifeexpectancy asc limit 1) as fr
                                                                                  join (
    select 'LLE' Indicator, lifeexpectancy "Republic"
    from country
    where governmentform in ('Republic') and lifeexpectancy is not null
    order by lifeexpectancy asc limit 1) as r
                                                                                       on fr.Indicator = r.Indicator
                                                                                  join (
    select 'LLE' Indicator, lifeexpectancy "Others"
    from country
    where governmentform not in ('Federal republic', 'Republic') and lifeexpectancy is not null
    order by lifeexpectancy asc limit 1) as other
                                                                                       on fr.Indicator = other.Indicator;

