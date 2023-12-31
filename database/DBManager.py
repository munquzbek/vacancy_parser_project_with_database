import psycopg2


def get_companies_and_vacancies_count(database_name: str, params: dict):
    """Get list of all companies and quantity of vacancies of each company."""
    conn = psycopg2.connect(dbname=database_name, **params)
    with conn.cursor() as cur:
        sql_select_query = "SELECT company_name, quantity_vacancies " \
                           "FROM companies"
        cur.execute(sql_select_query)
        data = cur.fetchall()
        for d in data:
            print(f'Company name: {d[0]}, quantity of vacancies {d[1]}')


def get_all_vacancies(database_name: str, params: dict):
    """Receives a list of all vacancies indicating the company name, vacancy title and salary,
    and a link to the vacancy."""
    conn = psycopg2.connect(dbname=database_name, **params)
    with conn.cursor() as cur:
        sql_select_query = "SELECT company_name, vacancy_name, salary, currency, vacancy_url "\
                           "FROM vacancies " \
                           "INNER JOIN companies using (company_id)"
        cur.execute(sql_select_query)
        data = cur.fetchall()
        for d in data:
            if d[2] == 0:
                salary = 'Unknown'
                currency = '-'
            else:
                salary = d[2]
                currency = d[3]
            print(f'Company name: {d[0]}, Vacancy name: {d[1]}, Salary: {salary} {currency}, url: {d[4]}')


def get_avg_salary(database_name: str, params: dict):
    """Get average salary of all vacancies."""
    conn = psycopg2.connect(dbname=database_name, **params)
    with conn.cursor() as cur:
        sql_select_query = 'SELECT AVG(salary) FROM vacancies'
        cur.execute(sql_select_query)
        data = cur.fetchone()
        return data


def get_vacancies_with_higher_salary(average_salary: float, database_name: str, params: dict):
    """Get list of vacancies that salary higher than avg salary."""
    conn = psycopg2.connect(dbname=database_name, **params)
    with conn.cursor() as cur:
        sql_select_query = f"SELECT vacancy_name, salary, currency, vacancy_url " \
                           f"FROM vacancies " \
                           f"WHERE salary > {str(average_salary)} " \
                           f"ORDER BY salary DESC"
        cur.execute(sql_select_query)
        data = cur.fetchall()
        for d in data:
            print(f'Vacancy name: {d[0]}, Salary: {d[1]} {d[2]}, url: {d[3]}')


def get_vacancies_with_keyword(keyword: str, database_name: str, params: dict):
    """Get list of vacancies with keyword. (ex: 'Python')"""
    conn = psycopg2.connect(dbname=database_name, **params)
    with conn.cursor() as cur:
        sql_select_query = f"SELECT vacancy_name, salary, currency, vacancy_url " \
                           f"FROM vacancies " \
                           f"WHERE vacancy_name LIKE '%{str(keyword)}%'"
        cur.execute(sql_select_query)
        data = cur.fetchall()
        for d in data:
            print(f'Vacancy name: {d[0]}, Salary: {d[1]} {d[2]}, url: {d[3]}')
        return data
