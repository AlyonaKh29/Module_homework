from Application.salary import calculate_salary as calc
from Application.db.people import get_employees as emp
from datetime import date
import wikipedia


def find_a_word_on_wikipedia(word):
    """ Задание 4: импортировать пакет, указать в requirements.txt  и написать программу с ним """
    language = "ru"
    wikipedia.set_lang(language)
    result = wikipedia.page(word)
    print(result.summary)


if __name__ == '__main__':
    print(date.today())
    calc()
    emp()
    find_a_word_on_wikipedia('Эльбрус')
