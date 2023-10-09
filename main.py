from API import company_ids_from_api, get_info_each_company

from DBManager import get_companies_and_vacancies_count, get_all_vacancies, get_avg_salary, \
    get_vacancies_with_higher_salary, get_vacancies_with_keyword


def main():
    search_name = 'developer'
    company_ids = company_ids_from_api(search_name)
    data = get_info_each_company(company_ids)
    print(data)


if __name__ == '__main__':
    main()
