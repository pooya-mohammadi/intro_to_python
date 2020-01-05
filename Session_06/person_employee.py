class Person:
    def __init__(self, first_name, last_name, age, education, middle_name=''):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.education = education
        self.middle_name = middle_name


    def print_full_name(self):
        if self.middle_name:
            print(f'{self.first_name} {self.middle_name} {self.last_name}')
        else:
            print(f'{self.first_name} {self.last_name}')

    def add_middle_name(self, middle_name):
        self.middle_name = middle_name
        self.print_full_name()


class Employee(Person):
    def __init__(self, first_name, last_name, age, education, job_title, salary,
                 expenses, middle_name=''):
        super().__init__(first_name, last_name, age, education, middle_name)
        self.__salary = salary
        self.__expenses = expenses
        self.job_title = job_title
        self.__whole_income = self.__salary - self.__expenses

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, val):
        self.__salary = val
        self.__calculate_whole_income()

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, val):
        self.__expenses = val
        self.__calculate_whole_income()

    @property
    def whole_income(self):
        return self.__whole_income

    def __calculate_whole_income(self):
        self.__whole_income = self.__salary - self.__expenses

    def change_salary(self, val):
        self.salary += val
        self.__calculate_whole_income()

    def change_job(self, job_title):
        self.job_title = job_title


pooya = Employee('pooya', 'mohammadi', '25', 'master', 'programmer', 100, 50)
print('my income is', pooya.whole_income)
pooya.change_salary(1500)
print('my income is', pooya.whole_income)
