def merge_sort(lst):
    
    if len(lst) > 1:
        mid = len(lst) //2
        left = lst[:mid]
        right = lst[mid:]
        
        
        merge_sort(left)
        merge_sort(right)
        
        i = j = k = 0 
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i +=1
            else:
                lst[k] = right[j]
                j+=1
            k +=1
            
        while i < len(left):
            lst[k] = left[i]
            k +=1
            i +=1
            
        while j < len(right):
            lst[k] = right[j]
            k+=1
            j+=1
    return lst

lst = [ 9,2,6,3,10]

print(merge_sort(lst))
            