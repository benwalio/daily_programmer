# Input: list of elements and a block size k or some other variable of your choice
# Output: return the list of elements with every block of k elements reversed, starting from the beginning of the list.
# For instance, given the list 12, 24, 32, 44, 55, 66 and the block size 2, the result is 24, 12, 44, 32, 66, 55.

input_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
block_reverse = 5

def reverse_for_blocks(input_list, k_reverse):
   output_list = []
   for i in range(0,(len(input_list)/k_reverse)):
      # print len(input_list)
      # print len(input_list) / k_reverse
      # print k_reverse

      j = k_reverse - 1
      while j > -1:
         output_list.append(input_list[j])
         del(input_list[j])
         j -= 1
         # print "j = " + str(j)
         # print input_list
         # print output_list


      print "i = " + str(i)
      i += 1
   return output_list


output = reverse_for_blocks(input_list, block_reverse)
print output
