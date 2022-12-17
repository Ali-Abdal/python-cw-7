#1
class Person1:
    name = 'Ali'
    age = 18

first_person = Person1
print(first_person.name,first_person.age)

#2
class Person2:
    name = 'Ali'
    age = 18

    def is_adult(self):
        if Person2.age >= 18:
            print('You have too much responsibilities')

        else:
            print('Lucky you')

first_person = Person2
first_person.is_adult(first_person.age)

#3
class Person3:
    def __init__(self,age,name):
        self.age = age
        self.name = name

    def __str__(self):
        return f"""My name is {self.name} and u am {self.age} year old """

first_person = Person3('Ali', 18)
print(first_person)

