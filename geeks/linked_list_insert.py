'''    
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
class Solution:
    #Function to insert a node at the beginning of the linked list.
    def insertAtBegining(self,head,x):
        n = Node(x)
        
        if not head:
            n.next = None
        else:
            n.next = head
            
        head=n

        return head 
    #Function to insert a node at the end of the linked list.
    def insertAtEnd(self,head,x):
        # code here 
        n = Node(x)
        
        if not head:
            n.next = None
            head = n
        
        else:   
            it = head
            while it.next:
                it = it.next
            
            it.next = n
        
        return head