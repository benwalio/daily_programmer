# Write a program that can translate Morse code in the format of ...---...
# A space and a slash will be placed between words. ..- / --.-
# For bonus, add the capability of going from a string to Morse code.
# Super-bonus if your program can flash or beep the Morse.
# This is your Morse to translate:
# .... . .-.. .-.. --- / -.. .- .. .-.. -.-- / .--. .-. --- --. .-. .- -- -- . .-. / --. --- --- -.. / .-.. ..- -.-. -.- / --- -. / - .... . / -.-. .... .- .-.. .-.. . -. --. . ... / - --- -.. .- -.--

morse_alphabet = ('.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..')
alphabet = "abcdefghijklmnopqrstuvwxyz"
out_message = ""

in_message = raw_input("Please enter your message - ")

for i in in_message.lower():
    l = in_message.index(i)
    print "i : " + str(i) + "\nl : " + str(l)
    out_message += alphabet[l]

print out_message
