class node:
    
    def __init__(self, data):
        self.data = data 
        self.next_node = None
        

class linkedlist:
    
    def __init__(self):
        self.head_node = None
        
    def insert_head(self, data):
        temp = node(data)
        
        temp.next_node = self.head_node
        
        self.head_node = temp
        return self.head_node
    
    
    def is_empty(self):
        if (self.head_node is None):
            return True
        else:
            return False
        
    # def print_linkedlist(self):
    #     if (self.is_empty()):
    #         print("is empty")
    #         return False
        
    #     temp = self.head_node
        
    #     while temp.next_node is not None:
    #         print(temp.data, end='->')
    #         temp = temp.next_node
        
    #     print(temp.data , '-> None')
    #     return True
    
    def print_list(self):
        if(self.is_empty()):
            print("List is Empty")
            return False
        temp = self.head_node
        while temp.next_node is not None:
            print(temp.data, end=" -> ")
            temp = temp.next_node
        print(temp.data, "-> None")
        return True


lst = linkedlist()

lst.print_list()

for i in range(1,10):
    lst.insert_head(i)
lst.print_list()