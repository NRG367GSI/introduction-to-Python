def hello_world():
    print("Hello World!")

hello = hello_world

#hello()

def wrapper():
    def hello_world():
        print("Hello World!")
    hello_world()

#wrapper()

def summ(x,y):
    return x + y

def higher(func):
    return func
    

#print(higher(summ(2,3)))

def decor(func):
    def speak(x,y):
        print("Декоратор")
        func(x,y)
    return speak

@decor
def mult(x,y):
    print(x * y)


mult(2,3)


