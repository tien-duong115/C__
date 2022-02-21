from linkedlist import LinkedList
from node import Node
# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Delete at head => list.delete_at_head()
# Delete by value => list.delete(value)
# Search for element => list.search()
# Length of the list => list.length()
# Remove duplicates => list.remove_duplicates()
# Node class  {int data ; Node next_element;}

# Returns a list containing the union of list1 and list2

def union(list1, list2):
    if list1.is_empty():
        return list1
    if list2.is_empty():
        return list2

    curr_node = list1.get_head()
    while curr_node.next_element:
        curr_node = curr_node.next_element

    curr_node.next_element = list2.get_head()

    list1.remove_duplicates()
    return list1


def intersection(list1, list2):

    res = LinkedList()
    curr = list1.get_head()

    while curr is not None:
        val = curr.data
        if (list2.search(val) is not None):
            res.insert_at_head(val)
        curr = curr.next_element
    res.remove_duplicates()
    return res

    
        