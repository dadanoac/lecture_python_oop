def deco(func):
    def wrapper():
        print("@ kj")
        func()
    return wrapper

@deco
def smile():
    print("😊")

@deco
def angry():
    print("😒")
    
@deco
def love():
    print("😍")
@deco   
def sorry():
    print("😢")
    
smile()
angry()
love()
sorry()