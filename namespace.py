"""
namespace: 개체를 구분할 수 있는 범위
__dict__: 네임스페이스를 확인할 수 있다.
dir(): 네임스페이스의  key 값을 확인할 수 있다.
__doc__: class의 주석을 확인한다.
__class__: 어떤 클래스로 만들어진 인스턴스인지 확인할 수 있다.
"""


class Robot:
    '''
    [Robot Class]
    Author: zizizi
    Role: ?????
    '''
    population = 0
    def __init__(self, name, code):
        self.name = name
        self.code = code
        Robot.population += 1
        
    def say_hi(self):
        print(f"Greetings, my masters call me {self.name}")
    
    def cal_add(self, a, b):
        return a + b
    
    def die(self):
        print(f"{self.name} is being destroyed")
        Robot.population -= 1
        if Robot.population == 0:
            print(f"{self.name} was the last one.")
        else:
            print(f"There are still {Robot.population} robots woring.")
            
        
    @classmethod
    def how_many(cls):
        print(f"{cls.population}")
        
    @staticmethod               # self, cls를 사용하지 않는 method. staticmethod decorator를 명시해야 instance에서 사용 가능
    def this_is_robot_class():
        print("robot class")
        
siri = Robot("siri", 21123213)
jarvis = Robot("jarvis", 13241323)
bixby = Robot("bixby", 234143)

print(Robot.__dict__)
print(jarvis.__dict__)

print(dir(Robot))
print(dir(siri))

print(Robot.__doc__)
print(siri.__doc__)

print(Robot.__class__)
print(siri.__class__)

Robot.this_is_robot_class()