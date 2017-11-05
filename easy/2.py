# Hello, coders! An important part of programming is being able to apply your programs, so your challenge for today is to create a calculator application that has use in your life. It might be an interest calculator, or it might be something that you can use in the classroom. For example, if you were in physics class, you might want to make a F = M * A calc.
# EXTRA CREDIT: make the calculator have multiple functions! Not only should it be able to calculate F = M * A, but also A = F/M, and M = F/A!

import sys

iSelect = raw_input("What kind of calculation would you like to do ? - ")

def compoundCalc():
    iPrincipal = input("What is your principal investment? - ")
    iInterest = input("What is the interest rate? - ")
    iOccur = input("How many times a year is this compounded? - ")
    iTime = input("How long until this investment matures (in years)? - ")

    if iInterest > 1:
        iInterest = iInterest / 100

    rOverN = iInterest/iOccur
    rONPlusOne = rOverN + 1
    occurTime = iOccur * iTime
    rONPOtooT = rONPlusOne ** occurTime
    amount = iPrincipal * rONPOtooT

    print "The amount will be - " + str(amount)

    sys.exit

if iSelect == "compound":
    compoundCalc()
else:
    sys.exit()
