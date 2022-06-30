"""
polymorphism(다형성)
여러 형태를 가질 수 있도록 한다. 즉, 객체를 부품화 할 수 있도록 한다.
같은 형태의 코드가 다른 동작을 하도록 하는 것
"""

class Robot:
    """
    Robot Class
    """

    _population = 0

    def __init__(self, name, age):
        self._name = name
        self._age = age
        Robot._population += 1

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("age는 0이하일 수 없습니다.")
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name == self._name:
            raise ValueError("동일 이름으로 변경할 수 없습니다.")
        self._name = name
        print("이름 변경 완료.")

    def say_hi(self):
        print("Greetings, I'm {self.name}")
    
    def cal_add(self, a, b):
        return a + b

    @classmethod
    def how_many(cls):
        return {f"We have {cls._population} robots."}

class Siri(Robot):
    def say_apple(self):
        print("hello my apple")

class SiriKo(Robot):
    def say_apple(self):
        print("안녕하세요 애플")

class Bixby(Robot):
    def say_samsung(self):
        print("안녕하세요")
