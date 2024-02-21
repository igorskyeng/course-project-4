from data.data import HeadHunterAPI


test_vacancies_name = "Python"
test_number_of_vacancies = 100
test_name_file = 'vacancy_dict.json'

hhru = HeadHunterAPI()


def test_load_vacancies_from_hhru():
    assert type(hhru.load_vacancies_from_hhru(test_vacancies_name, test_number_of_vacancies)) is str


def test_load_vacancies_from_json():
    assert type(hhru.load_vacancies_from_json(test_name_file)) is list


def test_str():
    assert str(hhru) == 'Класс для Загрузки вакансий из сайта hh.ru и их чтения с фалйла.'
