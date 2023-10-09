import requests
import json

from typing import Any

# URL OF API REQUEST
api_url = 'https://api.hh.ru/vacancies'


def get_data(params):
    response = requests.get(url=api_url, params=params)
    data = response.content.decode()
    vacancies = json.loads(data)
    return vacancies


def company_ids_from_api(search_name: str, quantity) -> list:
    """Get company ids using HeadHunter API, by searching name of vacancy"""
    params = {
        'text': search_name,
        'per_page': quantity
    }
    company_ids = []
    vacancies = get_data(params)
    for vacancy in vacancies['items']:
        company_ids.append(vacancy['employer']['id'])
        print(vacancy['employer']['name'])
    return company_ids


def get_info_each_company(company_ids: (list, Any)) -> list:
    """Get info about each company, and vacancies of them"""
    company_data = []
    for company_id in company_ids:
        params = {
            'employer_id': company_id
        }
        vacancies = get_data(params)
        company_data.append({'employer': vacancies['items'][0]['employer'],
                             'vacancy': vacancies['items'],
                             'quantity': vacancies['found']})
    return company_data
