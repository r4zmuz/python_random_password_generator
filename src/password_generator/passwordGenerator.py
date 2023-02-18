import random

def generate() -> str:
    # https://www.101computing.net/wp/wp-content/uploads/ASCII-Table.pdf (ASCII table)
    # Generate a random Uppercase letter (based on ASCII code)
    uppercaseLetter1 = chr(random.randint(65, 90))
    # Generate a random Uppercase letter (based on ASCII code)
    uppercaseLetter2 = chr(random.randint(65, 90))
    # Generate a random lowercase letter (based on ASCII code)
    lowercaseLetter1 = chr(random.randint(97, 122))
    # Generate a random lowercase letter (based on ASCII code)
    lowercaseLetter2 = chr(random.randint(97, 122))
    # Generate a random number (based on ASCII code)
    digit1 = chr(random.randint(48, 57))
    # Generate a random number letter (based on ASCII code)
    digit2 = chr(random.randint(48, 57))
    # Generate a random punctuation sign (based on ASCII code)
    punctuationSign1 = chr(random.randint(33, 47))
    # Generate a random punctuation sign (based on ASCII code)
    punctuationSign2 = chr(random.randint(33, 47))

    # Generate password using all the characters, in random order
    password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + \
                    lowercaseLetter2 + digit1 + digit2 + punctuationSign1 + \
                    punctuationSign2
    # Shuffle password
    password_lst = list(password)
    random.shuffle(password_lst)
    return  ''.join(password_lst)
        



