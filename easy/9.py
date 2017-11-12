# write a program that will allow the user to input digits, and arrange them in numerical order.
# for extra credit, have it also arrange strings in alphabetical order
import sys

to_sort = []
looping = True

while looping:
   cur_input = raw_input("Please input a digit or say 'done' - ")
   try:
      cur_input = int(cur_input)
      to_sort.append(cur_input)
   except:
      if cur_input == 'done':
         to_sort.sort()
         print to_sort
         sys.exit()
      else:
         print "not a valid digit - exiting"
         sys.exit()
