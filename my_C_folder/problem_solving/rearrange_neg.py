from turtle import right
import numpy as np


lst = np.random.randint(low=-10, high=10, size=10)



right_most_neg_index = 0

for pos in range(len(lst)):
    if lst[pos] < 0:
        if pos != right_most_neg_index:
            lst[pos] = lst[right_most_neg_index]
            lst[right_most_neg_index] = lst[pos]
        right_most_neg_index +=1
        
print(lst)
            