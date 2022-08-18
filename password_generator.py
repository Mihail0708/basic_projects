import random


def shuffle(string):
    random.shuffle(string)
    return ''.join(string)


password = []

for letter in range(6):
    password.append(chr(random.randint(65, 90)))

for num in range(3):
    password.append(chr(random.randint(48, 57)))


password = shuffle(password)


print(password)
