# Welcome to cipher day!
# write a program that can encrypt texts with an alphabetical caesar cipher. This cipher can ignore numbers, symbols, and whitespace.
# for extra credit, add a "decrypt" function to your program

import sys

togEorD = raw_input("Would you like to (e)ncode or (d)ecode? - ")
message = raw_input("What is your message? - ")
cipherShift = input("What is your shift? - ")

alphabet = "abcdefghijklmnopqrstuvwxyz"

outMessage = ""

def encodeCaesar(message, cipherShift):
    result = ""
    for i in message.lower():
        l = (alphabet.index(i) + cipherShift) % 26
        result += alphabet[l]

    return result.lower()

def decodeCaesar(message, cipherShift):
    result = ""
    for i in message.lower():
        l = (alphabet.index(i) - cipherShift) % 26
        result += alphabet[l]

    return result.lower()

if togEorD == "e":
    outMessage = encodeCaesar(message, cipherShift)
elif togEorD == "d":
    outMessage = decodeCaesar(message, cipherShift)
else:
    sys.exit()

print(outMessage)
