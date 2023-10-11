from database.DB_utils import create_database, save_data_to_database

from database.config import config

from src.API import company_ids_from_api, get_info_each_company

from database.DBManager import get_companies_and_vacancies_count, get_all_vacancies, get_avg_salary, \
    get_vacancies_with_higher_salary, get_vacancies_with_keyword


def main():
    params = config()

    search_name = 'back-end'
    quantity = 40

    company_ids = company_ids_from_api(search_name, quantity)
    data = get_info_each_company(company_ids)
    create_database('headhunter', params)
    save_data_to_database(data, 'headhunter', params)

    get_companies_and_vacancies_count('headhunter', params)
    get_all_vacancies('headhunter', params)
    average_salary = get_avg_salary('headhunter', params)
    get_vacancies_with_higher_salary(average_salary, 'headhunter', params)
    get_vacancies_with_keyword('Web', 'headhunter', params)


if __name__ == '__main__':
    main()
