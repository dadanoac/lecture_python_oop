"""
public vs private

getter/setter

"""

class Robot:
    """
    Robot Class
    """

    population = 0

    # 변수 앞에 _를 두개 사용하면 private으로 적용되어 외부에서 접근이 불가능함
    # 파이썬에서는 보통 _를 하나만 사용해서 개발자에게 선택권을 줌
    # __로 설정하면 상속받은 class에서도 사용할 수 없음
    def __init__(self, name, age):
        self._name = name
        self._age = age
        Robot.population += 1

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
        return {f"We have {cls.population} robots."}

ss = Robot("yss", 8)

ss.name = "arara"
# ss.name = "arara"
ss.age = 100
# ss.age = -100
print(ss.name, ss.age)