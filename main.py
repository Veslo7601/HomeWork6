"""Module providing a function """
from collections import UserDict
from datetime import datetime


class Field:
    """Class representing a default class"""

    def __init__(self, value):
        self.__value = None
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    """Class representing a Name"""

class Phone(Field):
    """Class representing a Phone"""

    @property
    def value(self):
        """Getter"""
        return self.__value

    @value.setter
    def value(self, value):
        """Setter"""
        if len(str(value)) != 10:
            raise ValueError ("Номер не має 10 цифр")
        elif not value.isdigit():
            raise ValueError ("У номері є зайві символи ")
        else:
            self.__value = value

class Birthday(Field):
    """Class representing a Birthday """

    @property
    def valid_birthday(self):
        """Getter"""
        return self.__value

    @valid_birthday.setter
    def valid_birthday(self,value):
        """Setter"""
        correct = datetime.strptime(value, '%d-%m-%Y')
        if correct:
            self.__value = correct
        else:
            raise ValueError ("Дата не коректна")

class Record:
    """Class representing a Record"""

    def __init__(self, name, birthday=None):

        self.name = Name(name)
        self.phones = []
        self.birthday = Birthday(birthday)

    def add_phone(self,value):
        """function for adding phones"""

        self.phones.append(Phone(value))

    def remove_phone(self,value):
        """function for remove phones"""

        if self.find_phone(value):
            self.phones.remove(self.find_phone(value))

    def edit_phone(self,value,value_two):
        """function for edit phones"""

        if self.find_phone(value):
            self.remove_phone(value)
            self.add_phone(value_two)
        else:
            raise ValueError("Номер не існує")

    def find_phone(self,value):
        """function for find phones"""

        for phone in self.phones:
            if str(phone) == str(value):
                return phone

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def days_to_birthday(self):
        """Function to find birthday"""
        current_date = datetime.now().date()
        day, month, year = str(self.birthday).split("-")
        if int(month) >= current_date.month:
            birthday = datetime(year=current_date.year, month=int(month), day=int(day)).date()
        else:
            birthday = datetime(year=current_date.year+1, month=int(month), day=int(day)).date()

        days = birthday - current_date

        if days.days < 0:
            return print("Birthday passed")
        elif days.days == 0:
            return print("Birthday today")
        else:
            return print(f"There are {days.days} days left until the birthday")

class AddressBook(UserDict):
    """Class representing a AddressBook"""

    def add_record(self,Record):
        """function for add record"""

        return super().__setitem__(Record.name.value,Record)

    def find(self,Name):
        """function for find record"""

        for key in self.data:
            if str(key) == str(Name):
                return super().__getitem__(key)

    def delete(self,Name):
        """function for delete record"""

        for key in self.data:
            if str(key) == str(Name):
                return super().__delitem__(key)

    def iterator(self,max_number):
        """Generator for finding N number of contacts"""
        count = 0
        for key in self.data:
            if count >= max_number:
                break
            yield self.find(key)
            count += 1

#The file ends


book = AddressBook()

ihor = Record("Ihor","8-02-1998")
ihor.add_phone("1111111111")
ihor.add_phone("2222222222")

Oleg = Record("Oleg","13-02-1998")
Oleg.add_phone("3333333333")
Oleg.add_phone("4444444444")

Ivan = Record("Ivan","12-02-1998")
Ivan.add_phone("5555555555")
Ivan.add_phone("6666666666")
Ivan.add_phone("7777777777")

Max = Record("Max","13-02-1998")
Max.add_phone("8888888888")
Max.add_phone("9999999999")

ihor.days_to_birthday()

book.add_record(ihor)
book.add_record(Oleg)
book.add_record(Ivan)
book.add_record(Max)

iter = book.iterator(5)
for k in iter:
    print(f"{k}")
