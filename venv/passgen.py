import secrets
import string

# string.ascii_letter is the combination of string.ascii_lowercase and string.ascii_uppercase
# string.digits is 0-9
# alphabet is the sequence that fills the need of the choice function
def pwrd(n):
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(n))
    return password

def phrase(n):
    with open('words') as f:
        words = [word.strip() for word in f]
        password = ' '.join(secrets.choice(words) for i in range(n))
        return password

#print(pwrd(100))

#print(phrase(3))

#print(secrets.randbelow(10))
