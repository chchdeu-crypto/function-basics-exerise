#mission 1
def greet(name):
    print("hello",name)
greet("agent_x")
#mission 2
def add(a,b):
    print(a+b)
add(3,4)
#mission 3
def square(n):
    print(n**2)
square(5)
square(12)
#mission 4
def greet_with_titel(name,titel="agent"):
    print("hello",titel,name)
greet_with_titel(name="chaim")
greet_with_titel(name="chaim",titel="commander")
#mission 5
def agent_detalis(active,name,level):
    print("name: ", name , "level: " ,level , "active: ", active)
agent_detalis(level=5,name="agent x",active=True )    
#mission 6
def multiply(a,b=2):
    print(a*b)
multiply(5)
multiply(5,5)
#mission 7
def print_largest(a,b,c):
    if a>=b and a>=c:
        print(a)
    elif b>=a and b>=c:
        print(b)
    else:
        print(c)
print_largest(3,8,5)
print_largest(10,2,7)
print_largest(4,4,1)
#mission 8
def show_fahrenheit(c):
    print((c*9/5)+32)
show_fahrenheit(0)
show_fahrenheit(100)
show_fahrenheit(37.5)