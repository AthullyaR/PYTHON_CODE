class Node:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
    
class Sol:
    def addtwonumbers(self,l1,l2):
        added=Node(val=(l1.val+l2.val)%10)
        carry=(l1.val+l2.val)//10
        current=added

        while(l1.next and l2.next):

            l1=l1.next
            l2=l2.next
            current.next=Node(val=(carry+l1.val+l2.val)%10)
            carry=(carry+l1.val+l2.val)//10
            current=current.next

        while(l1.next):
            l1=l1.next
            current.next=Node(val=(carry+l1.val)%10)
            carry=(carry+l1.val)//10
            current=current.next

        while(l2.next):
            l2=l2.next
            current.next=Node(val=(carry+l2.val)%10)
            carry=(carry+l2.val)//10
            current=current.next

        if(carry>0):
            current.next=Node(val=1)

        return(added)
    
class SLinkedlist:
    def __init__(self):
        self.head=None

    def printl(self):
        printval=self.head
        
        while printval is not None:
            print(printval.val)
            printval=printval.next

    #inserting element at front
    def add(self,new):
        new_node=Node(new)
        
        new_node.next=self.head
        self.head=new_node

    def addrear(self,new):
        if self.head==None:
            self.head=Node(new)
            return
        
        new_node=Node(new)
        link=self.head
        while link.next!=None:
            link=link.next
        link.next=new_node
        new_node.next=None

    
        
    
l=SLinkedlist()

n=int(input("enter number of nodes"))
values1=list(map(int,input().split(" ")))
for i in range(n):
    
    l.addrear(values1[i])
  #  list=list.next


l2=SLinkedlist()

n=int(input("enter number of nodes"))
values2=list(map(int,input().split(" ")))
for i in range(n):
    
    l2.addrear(values2[i])

#sum=SLinkedlist()
#sum=l.addtwonumbers(l,l2)


