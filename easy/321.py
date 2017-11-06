# Description
# No more hiding from your alarm clock! You've decided you want your computer to keep you updated on the time so you're never late again. A talking clock takes a 24-hour time and translates it into words.
# Input Description
# An hour (0-23) followed by a colon followed by the minute (0-59).
# Output Description
# The time in words, using 12-hour format followed by am or pm.

input_line = raw_input("Please input the time - ")
split_input = input_line.split(":")

time_words = {
    "00":"",
    "0":"oh",
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine",
    "10":"ten",
    "11":"eleven",
    "12":"twelve",
    "13":"thirteen",
    "14":"fourteen",
    "15":"fifteen",
    "16":"sixteen",
    "17":"seventeen",
    "18":"eighteen",
    "19":"nineteen",
    "20":"twenty",
    "30":"thirty",
    "40":"fourty",
    "50":"fifty",
}

hours = split_input[0]
minutes = split_input[1]
hours_words = ""
minutes_words = ""
ampm = ""

if hours < 12:
    ampm = "am"
else:
    ampm = "pm"

hours_words = time_words[str((int(hours) % 12) or 12)]

try:
    minutes = time_words[minutes]
except KeyError:
    t, o = divmod(int(minutes), 10)
    minutes_words = '{0} {1} '.format(time_words[str(t*10)], time_words[str(o)])
print "It's {0} {1}{2}".format(hours_words, minutes_words, ampm)
