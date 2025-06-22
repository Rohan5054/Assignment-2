#node class
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
#linkedlist class
class LinkedList:
    def __init__(self):
        self.head= None
#add node
    def add_node(self,data):
        new_node=Node(data)
    
        if self.head is None:
            self.head=new_node

        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=new_node
#printing the list
    def print_list(self):
        if self.head is None:
            print("Empty list.")
            return

        current=self.head
        while current:
            print(current.data, end=", ")
            current=current.next
        print("None")
#delete node
    def delete_node(self,n):
        if self.head is None:
            raise Exception("List is empty. Cannot delete")

        if n<=0:
            raise Exception("Enter an index greater than or equal to 1")

        if n==1:
            self.head=self.head.next
            return

        current=self.head
        count=1

        while current is not None and count < n - 1:
            current = current.next
            count += 1

        if current is None or current.next is None:
            raise Exception("Index out of range.")
        
        current.next = current.next.next

#working->
ll = LinkedList()
ll.add_node(10)
ll.add_node(20)
ll.add_node(30)
ll.add_node(40)

print("Initial list:")
ll.print_list()

print("Deleting 2nd node:")
try:
    ll.delete_node(2)
    ll.print_list()
except Exception as e:
    print(e)

print("Deleting 10th node (invalid index):")
try:
    ll.delete_node(10)
except Exception as e:
    print(e)
