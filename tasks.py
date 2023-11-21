# task 1
import datetime

class CreateMixin:
    def create(self, todo, key):
        self.todo = todo
        self.key = key
    
class DeleteMixin:
    pass
class UpdateMixin:
    pass
class ReadMixin:
    pass
class ToDo(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin):
    todos = {}

    def set_deadline(self, date):
        self.date = date

    

# task 2
class Person:
    def __init__(self) -> None:
        self.__name = None
        self.__last_name = None
        self.__age = None
        self.__email = None

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

    @ property
    def last_name(self):
        return self.__last_name
    @last_name.setter
    def last_name(self, last_name):
        self.__last_name = last_name

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        self.__age = age
    
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email):
        self.__email = email

    

john = Person()
print(john.name) # None
print(john.last_name) # None
print(john.age) # None
print(john.email) # None
john.name = 'John'
john.last_name = 'Snow'
john.age = 30
john.email = 'johnsnow@gmail.com'
print(john.name) # John
print(john.last_name) # Snow
print(john.age) # 30
print(john.email) # johnsnow@gmail.com

# task 3
class Dog:
    def voice(self):
        print('Гав')

class Cat:
    def voice(self):
        print('Мяу')

barsik = Cat()
rex = Dog()
def to_pet(obj):
    obj.voice()

to_pet(barsik)
to_pet(rex)
