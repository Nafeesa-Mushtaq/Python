'''
try:
    # Code that might raise an error
except SomeError:
    # Code that runs if the error occurs
else:
    # Code that runs if no error occurs (optional) if try successfully runs
finally:
    # Code that always runs (optional)

'''
# Example 1: Handling ZeroDivisionError
try:
    x = int(input("Enter a number: "))
    result = 100 / x
    print("Result:", result)
except ZeroDivisionError:
    print("You can't divide by zero!")

# Example 2: Catching Multiple Exceptions
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("That's not a valid number!")
except Exception as e:
    print("Something went wrong:", e)

#  Example 3: Using else and finally
try:
    num = int(input("Enter number: "))
except ValueError:
    print("Invalid input!")
else:
    print(f"You entered {num} successfully.")
finally:
    print("Program ended.")

