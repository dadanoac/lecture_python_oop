"""
객체 내에 있는 변수등른 __dict__를 통해 관리가 된다.
__slots__을 통해 변수를 관리:
파이썬 인터프리터에게 통보 해당 클래스가 가지는 속성을 제한한다.
__dict__를 통해 관리되는 객체의 성능을 최적화한다. -> 다수의 객체 생성시 메모리 사용 공간 대폭 감소한다.
"""
class WithoutSlotClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age


wos = WithoutSlotClass("manem", 15)

print(wos.__dict__)

# wos.__dict__["hello"] = "world"

# print(wos.__dict__)

class withSlotClass:
    __slots__ = ["name", "age"]

    def __init__(self, name, age):
        self.name = name
        self.age = age

ws = withSlotClass("amamov", 25)

# slot을 사용하면 __dict__를 사용할 수 없음
# print(ws.__dict__)

print(ws.__slots__)

import timeit

#메모리 사용량 비교

def repeat(obj):
    def inner():
        obj.name = "amamov"
        obj.age = 227
        del obj.name
        del obj.age
    return inner

use_slot_time = timeit.repeat(repeat(ws), number=999999)
no_slot_time = timeit.repeat(repeat(wos), number=999999)

print("use slot:", min(use_slot_time))
print("no slot:", min(no_slot_time))