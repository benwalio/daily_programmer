# Input: a list
# Output: Return the two halves as different lists.
# If the input list has an odd number, the middle item can go to any of the list.
# Your task is to write the function that splits a list in two halves.


in_list = ['a', 'b', 'c', 1,2,3,4,5,1,3,2,'1']

def split_list(in_list):
   outlist_1, outlist_2 = [], []
   midpoint = len(in_list) / 2
   outlist_1 = in_list[:midpoint]
   outlist_2 = in_list[midpoint:]
   return (outlist_1, outlist_2)

out_1 = []
out_2 = []

out_1, out_2 = split_list(in_list)
print out_1
print out_2
