# your task is to complete this function

'''
class node:
    def __init__(data):
        self.data = data
        self.next = None
'''
class Solution:
    #  Should return data of middle node. If linked list is empty, then  -1
    def getLen(self, head):

        if not head:
            return -1 

        count = 0
        itr = head

        while itr:
            count += 1
            itr = itr.next
        
        return count

    def findMid(self, head):

        l = self.getLen(head)
        m = (l//2)
        count = 0
        itr = head

        while itr:
            if count == m:
                return itr.data

            count +=1
            itr = itr.next