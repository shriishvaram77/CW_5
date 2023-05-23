import json
import requests as requests


def getting_employer(keyword: str):
    """ Выгрузка списка работодателей с помощью API подключения к сайту hh.ru"""

    params = {'text': keyword,
              'per_page': 10,
              'only_with_vacancies': True
              }
    response_url = requests.get('https://api.hh.ru/employers', params=params, verify=False)
    response_data = json.loads(response_url.text)
    employers = response_data['items']
    return employers


def employer_id(keyword):
    '''получение  ID работодателей'''

    employer_list = []
    employers = getting_employer(keyword)
    for emp in employers:
        employer_list.append(emp['id'])
    return tuple(employer_list)


def getting_vacancies(index):
    """Выгрузка списка вакансий выбраных работодателей
     с помощью API подключения к сайту hh.ru"""

    params = {'employer_id': index,
              'per_page': 100,
              }
    response_url = requests.get('https://api.hh.ru/vacancies', params=params, verify=False)
    response_data = json.loads(response_url.text)
    vacancies = response_data['items']
    return vacancies


def getting_json_employer(keyword):
    """Выгрузка данных о работодателях в файл JSON"""

    data = getting_employer(keyword)
    with open('src/employer.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
        print("Данные о работодателях получены!!!")


def getting_json_vacancies(keyword):
    """Выгрузка данных о вакансиях в файл JSON"""

    data = getting_vacancies(employer_id(keyword))
    with open('src/vacancies.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
        print("Данные о вакансиях получены!!!")
