import psycopg2


def create_database(database_name: str, params: dict):
    """Create database and tables about companies and vacancies."""
    conn = psycopg2.connect(dbname='postgres', **params)
    conn.autocommit = True  # automatic commit after each sql query (lines: 10, 11)
    cur = conn.cursor()

    cur.execute(f'DROP DATABASE {database_name}')
    cur.execute(f'CREATE DATABASE {database_name}')

    cur.close()
    conn.close()

    conn = psycopg2.connect(dbname=database_name, **params)
    #   OPEN CURSOR FOR CREATING TABLE 'companies'
    with conn.cursor() as cur:
        cur.execute("""
                    CREATE TABLE companies (
                        company_id SERIAL PRIMARY KEY,
                        company_name VARCHAR(255) NOT NULL,
                        quantity_vacancies INTEGER,
                        company_url TEXT
                    )
                """)
    #   CREATING TABLE 'companies'
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE vacancies (
                vacancy_id SERIAL PRIMARY KEY,
                company_id INT REFERENCES companies(company_id),
                vacancy_name VARCHAR NOT NULL,
                min_salary INTEGER,
                max_salary INTEGER,
                vacancy_url TEXT
            )
        """)

    conn.commit()
    conn.close()
