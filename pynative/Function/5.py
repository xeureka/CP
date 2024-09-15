def outer(a,b):
    def inner():
        return a + b
    
    return inner() + 5


print(outer(5,5))