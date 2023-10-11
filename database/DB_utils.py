from typing import Any

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
                salary INTEGER,
                currency VARCHAR,
                vacancy_url TEXT
            )
        """)

    conn.commit()
    conn.close()


def save_data_to_database(data: list[dict[str, Any]], database_name: str, params: dict):
    """Save gotten data in DB"""
    conn = psycopg2.connect(dbname=database_name, **params)

    with conn.cursor() as cur:
        for company in data:
            cur.execute(
                """
                INSERT INTO companies (company_name, quantity_vacancies, company_url)
                VALUES (%s, %s, %s)
                RETURNING company_id
                """,
                (company['employer']['name'], company['quantity'], company['employer']['url'])
            )
            company_id = cur.fetchone()[0]
            for vacancy in company['vacancy']:
                if vacancy['salary'] is None:
                    salary = 0
                    currency = None
                else:
                    if vacancy['salary']['from'] is None:
                        salary = 0
                        currency = None
                    else:
                        currency = vacancy['salary']['currency']
                        salary = vacancy['salary']['from']
                cur.execute(
                    """
                    INSERT INTO vacancies (company_id, vacancy_name, salary, currency, vacancy_url)
                    VALUES (%s, %s, %s, %s, %s)
                    RETURNING company_id
                    """,
                    (company_id, vacancy['name'], salary, currency, vacancy['alternate_url'])
                )

    conn.commit()
    conn.close()

