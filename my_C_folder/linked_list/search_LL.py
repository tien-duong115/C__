from linkedlist import LinkedList

from node import node


def search(lst, value):
    
    if lst.get_head() is None:
        print('empty LL')
        return
    tmp = lst.get_head()
    
    while tmp.next_element:
        if tmp.next_element == value:
            return value
        tmp = tmp.next_element
        
            
        