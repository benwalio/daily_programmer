# Write a program that will compare two lists, and append any elements in the second list that doesn't exist in the first.
# input: ["a","b","c",1,4,], ["a", "x", 34, "4"]
# output: ["a", "b", "c",1,4,"x",34, "4"]


input1 = ["a","b","c",1,4,]
input2 = ["a", "x", 34, "4"]

def append_differences(array1, array2):
   for element in array2:
      if element not in array1:
         array1.append(element)

   return array1

output = append_differences(input1, input2)
print output
