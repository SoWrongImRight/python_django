# local
lambda x: x**2

# ecnlosing function levels
name = 'this is a global name'

def greet():
    name = "sammy"
    
    def hello():
        print("Hello "+ name)

    hello()
    
greet()
print(name)