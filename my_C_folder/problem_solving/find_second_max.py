def second_max(lst):
    
    if len(lst) < 2:
        return 
    
    max_no = second_max = 0
    
    for i in range(len(lst)):
        if lst[i] > max_no:
            sec_max_no = max_no
            max_no = lst[i]
        elif sec_max_no < lst[i] and lst[i] != max_no:
            sec_max_no = lst[i]
            
    return sec_max_no

print(second_max([9, 2, 3, 6]))

            
    
    