"""
type hint
    type_check 사용
    mypy 사용(type check만 할뿐 실행은 안해줌)
        pip install mypy
        mypy program.py
    pyright 사용(microsoft, c로 컴파일하기 때문에 빠름, 마찬가지로 type checking만)
        npm install -g pyright
        pyright program.py
"""

from typing import List, Tuple, Dict

int_var: int = 88
str_var: str = "abc"
float_var: float = 889.8
bool_var: bool = True
list_var: List[int] = [1, 2, 3]
tuple_var: Tuple[int] = (1, 2, 3)
dic_var: Dict[str, int] = {"age":17}

def type_check(obj, typer) -> None:
    if isinstance(obj, typer):
        pass
    else:
        raise TypeError("Type error :  + {typer}")

def cal_add(x: int, y: int) -> int:
    type_check(x, int)
    type_check(y, int)
    return x + y

print(cal_add(1, 3))
print(cal_add("dslafjasd","23048972wfy"))
print(cal_add([1, 2], [587, "asdfsa"]))

# isinstance(obj, class)

print(isinstance(88, int))