
from random import randint, choice
import string

def generate_password():
	password_min = 20
	password_max = 30
	all_chars = string.ascii_letters + string.punctuation + string.digits

	password = "".join(choice(all_chars)for x in range(randint(password_min, password_max)))
	print(password)


generate_password()