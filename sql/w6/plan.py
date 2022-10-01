import psycopg2


def start_planning(year, quarter, user, pwd):
    con = psycopg2.connect(
        database='y2022_plans_yumen', user=user, password=pwd, host='localhost')

    quarter_id = year + '.' + quarter
    cur = con.cursor()

    '''
    1. Delete plan data from the plan_data table related to the target year and quarter.
    '''
    cur.execute(f'delete from plan_data where quarterid=\'{quarter_id}\'')

    '''
    In the plan_status table delete records related to the target quarter
    '''
    cur.execute(f'delete from plan_status where quarterid=\'{quarter_id}\'')

    '''
    2. Create planning status records (plan_status table) for the selected quarter. The number of records added equals the number of countries in which customer-companies (shops) are situated.
    '''
    cur.execute(
        f'''
        insert into plan_status (quarterid, status, country)
        select
        distinct
            {quarter_id} as quarterid,
            'R' as status,
            co.countrycode as country
        from company_sales cs
        join customer cu on cs.cid = cu.customerid
        join company co on co.cname = cu.companyname;
        ''')

    '''
    3. Generate version N of planning data in the plan_data table. Use the calculation algorithm is described in section 1.4. on the page.
    '''
    cur.execute(
        f'''
        insert into plan_data
        select
            'N' as versionid,
            country,
            '{year}.' || quarter_yr as quarterid,
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
        where cs.ccls in ('A', 'B') and quarter_yr = {quarter}
        group by cs.year, cs.quarter_yr, cs.categoryid, co.countrycode) as sum_comp
        group by sum_comp.quarter_yr, sum_comp.categoryid, sum_comp.country;
        ''')

    '''
    4. Copy data from version N into version P in the plan_data table.
    '''
    cur.execute(
        f'''
        insert into plan_data
        select
            'P' as versionid,
            country,
            quarterid,
            pcid,
            salesamt
        from plan_data
        where versionid = 'N' and quarterid = '{quarter_id}';
        ''')

    con.commit()


def change_lock(year, quarter, user, pwd, status):
    con = psycopg2.connect(
        database='y2022_plans_yumen', user=user, password=pwd, host='localhost')

    quarter_id = year + '.' + quarter
    cur = con.cursor()

    cur.execute(
    f'''
    update plan_status
    set status = '{status}',
    author = current_user,
    modifieddatetime = current_timestamp
    where country in (select country from country_managers where username = current_user)
    and quarterid = '{quarter_id}'
    ''')

    con.commit()


def set_lock(year, quarter, user, pwd):
    change_lock(year, quarter, user, pwd, 'L')

def remove_lock(year, quarter, user, pwd):
    change_lock(year, quarter, user, pwd, 'R')

def accept_plan(year, quarter, user, pwd):
    con = psycopg2.connect(
        database='y2022_plans_yumen', user=user, password=pwd, host='localhost')

    quarter_id = year + '.' + quarter
    cur = con.cursor()
    cur.execute(f'''
    delete from plan_data
    where quarterid = '{quarter_id}'
    and versionid = 'A'
    and country in (select country from country_managers where username = current_user)
    ''')

    cur.execute(f'''
    insert into plan_data
    select
        'A' as status,
        pd.country as country,
        pd.quarterid as quarterid,
        pd.pcid as pcid,
        pd.salesamt as salesamt
    from plan_data pd
    left join plan_status ps on ps.quarterid = pd.quarterid and ps.country = pd.country
    left join country_managers cm on pd.country = cm.country
    where pd.quarterid = '{quarter_id}'
    and pd.versionid = 'P'
    and ps.status = 'R'
    and cm.username = current_user
    ''')

    cur.execute(
    f'''
    update plan_status
    set status = 'A',
    author = current_user,
    modifieddatetime = current_timestamp
    where country in (select country from country_managers where username = current_user)
    and quarterid = '{quarter_id}'
    ''')

    con.commit()


if __name__ == '__main__':
    # start_planning('2014', '1', 'ivan', None)
    # set_lock('2014', '1', 'kirill', None)
    # set_lock('2014', '1', 'sophie', None)

    remove_lock('2014', '1', 'kirill', None)
    remove_lock('2014', '1', 'sophie', None)
    accept_plan('2014', '1', 'kirill', None)
    accept_plan('2014', '1', 'sophie', None)