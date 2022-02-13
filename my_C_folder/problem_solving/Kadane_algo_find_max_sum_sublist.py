
import random as r
from random import seed

# r.seed(10)
lst =  [e for e in range(10)]


def max_sub_list(lst):
    
    if len(lst) < 1:
        return 0
    
    curr_max = lst[0]
    
    max_max = lst[0]
    
    for i in range(1,len(lst)):
        if curr_max < 0:
            curr_max = lst[i]
            
        else:
            
            curr_max  += lst[i]
            
        if max_max < curr_max:
            max_max = curr_max
    return max_max
lst = [-4, 2, -5, 1, 2, 3, 6, -5, 1];
print("Sum of largest subarray: ", max_sub_list(lst));

