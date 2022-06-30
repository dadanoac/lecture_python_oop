"""
composition
다른 클래스의 일부 메서드를 사용하고 싶지만, 상속은 하고 싶지 않은 경우
1. 부모 클래스가 변하면 자식 클래스는 계속 수정되어야 한다.
2. 부모 클래스의 메서드를 오버라이딩 하는 경우 내부 구현 방식의 얕은 이해로 오류가 생길 가능성 증가
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

    def cal_add(self, a, b):
        return a + b

class BixbyCal:
    def __init__(self, name, age):
        self.Robot = Robot(name, age)

    def cal_add(self, a, b):
        return self.Robot.cal_add(a, b)

bixbycal = BixbyCal("galuxy", 10)
print(bixbycal.cal_add(1,2))