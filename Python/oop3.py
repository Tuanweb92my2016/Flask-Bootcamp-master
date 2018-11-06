def new_decorator(func):

    def wrap_func():
        print("Some code before executing func")
        func()
        print("Code here, after executing func()")

    return wrap_func

@new_decorator
def func_needs_decorator():
    print("Please decorate me!")

# func_needs_decorator = new_decorator(func_needs_decorator)


func_needs_decorator()
