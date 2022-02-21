from linkedlist import LinkedList
from node import Node

def find_mid(lst):
    
    #edge cases
    
    #if empty list return last element
    if lst.is_empty():
        return -1
    
    curr_node = lst.get_head()
    
    #if only one element within the linkedlist edge case
    if curr_node.next_element == None:
        return curr_node.data
    
    # two pointer generating
    mid_node = curr_node
    curr_node = curr_node.next_element.next_element
    
    
    while curr_node:
        mid_node = mid_node.next_element
        curr_node = curr_node.next_element
        
        if curr_node:
            curr_node = curr_node.next_element
    if mid_node:
        return mid_node.data
    
    return -1
    

lst = LinkedList()
lst.insert_at_head(22)
lst.insert_at_head(21)
lst.insert_at_head(10)
lst.insert_at_head(14)
lst.insert_at_head(7)

lst.print_list()
print(find_mid(lst))    
    

    