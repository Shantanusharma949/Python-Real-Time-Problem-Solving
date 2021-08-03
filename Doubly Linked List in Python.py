class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class Linked_list:
    def __init__(self):
        self.head=None
    
    def traverse(self):
        temp=self.head
        print("Linked List: ")
        while(temp):
            print(temp.data)
            p=temp
            temp=temp.next
    
        print("Reverse Linked List: ")
        while(p):
            print(p.data)
            p=p.prev
    

linked_list_01=Linked_list()
linked_list_01.head=Node(1)
second=Node(2)
third=Node(3)

linked_list_01.head.next=second
second.prev=linked_list_01.head
second.next=third
third.prev=second

linked_list_01.traverse()

            
        
        