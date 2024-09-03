# local variable
def hello():
    x=8
    print("local variable", x)
hello()

# global variable
def world():
    print(y)

y="happy world"
world()
