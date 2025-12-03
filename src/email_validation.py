import re


def email_validation(email: str) -> str:
    """Validates email address is Vodafone domain"""
    if not email:
        raise ValueError('Email cannot be empty')

    regex = re.compile(r"[\w\d.]*@vodafone.com")

    if not regex.match(email):
        return 'Invalid email address'

    return "Email address is valid"
