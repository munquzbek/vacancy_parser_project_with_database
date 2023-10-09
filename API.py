import requests
import json

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

