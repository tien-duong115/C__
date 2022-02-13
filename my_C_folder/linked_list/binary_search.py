def bin_search(lst, item):
    first = 0
    last = len(lst) - 1
    found = False
    ind = -1
    
    while first <= last and not found:
        mid = (first+last) // 2
        
        if lst[mid] == item:
            ind = mid
            found = True
        else:
            if item < lst[mid]:
                last = mid - 1
            else:
                first = mid + 1
    if found:
        return ind
    else:
        return -1
    
    
def binary_search(a, item):
    first = 0
    last = len(a) - 1
    found = False
    index = -1
    while first <= last and not found:
        mid = (first + last) // 2
        if a[mid] == item:
            index = mid
            found = True
        else:
            if item < a[mid]:
                last = mid - 1
            else:
                first = mid + 1
    if found:
        return index
    else:
        return -1
    
    
mlst = [e for e in range(0,10,1)]
print(mlst)
print(bin_search(mlst, 5))
        
            