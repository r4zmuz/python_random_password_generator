import random

#https://www.101computing.net/wp/wp-content/uploads/ASCII-Table.pdf (ASCII table)

uppercaseLetter1 = chr(random.randint(65, 90))  # Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter2 = chr(random.randint(65, 90)) # Generate a random Uppercase letter (based on ASCII code)
lowercaseLetter1 = chr(random.randint(97, 122))  # Generate a random lowercase letter (based on ASCII code)
lowercaseLetter2 = chr(random.randint(97, 122))  # Generate a random lowercase letter (based on ASCII code)
digit1 = chr(random.randint(48, 57))  # Generate a random number (based on ASCII code)
digit2 = chr(random.randint(48, 57))  # Generate a random number letter (based on ASCII code)
punctuationSign1 = chr(random.randint(33, 47))  # Generate a random punctuation sign (based on ASCII code)
punctuationSign2 = chr(random.randint(33, 47))  # Generate a random punctuation sign (based on ASCII code)


# Generate password using all the characters, in random order
password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + \
           lowercaseLetter2 + digit1 + digit2 + punctuationSign1 + \
           punctuationSign2


# A function do shuffle all the characters of a string
def shuffle(password):
    password = list(password)
    random.shuffle(password)
    return ''.join(password)



if __name__ == '__main__':
    print(password)
