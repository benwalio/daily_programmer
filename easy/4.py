# You're challenge for today is to create a random password generator!
# For extra credit, allow the user to specify the amount of passwords to generate.
# For even more extra credit, allow the user to specify the length of the strings he wants to generate!

from random import randint

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!#$%^*-=_+/?<>,."

def genPassword(howLong):
    i = 0
    seed = 0
    result = ""

    while i < howLong:
        seed = randint(0,(len(alphabet)-1))
        result += alphabet[seed]
        i += 1
    return result

howLong = input("How long would you like the password to be? - ")

message = genPassword(howLong)
print message
