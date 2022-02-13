from linkedlist import LinkedList
from node import node

def search(node, value):
    # base case
    if (not node):
        return False
    
    if (node.data is value):
        return True
    
    return search(node.next_element, value)

lst = LinkedList()
lst.insert_at_head(4)
lst.insert_at_head(10)
lst.insert_at_head(40)
lst.insert_at_head(5)
lst.print_list()
print(search(lst.get_head(), 4))
