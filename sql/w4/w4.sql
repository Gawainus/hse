select region r, sum(population) from country
group by r;

select r, c from (
select region r, count(code) c from country
group by r) as count_per_region
where c > 10;

select region r from country
group by r
having count(code) > 10;


select * from city order by population desc limit 10;

select * from country as c join city as ct on c.code = ct.countrycode
where ct.id in (select city.id from city order by population desc limit 10)
order by ct.population desc;

select count(distinct cl.language) nr, c.continent
from country c
         join countrylanguage cl ON cl.countrycode = c.code
group by c.continent, isofficial
having isofficial = true;

select count(distinct cl.language) nr,
       c.continent
from country c
         join countrylanguage cl ON cl.countrycode = c.code
where isofficial = true
group by c.continent;

select * from
    (select count(distinct cl.language) nr, c.continent from country c
     join countrylanguage cl ON cl.countrycode = c.code
     group by c.continent, isofficial) as data
where isofficial = true;

select c.continent, count(distinct c.region) regions from country c group by c.continent;

select count(distinct c.region) regions from country c group by c.continent;

select continent, count(*)
from (select distinct continent, region from country) as tab
group by continent;


select c.continent, count(*) regions
from country c group by c.continent;

select * from country
where country.population > all (
select city.population from city
join country c on city.countrycode = c.code
where c.continent = 'Asia'
) and country.continent = 'North America';

select name, code,
to_char(surfacearea / (select sum(surfacearea) from country where continent = 'Asia') * 100, '99D9999%') as share
from country
order by share desc;

select * from city where countrycode = 'RUS' order by population desc limit 1;

select
    c.name as country_name,
    ct.name as city_name,
    ct.population - (select max(population) from city where countrycode = c.code) as diff
from country as c
join city as ct
on ct.countrycode = c.code
order by 1, 3 desc;

select
    c.name as country_name,
    ct.name as city_name,
    ct.population - m as diff
from country as c
join city as ct on ct.countrycode = c.code
join (select max(population) as m, countrycode from city group by countrycode) as max_pop
    on ct.countrycode = max_pop.countrycode
order by 1, 3 desc;


select * from city as ct
where not exists (select * from country as c
where c.capital=ct.id)
and population >= 8000000;

select * from
city as ct
left join country as c
on ct.countrycode = c.code
where c.capital <> ct.id and ct.population >= 8000000;

select  c.name countryname,  ct.name cityname,  ct.population
as city_population
from city as ct
join country as c on c.code = ct.countrycode
where  ct.population > (select avg(population) as avg_population from city where countrycode = ct.countrycode )
order by c."name" , ct."name";

select  c.name countryname,  ct.name cityname,  ct.population as city_population
from (
country c
left join
city ct
on c.code = ct.countrycode
left join (
select countrycode, avg(population) pop from city group by countrycode) city_mean
on c.code = city_mean.countrycode)
where ct.population > city_mean.pop
order by c."name" , ct."name";

-- Query 1
select * from
    city as ct
        left join country as c
                  on ct.countrycode = c.code
where c.capital <> ct.id and ct.population >= 8000000;

-- Query 2
select  c.name countryname,  ct.name cityname,  ct.population as city_population
from (
         country c
             left join
             city ct
             on c.code = ct.countrycode
             left join (
             select countrycode, avg(population) pop from city group by countrycode) city_mean
         on c.code = city_mean.countrycode)
where ct.population > city_mean.pop
order by c."name" , ct."name";



select sum(population)
from country c2
where c2.code in
      (select countrycode
       from countrylanguage
       where percentage < 5);

select sum(case when c3.percentage < 5 then population else 0 end)
from country c2 join countrylanguage c3
                     on c2.code = c3.countrycode;

select sum(population)
from country c2
where exists (select 1 from countrylanguage c3 where c2.code = c3.countrycode and c3.percentage < 5);

select sum(population)
from country c2 join countrylanguage c3
                     on c2.code = c3.countrycode
where c3.percentage < 5;

-- comma-separated list of country codes where English is an official language
select region, string_agg(code, ',')
from country
left join countrylanguage c on country.code = c.countrycode
group by region;

select count(code)
from (select distinct code
from country
left join countrylanguage c on country.code = c.countrycode) as data
group by code;

select continent, language
from countrylanguage as cl
join country as c on c.code=cl.countrycode
where cl.language = 'Danish'
group by continent, language
having bool_and(percentage > 10) = true;

select name, continent, percentage
from countrylanguage as cl
join country as c on c.code=cl.countrycode
where cl.language = 'Danish';
