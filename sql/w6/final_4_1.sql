create database y2014_plans_yumen;

SELECT * FROM pg_roles;

-- 4.1
grant select on all tables in schema public to planadmin, planmanager;
grant select, update, insert, delete on plan_data, plan_status, country_managers to planadmin;

grant select, update, insert, delete on plan_data to planmanager;
grant select, update on plan_status to planmanager;
grant select on country_managers to planmanager;

grant select, update on v_plan_edit to planmanager;
grant select on v_plan to planmanager;

create user ivan;
create user sophie;
create user kirill;

grant planadmin to ivan;
grant planmanager to sophie, kirill;

select
    *
from information_schema.role_table_grants where grantee = 'planadmin';

insert into country_managers
values
    ('sophie', 'US'), ('sophie', 'CA'),
    ('kirill', 'FR'), ('kirill', 'GB'), ('kirill', 'DE'), ('kirill', 'AU');

