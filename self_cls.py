# ** self는 인스턴스 객체이다!!
# ** 클래스 안에 있는 self의 주소와 만들어진 인스턴스의 주소는 같다. 즉, self는 인스턴스 그 자체

class SelfTest:
    
    # 클래스 변수
    name = "amamov"
    
    def __init__(self, x):
        self.x = x
        
    # 클래스 메서드
    @classmethod
    def func1(cls):
        print(f"cls: {cls}")
        print("func1")
    
    # 인스턴스 메서드
    def func2(self):
        print(f"self: {self}")
        print("class 안의 self 주소: ", id(self))
        print("func2")
        
test_obj1 = SelfTest(17)

test_obj1.func1()
test_obj1.func2()

print(f"인스턴스의 주소: {id(test_obj1)}")

SelfTest.func1()
print(test_obj1.name)
SelfTest.func2()