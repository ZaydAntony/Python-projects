def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("You add sprinkles 🎊");
        func(*args ,**kwargs)
    return wrapper;

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("You added some fudge 🍫");
        func(*args, **kwargs);
    return wrapper

@add_sprinkles
@add_fudge
def get_icecream(flavour):
    print(f"Here is your {flavour} ice cream 🍨.");

get_icecream("Vanilla");