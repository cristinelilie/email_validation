from src.input import input_function
from src.email_validation import email_validation


"""Email validation scripts"""

try:

    email = input_function()
    print(email_validation(email))

except Exception as e:
    print(e)
