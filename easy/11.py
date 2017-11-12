# The program should take three arguments. The first will be a day, the second will be month, and the third will be year. Then, your program should compute the day of the week that date will fall on.

from calendar import weekday, day_name

arg1 = raw_input("arg 1 - ")
arg2 = raw_input("arg 2 - ")
arg3 = raw_input("arg 3 - ")

arg1 = int(arg1)
arg2 = int(arg2)
arg3 = int(arg3)

print day_name[weekday(arg3, arg2, arg1)]
