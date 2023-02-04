import re
import numpy as np

# read inputs
int_range = input() 
array = input() # there are two separate inputs, one int one list

###
# function to define template for output
def template(array):
    template = ""

    #store first consecutive string list as template
    for i in range(len(array)):
        if array[i] != " ":
            template += array[i]
        else:
            break
    return template

template = template(array)
###
def sum_answer(template,array):
    int_sum = 0 # used to find the sum of the elements in the array

    # string group is defined everytime we encounter a " "
    for i in np.arange(len(array)):
        if array[i] == " ":
            # finds the integer of each string group, range is defined by length of each string group (aka template)
            strings = ""
            for n in np.arange(len(str(template))):
                strings += array[n-i]
            #print(strings)
            int_sum += int(strings)

    strings = ""
    for n in np.arange(len(str(template))):
        strings += array[n]
    #print(strings)
    int_sum += int(strings)

    return int_sum

print(sum_answer(template,array))
