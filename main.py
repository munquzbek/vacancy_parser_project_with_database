from database.DB_utils import create_database, save_data_to_database

from database.config import config

from src.API import company_ids_from_api, get_info_each_company


def main():
    params = config()

    search_name = 'developer'
    quantity = 10

    company_ids = company_ids_from_api(search_name, quantity)
    data = get_info_each_company(company_ids)
    create_database('headhunter', params)
    save_data_to_database(data, 'headhunter', params)


if __name__ == '__main__':
    main()
