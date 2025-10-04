# it is just like switch cases 

def handle(data):
    match data:
        case (x, y):  # matches a tuple of 2 elements
            print(f"Tuple with values: {x}, {y}")
        case int():
            print("Got an integer")
        case str():
            print("Got a string")
        case _:
            print("Unknown type")

handle((1, 2))     # Tuple
handle(42)         # Integer
handle("hello")    # String



score = 85

match score:
    case s if s >= 90:
        print("Grade: A")
    case s if s >= 75:
        print("Grade: B")
    case s if s >= 60:
        print("Grade: C")
    case _:
        print("Grade: F")
