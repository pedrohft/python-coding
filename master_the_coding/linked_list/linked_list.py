from msilib.schema import SelfReg


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1   

    def prepend(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length += 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1

    def print_list(self):
        if self.head == None:
            print("Empty")
        else:
            current_node = self.head
            while current_node != None:
                print(current_node.data, end="-->")
                current_node = current_node.next

    def insert(self, position, data):
        if position >= self.length:
            if position>self.length:
                print("This position is not available. Inserting at the end of the list")
            self.append(data)
        elif position == 0:
            self.prepend(data)
        else:
            new_node = Node(data)
            current_node = self.head
            for i in range(position-1):
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node
            self.length += 1
            
    def remove_by_position(self, position):
        if self.head == None:
            print("Linked List is empty. Nothing to delete.")
            return
        if position == 0:
            self.head = self.head.next
            if self.head == None or self.head.next == None:
                self.tail = self.head
            self.length -= 1
            return 
        if position >= self.length:
            position = self.length-1
        current_node = self.head    
        for i in range(position - 1):
            current_node = current_node.next
        current_node.next = current_node.next.next
        self.length -= 1
        if current_node.next == None:
            self.tail = current_node
        return        
    
    def remove_by_value(self, data):
        if self.head == None:
            print("Linked List is empty. Nothing to delete.")
            return
        current_node = self.head
        if current_node.data == data:
            self.head = self.head.next
            if self.head == None or self.head.next == None:
                self.tail = self.head
            self.length -= 1
        
        while current_node != None and current_node.next.data != data:
            current_node = current_node.next
        
        if current_node.next != None:
            current_node.next = current_node.next.next

            if current_node.next ==  None:
                self.tail = current_node

            self.length -= 1  
        else:
            print("Given value not found.")

    #leetcode_removeElementes
    def removeElements(self, val):
        if self.head == None:
            return []
        if self.head.data == val:
            self.head =  self.head.next
        
        itr =  self.head
        while itr.next:
            
            if itr.next.data == val:
                itr.next = itr.next.next

            itr = itr.next


if __name__ == '__main__':
    my_linked_list = LinkedList()
    my_linked_list.print_list()
    my_linked_list.append(5)
    my_linked_list.append(2)
    my_linked_list.append(9)
    my_linked_list.print_list()
    print("\n")
    my_linked_list.prepend(4)
    my_linked_list.print_list()
    print('\n')
    my_linked_list.insert(5, 10)
    my_linked_list.print_list()
    print('\n')
    my_linked_list.insert(0, 11)
    my_linked_list.print_list()
    print("\n")
    my_linked_list.insert(3, 6)
    my_linked_list.print_list()
    print("\n")
    my_linked_list.remove_by_position(2)
    my_linked_list.print_list()
    print("\n")
    my_linked_list.remove_by_value(9)
    my_linked_list.print_list()
    print("\n")
    my_linked_list.removeElements(2)
    my_linked_list.print_list()