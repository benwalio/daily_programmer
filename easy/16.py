# Hi folks! We are in the midst of discussing how this subreddit will go about but for now how about we just concentrate on challenges!
# Write a function that takes two strings and removes from the first string any character that appears in the second string. For instance, if the first string is "Daily Programmer" and the second string is "aeiou "" the result is "DlyPrgrmmr".
# note: the second string has [space] so the space between "Daily Programmer" is removed

# in_result = raw_input("please insert your initial string - ")
# in_remove = raw_input("please insert your removal string - ")

in_result = "Daily Programmer"
in_remove = "aeiou "

out_result = in_result
i=0
j=0

for letter in in_remove:
    for other_letter in in_result:
        if letter == other_letter:
            in_result = in_result.replace(other_letter, "")
            continue
        j += 1
    i += 1

print in_result
