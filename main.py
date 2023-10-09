from src.API import company_ids_from_api, get_info_each_company


def main():
    search_name = 'developer'
    company_ids = company_ids_from_api(search_name)
    data = get_info_each_company(company_ids)
    print(data)


if __name__ == '__main__':
    main()
