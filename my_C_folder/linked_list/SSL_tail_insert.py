# Inserts a value at the end of the list
from node import node
from linkedlist import LinkedList

def insert_at_tail(lst, value):
    # Write - Your - Code
    new_val = node(value)
    if lst.get_head() is None:
        lst.head_node = new_val
        return 
    
    tmp = lst.get_head()

    while tmp.next_element:
        tmp = tmp.next_element
    
    tmp.next_element = new_val
    return 

lst = LinkedList()
lst.print_list()
insert_at_tail(lst, 0)
lst.print_list()
insert_at_tail(lst, 1)
lst.print_list()
insert_at_tail(lst, 2)
lst.print_list()
insert_at_tail(lst, 3)
lst.print_list()