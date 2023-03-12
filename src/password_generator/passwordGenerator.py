import random

def generate() -> str:
    # https://www.101computing.net/wp/wp-content/uploads/ASCII-Table.pdf (ASCII table)
    # Generate a random Uppercase letter (based on ASCII code)
    password = []
    for _ in range(3):
        uppercaseLetter = list(chr(random.randint(65, 90)))
        # Generate a random lowercase letter (based on ASCII code)
        lowercaseLetter = list(chr(random.randint(97, 122)))
        # Generate a random number (based on ASCII code)
        digit = list(chr(random.randint(48, 57)))
        # Generate a random punctuation sign (based on ASCII code)
        punctuationSign = list(chr(random.randint(33, 47)))
        # Generate password using all the characters, in random order
        password += uppercaseLetter + lowercaseLetter + digit + punctuationSign
        # Shuffle random characters
    random.shuffle(password)
    return  ''.join(password)
        


