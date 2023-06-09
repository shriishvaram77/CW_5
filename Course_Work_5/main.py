from src.config import config
from src.DBManager import DBManager
from src.utils import getting_json_employer, getting_json_vacancies
from src.create_database import create_database, save_data_to_database_emp, save_data_to_database_vac


def main():
    params = config()
    select_employer = input("Введите имя работодателя для получения данных:  ")
    getting_json_employer(select_employer)
    getting_json_vacancies(select_employer)
    print("Внимание! Идет загрузка результатов в базу данных!")
    create_database('hh', params)
    save_data_to_database_emp('hh', params)
    save_data_to_database_vac('hh', params)
    print("Внимание! Загрузка результатов завершена!!!")
    while True:
        get = DBManager('hh', params)
        answer = input(f"Вам доступны следующие команды для отображения полученной информации:\n"
                       f"1: Получить список всех компаний c количеством вакансий в каждой компании\n"
                       f"2: Получить список всех вакансий с указанием названия компании,"
                       f"названия вакансии, зарплаты и ссылки на вакансию\n"
                       f"3: Получить среднюю зарплату по всем вакансиям\n"
                       f"4: Получить список всех вакансий, у которых зарплата выше средней по всем вакансиям\n"
                       f"5: Получить список всех вакансий по ключевому слову\n"
                       f"6: Выход из программы\n"
                       f"   Введите номер команды из вышеуказанного списка:  \n")

        if answer not in ('1', '2', '3', '4', '5', '6'):
            print("!!!! Ошибка ввода !!!! Введите номер команды из указанного списка !!!\n")
            continue
        elif answer == '1':
            get.get_companies_and_vacancies_count()
        elif answer == '2':
            get.get_all_vacancies()
        elif answer == '3':
            get.get_avg_salary()
        elif answer == '4':
            get.get_vacancies_with_higher_salary()
        elif answer == '5':
            keyword = input('Введите ключевое слово ...')
            get.get_vacancies_with_keyword(keyword)
        elif answer == "6":
            print("!!!! Спасибо, что воспользовались нашей программой !!!!")
            break


if __name__ == "__main__":
    main()
