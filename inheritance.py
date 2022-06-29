"""
[클래스 상속]
1. 부모 클래스가 갖는 모든 메서드와 속성이 자식 클래스에 그대로 상속된다.
2. 자식 클래글래스에서 별도의 메서드나 속성을 추가할 수 있다.
3. 메서드 오버라이딩
4. super()
5. Python의 모든 클래스는  Object 클래스를 상속한다.: 모든 것은 객체이다.
MyClass.mro() --> 상속 관계를 보여준다.
"""

class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        Robot.population += 1

    def __call__(self):
        print("call")
        return f"I'm {self.name}"

    @staticmethod
    def are_you_robot():
        print("yes")

    def say_hi(self):
        print("Greetings, call me {self.name}.")


class Siri(Robot):

    # super를 사용하지 않으면 __init__이 overriding됨.
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age      

    def call_me(self):
        print("뭐요")
    
    def cal_add(self, a, b):
        return a + b

    @classmethod
    def hello_app(cls):
        print(f"{cls} hello apple")

    def say_hi(self):
        print("Greetings, call me {self.name}. by apple")
        
    def super_say_hi(self):
        self.say_hi()
        super().say_hi()

siri = Siri("iphone13 pro", 15)

print(siri())
siri.call_me()
print(siri.cal_add(10, 35))
Siri.hello_app()

siri.say_hi()
print(Siri.population)
print(Robot.population)
siri.super_say_hi()

# 아무것을 상속받지 않아도 object class를 상속
print(Siri.mro())   #[<class '__main__.Siri'>, <class '__main__.Robot'>, <class 'object'>]
# print(object)
# print(dir(object()))
# print(object.__name__)
# 
# print(int.mro())


class A:
    pass

class B:
    pass

# 의미없는 다중상속은 지양. 조립 등의 동작을 할때에는 사용할 수 있음.
class C(A, B):
    pass

print(C.mro())