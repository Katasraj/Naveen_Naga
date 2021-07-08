def start_end_decorator(fun):
    def wrapper_fun():
        b = "Hello "+ fun()
        print(b)
    return wrapper_fun()

@start_end_decorator
def print_name():
    a = str(input("Enter Your name: "))
    return a

print_name