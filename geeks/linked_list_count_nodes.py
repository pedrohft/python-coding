#User function Template for python3

'''

#Linked list class
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        '''
class Solution:
    
    #Function to count nodes of a linked list.
    def getCount(self, head_node):
        #code here
        count = 0
        itr = head_node
        while itr:
            count+=1
            itr = itr.next
        return count