
from datetime import datetime


class Person:
    def __init__(self, full_name, birthday_age):
        full_name.strip()
        # assert full_name.count(' ') !=1, 'Введены неправильные входные данные!!!'
        assert int(birthday_age) in range(1900, 2019), 'Введен неверный год!!!'
        self.full_name = full_name
        self.age = int(birthday_age)

    def name(self):
        a = self.full_name.split()[0]
        return print("Имя: ", a)

    def familiya(self):
        b = self.full_name.split()[1]
        return print("Фамилия: ", b)

    def age_in(self, age_in):
        if not age_in:
            b = datetime.now().year - self.age
        else:
            b = self.age - int(age_in)
        return print("Vozrast", abs(b))

########################################################################################################################
class Employee(Person):
    def __init__(self, full_name, birthday_age, position, work_experience, salary=1000):

        super().__init__(full_name, birthday_age)
        self.position = position
        self.work_experience = int(work_experience)
        assert self.work_experience > 0, 'Введены неправильные входные данные!!!'
        self.salary = int(salary)

    def position1(self) -> str:
        if self.work_experience < 3:
            return "Junior" + ' ' + self.position
        if 3 <= self.work_experience < 6:
            return "Middle" + ' ' + self.position
        if self.work_experience >= 6:
            return "Senior" + ' ' + self.position

    def zepeshka(self, povushenie):
        zp = self.salary + povushenie
        return zp
########################################################################################################################
class ITEmployee(Employee):
    def __init__(self, full_name, birthday_age, position, work_experience, *args, **kwargs):
        super.__init__(*args, **kwargs)
        super().__init__(full_name, birthday_age, position, work_experience)
        self.skills = []

#Тут расбираюсь почему ошибку выдает; 'str' object has no attribute 'skills'
    # def add_skills(self, *args) -> list:
    #     k = []
    #     for i in args:
    #         k.append(i)
    #     self.skills = k
    #     return self.skills

full_name = input("Имя и фамилия: ")
birthday_age = input("Год рождения: ")

p = Person(full_name, birthday_age)
p.name()
p.familiya()
p.age_in(input("Введите год: "))


d = Employee(full_name, birthday_age, input("Position"), input("Age Prof"))
print(d.position1())
print(d.zepeshka(int(input("Povusit zp na: "))))

c = ITEmployee
d = ["Auto", "QC", "PR"]
# c.add_skills(*d)






