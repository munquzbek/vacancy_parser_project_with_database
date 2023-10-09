import requests
import json

from typing import Any

# URL OF API REQUEST
api_url = 'https://api.hh.ru/vacancies'


def company_ids_from_api(search_name: str) -> list:
    """Get company ids using HeadHunter API, by searching name of vacancy"""
    quantity = 3
    params = {
        'text': search_name,
        'per_page': quantity
    }
    company_ids = []
    response = requests.get(url=api_url, params=params)
    data = response.content.decode()
    vacancies = json.loads(data)
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
        response = requests.get(url=api_url, params=params)
        data = response.content.decode()
        vacancies = json.loads(data)
        company_data.append(vacancies)
    return company_data
