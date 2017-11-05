# Welcome to cipher day!
# write a program that can encrypt texts with an alphabetical caesar cipher. This cipher can ignore numbers, symbols, and whitespace.
# for extra credit, add a "decrypt" function to your program

import sys

togEorD = input("Would you like to (e)ncode or (d)ecode? - ")
message = input("What is your message? - ")
cipherShift = input("What is your shift? - ")

def encodeCaesar(message, cipherShift):
    

def decodeCaesar(message, cipherShift):




if togEorD == "e":
    encodeCaesar(message, cipherShift)
elif togEorD == "d":
    decodeCaesar(message, cipherShift)
else:
    sys.exit()
