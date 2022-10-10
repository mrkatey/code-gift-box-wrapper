import random
from uuid import uuid4
from string import ascii_lowercase

def get_initial_credentials():
    salt = f"{uuid4()}"*5
    secret = ''.join([random.choice(ascii_lowercase)+salt[count] for count, _ in enumerate(ascii_lowercase)])
    return f"export SECRET_KEY='{secret}'"