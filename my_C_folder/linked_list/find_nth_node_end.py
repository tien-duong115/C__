from linkedlist import LinkedList
from node import Node

def find_nth(lst,n):
    if lst.is_empty():
        return -1
    
    left = lst.get_head()
    right = lst.get_head()
    
    count = 0
    
    while count < n:
        if right is None:
            return -1
        right = right.next_element
        count+=1
    
    while right is not None:
        left = left.next_element
        right = right.next_element
        
    return left.data
        
    