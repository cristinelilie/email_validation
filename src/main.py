from src.input import input_function
from src.email_validation import email_validation

try:

    email = input_function()
    print(f"email: {email}")
    print(email_validation(email))

except Exception as e:
    print(e)
