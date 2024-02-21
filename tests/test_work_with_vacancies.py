from src.work_with_vacancies import VacancyFilter
from src.work_with_vacancies import JSONVacancies
from data.data import HeadHunterAPI


test_vacancies_name = "Python"
test_number_of_vacancies = 100
test_name_file = 'vacancy_dict.json'
test_salary_from = 100000
test_salary_to = 300000
test_deleted_vacancy = 1

hhru = VacancyFilter(test_vacancies_name, test_number_of_vacancies, test_salary_from, test_salary_to)


def test_sort_by_salary_vacancies():
    assert type(hhru.sort_by_salary_vacancies(HeadHunterAPI.load_vacancies_from_json(test_name_file))) is list


def test_delete_and_save_vacancy():
    len1 = len(HeadHunterAPI.load_vacancies_from_json())
    JSONVacancies.save_vacancy(vacancies_dict_json=(JSONVacancies.delete_vacancy(deleted_vacancy=test_deleted_vacancy)))
    len2 = len(HeadHunterAPI.load_vacancies_from_json())
    assert len1 > len2


def test__str__vacancy_filter():
    assert str(hhru) == 'Успешный вывод.'


def test__str__json_vacancies():
    assert str(JSONVacancies()) == 'Успешный вывод.'


def test__repr__json_vacancies():
    assert repr(hhru) == (f"Название вакансии: {test_vacancies_name}\nКоличесвто вакансий для поиска: "
                          f"{test_number_of_vacancies}\nМаксимальная заработная плата: {test_salary_from}\n"
                          f"Минимальная заработная плата: {test_salary_to}\n")
