from Application.salary import calculate_salary as calc
from Application.db.people import get_employees as emp
from datetime import date


if __name__ == '__main__':
    print(date.today())
    calc()
    emp()

