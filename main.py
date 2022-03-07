import datetime
from db import people
from application import salary

if __name__ == '__main__':
    print(f'Current date is {datetime.date.today()}')
    salary.calculate_salary()
    people.get_employees()
