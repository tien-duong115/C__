from linkedlist import LinkedList
from node import Node


def remove_duplicates(self):
    if self.is_empty():
        return

    # If list only has one node, leave it unchanged
    if self.get_head().next_element is None:
        return

    outer_node = self.get_head()
    while outer_node:
        inner_node = outer_node  # Iterator for the inner loop
        while inner_node:
            if inner_node.next_element:
                if outer_node.data == inner_node.next_element.data:
                    # Duplicate found, so now removing it
                    new_next_element = inner_node.next_element.next_element
                    inner_node.next_element = new_next_element
                else:
                    # Otherwise simply iterate ahead
                    inner_node = inner_node.next_element
            else:
                # Otherwise simply iterate ahead
                inner_node = inner_node.next_element
        outer_node = outer_node.next_element
    return
