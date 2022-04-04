#User function Template for python3
'''
	Your task is to return the data stored in
	the nth node from end of linked list.
	
	Function Arguments: head (reference to head of the list), n (pos of node from end)
	Return Type: Integer or -1 if no such node exits.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
#Function to find the data of nth node from the end of a linked list
def getLen(head):

        if not head:
            return -1 

        count = 0
        itr = head

        while itr:
            count += 1
            itr = itr.next
        
        return count
        
def getNthFromLast(head,n):
    #code here
    l = getLen(head)
    
    if l < n:
        return -1
        
    itr = head
    count = 0
    x = l-n
    while itr:
        if x == count:
            return itr.data
            
        count +=1
        itr = itr.next
    