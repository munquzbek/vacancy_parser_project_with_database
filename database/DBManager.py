import psycopg2


def get_companies_and_vacancies_count(database_name: str, params: dict):
    """Get list of all companies and quantity of vacancies of each company."""
    conn = psycopg2.connect(dbname=database_name, **params)
    with conn.cursor() as cur:
        sql_select_query = 'SELECT company_name, quantity_vacancies ' \
                           'FROM companies'
        cur.execute(sql_select_query)
        data = cur.fetchall()
        for d in data:
            print(f'Компания: {d[0]}, кол-во вакансий {d[1]}')


def get_all_vacancies():
    """Receives a list of all vacancies indicating the company name, vacancy title and salary,
    and a link to the vacancy."""
    pass


def get_avg_salary():
    """Get average salary of all vacancies."""
    pass


def get_vacancies_with_higher_salary():
    """Get list of vacancies that salary higher than avg salary."""
    pass


def get_vacancies_with_keyword():
    """Get list of vacancies with keyword. (ex: 'Python')"""
    pass