'''
class AgeTooSmallError(Exception) → Defines a custom error class.

raise AgeTooSmallError("...") → Triggers the custom error when a condition fails.

except AgeTooSmallError → Catches your custom exception and handles it.

'''
# Custom Exceptions
class InsufficientBalanceError(Exception):
    """Raised when balance is too low for withdrawal."""
    pass

class ExceedsLimitError(Exception):
    """Raised when withdrawal exceeds per-transaction limit."""
    pass

# Function to withdraw money
def withdraw(balance, amount):
    MAX_LIMIT = 5000  # per transaction

    if amount > balance:
        raise InsufficientBalanceError("❌ Not enough balance to withdraw this amount.")
    elif amount > MAX_LIMIT:
        raise ExceedsLimitError(f"❌ Cannot withdraw more than {MAX_LIMIT} at once.")
    else:
        balance -= amount
        print(f"✅ Withdrawal of ₹{amount} successful. Remaining balance: ₹{balance}")
        return balance

# Main Program
try:
    current_balance = 6000
    print(f"Your current balance: ₹{current_balance}")
    
    amount = int(input("Enter amount to withdraw: ₹"))
    current_balance = withdraw(current_balance, amount)

except InsufficientBalanceError as e:
    print(e)

except ExceedsLimitError as e:
    print(e)

except ValueError:
    print("❗ Please enter a valid number.")


# JUST AN OTHER EXAMPLE

class AgeTooSmallError(Exception):
    """Custom exception for age below 18"""
    pass

def validate_age(age):
    if age < 18:
        raise AgeTooSmallError("Age must be at least 18.")
    else:
        print("Access granted.")

try:
    user_age = int(input("Enter your age: "))
    validate_age(user_age)
except AgeTooSmallError as e:
    print("Custom Exception:", e)
except ValueError:
    print("Please enter a valid number!")
