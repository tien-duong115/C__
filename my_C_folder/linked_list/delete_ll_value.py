
def delete(lst, value):
    deleted = False
    
    if(lst.is_empty()):
        print('empty list')
        return False
    
    current_node = lst.get_head()
    previous_node = None
    
    while current_node.data == value:
        current_node.delete_at_head()
        deleted =True
        return deleted
    
    while current_node is not None:
        
        if current_node.data == value:
            previous_node.next_element = current_node.next_element
            current_node.next_element = None
            deleted = True
            break
        previous_node = current_node
        current_node = current_node.next_element
        
        
    if (deleted is False):
        print(str(value), " is not in List!" )
    else:
        print(str(value), " is in the List! and Deleted")
        
        

lst = LinkedList()
lst.insert_at_head(1)
lst.insert_at_head(4)
lst.insert_at_head(3)
lst.insert_at_head(2)
lst.print_list()
delete(lst, 4)
lst.print_list()
