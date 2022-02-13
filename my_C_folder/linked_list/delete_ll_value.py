from LinkedList import LinkedList
from Node import Node


# def delete(lst, value):
#     deleted = False
#     if lst.is_empty():  # Check if list is empty -> Return False
#         print("List is Empty")
#         return deleted
#     current_node = lst.get_head()  # Get current node
#     previous_node = None  # Get previous node
#     if current_node.data == value:
#         lst.delete_at_head()  # Use the previous function
#         deleted = True
#         return deleted

#     # Traversing/Searching for Node to Delete
#     while current_node is not None:
#         # Node to delete is found
#         if value == current_node.data:
#             # previous node now points to next node
#             previous_node.next_element = current_node.next_element
#             current_node.next_element = None
#             deleted = True
#             break
#         previous_node = current_node
#         current_node = current_node.next_element

#     if deleted == False:
#         print(str(value) + " is not in list!")
#     else:
#         print(str(value) + " deleted!")

#     return deleted


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
