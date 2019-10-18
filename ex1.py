
# Задание 1 (на создание классов)
# Переделываем (а что-то повторяем и закрепляем) наши классы таким образом:
# 1) Person (два свойства: 1. теперь full_name пусть будет свойством, а не функцией (одно поле, мы ожидаем - тип строка и состоит из двух слов «имя фамилия»), а свойств name и surname нету, 2. год рождения).
# Реализовать методы, которые:
# 1.	выделяет только имя из full_name
# 2.	выделяет только фамилию из full_name;
# 3.	вычисляет сколько лет было/есть/исполнится в году, который передаётся параметром (obj.age_in(year)); если не передавать параметр, по умолчанию, сколько лет в этом году;
# ** (только для продвинутых) Можете в конструкторе проверить, что в full_name передаётся строка, состоящая из двух слов, если нет, вызывайте исключение 😊
# ** (только для продвинутых) Можете в конструкторе проверить, что в год рождения меньше 2019, но больше 1900, если нет вызывайте исключение
# 2) Employee (наследуемся от Person) (добавляются свойства: должность, опыт работы, зарплата)
# ** (только для продвинутых) Можете в конструкторе проверить, что в опыт работы и зарплата не отрицательные 😊
# Реализовать новые методы:
# 1.	возвращает должность с приставкой, которая зависит от опыта работы: Junior — менее 3 лет, Middle — от 3 до 6 лет, Senior — больше 6 лет.
# Т.е. метод должен вернуть позицию с приставкой Junior/Middle/Senior <position>. Если, например у вас объект имел должность “programmer” с опытом 2 года, метод должен вернуть “Junior programmer”
# 2.	метод, который увеличивает зарплату на сумму, которую вы передаёте аргументом.
# 3) ITEmployee (наследуемся от Employee)
# 1. Реализовать метод добавления одного навыка в новое свойство skills (список) новым методом add_skill (см. презентацию).
# 2. * Реализовать метод добавления нескольких навыков в новое свойство skills (список) новым методом add_skills.
# Тут можно выбрать разные подходы: или аргумент один и он список навыков, которым вы расширяете список-свойство skill, или вы принимаете неопределённое количество аргументов, и все их добавляете в список-свойство skill

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

    def add_skills(self, *args):
        for i in args:
            self.skills.append(i)

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
d = ["Auto", "QC"]
c.add_skills(*d)






