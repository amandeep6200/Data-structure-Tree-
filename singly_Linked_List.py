class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class linked_List:
       def __init__(self):
           self.head=None
       def insert(self,item):
           new_node=Node(item)
           new_node.next=self.head
           self.head=new_node
       def print_List(self):
           temp=self.head
           while temp:
               print(temp.val,end=" ")
               temp=temp.next
       def reverse(self):
           prev=None
           curr=self.head
           while curr:
               next=curr.next
               curr.next=prev
               prev=curr
               curr=next
           self.head=prev
       def detect_loop(self):
           slow=self.head
           fast=self.head
           while slow and fast and fast.next:
               slow=slow.next
               fast=fast.next.next
               if slow==fast:
                   return "Loop is present"
           else:
               return "No Loop"
       def remove_loop(self):
           slow=self.head
           fast=self.head
           while slow and fast and fast.next:
               if slow==fast:
                   print("loop detected")
                   break
               slow=slow.next
               fast=fast.next.next
           if slow==fast:
               slow=self.head
               while slow.next!=fast.next:
                   slow=slow.next
                   fast=fast.next
               fast.next=None
llist=linked_List()
llist.insert(4)
llist.insert(3)
llist.insert(2)
llist.insert(1)
llist.reverse()
llist.print_List()
               
            
               
           
        
