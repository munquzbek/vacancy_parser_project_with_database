from database.DB_utils import create_database, save_data_to_database

from database.config import config

from src.API import company_ids_from_api, get_info_each_company

from database.DBManager import get_companies_and_vacancies_count, get_all_vacancies, get_avg_salary, \
    get_vacancies_with_higher_salary, get_vacancies_with_keyword


params = config()


def user_interaction():
    while True:
        search_name = input("Enter keyword of vacancy: \n")
        companies_quantity = input("Enter quantity of companies: \n")
        database_name = 'headhunter'

        # get company ids from search with keyword
        company_ids = company_ids_from_api(search_name, companies_quantity)
        user_answer = input('\nDo you want to look more with these companies?\n'
                            'Yes or No:\n')
        if user_answer == 'Yes':
            # get info about each company, all vacancies in each, and quantity of vacancies
            data = get_info_each_company(company_ids)
            # create database and tables for companies and vacancies
            create_database(database_name, params)
            # save data in each table in DB
            save_data_to_database(data, 'headhunter', params)

            while True:
                input('Tap enter to show options\n')
                choice = input('\nYou have these options:\n'
                               '1. Get company names and their quantity of vacancies\n'
                               '2. Get all vacancies\n'
                               '3. Get average salary of all vacancies\n'
                               '4. Get vacancies which have salary higher than average salary\n'
                               '5. Get vacancies with keyword in name of vacancy\n'
                               'Write "end" to exit\n')

                if choice == '1':
                    get_companies_and_vacancies_count(database_name, params)
                elif choice == '2':
                    get_all_vacancies(database_name, params)
                elif choice == '3':
                    average_salary = get_avg_salary(database_name, params)
                    for d in average_salary:
                        print(f'Average salary: {round(float(d), 2)}')
                elif choice == '4':
                    average_salary = get_avg_salary(database_name, params)
                    for d in average_salary:
                        get_vacancies_with_higher_salary(round(d), 'headhunter', params)
                elif choice == '5':
                    keyword = input('Enter keyword: \n')
                    match = get_vacancies_with_keyword(keyword, database_name, params)
                    if not match:
                        print('No matches(')
                elif choice == "end":
                    print('Thank you, bye')
                    break
                else:
                    print('\nTry again')
                    continue
        else:
            print('Thank you, bye')
            break
        break
