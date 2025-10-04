def myFunc():
    print("Hello I am in the name_01 file")

myFunc()

# __name__ is a special built-in variable in Python, and it's used to tell whether a Python file is being run directly or being imported as a module.

print(__name__)  # __main__ this output means we are running the file directly but if we are importing it will give us the name of the file