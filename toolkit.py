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