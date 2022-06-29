"""
추상화: abstraction
불필요한 정보는 숨기고 중요한(필요한) 정보만을 표현함으로써
공통의 속성 값이나 행위(methons)를 하나로 묶어 이름을 붙이는 것이다
"""

class Robot:
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
        
siri = Robot("siri", 21123213)
jarvis = Robot("jarvis", 13241323)
bixby = Robot("bixby", 234143)

siri.say_hi()
print(Robot.population)
print(jarvis.population)
jarvis.how_many()