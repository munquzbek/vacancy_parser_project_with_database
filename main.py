from database.DB_utils import create_database
from database.config import config
from src.API import company_ids_from_api, get_info_each_company


def main():
    params = config()

    search_name = 'developer'

    company_ids = company_ids_from_api(search_name)
    data = get_info_each_company(company_ids)
    create_database('headhunter', params)


if __name__ == '__main__':
    main()
