#Your task is to complete this function
#Your function should print the data in one line only
#You need not to print new line

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''
class Solution:
    def display(self,node):
        #code here
        itr = node
        while itr:
            
            print(str(itr.data), end=" ")
            itr = itr.next
