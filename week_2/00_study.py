class Person:
    def __init__(self, param_name):
        print("i'm create", self)
        self.name = param_name

    def talk(self):
        print("안녕하세요, 제이름은", self.name, "입니다.")


person_1 = Person("유재석")
print(person_1)
print(person_1.name)
person_1.talk()
person_2 = Person("박명수")
print(person_2)
print(person_2.name)
