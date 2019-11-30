def fuzzint(argument):
    def decorator(function):
        def fuzz(*args,**kwargs):
            print("inside decorator")
            print("argument:"+str(argument))
            return function(*args,**kwargs)
        return fuzz
    return decorator