#------Linked List-----

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class ll:
    def __init__(self):
        self.head=None
        
    #----print Linked List
    
    def print(self):
        if self.head is None:
            print("LL is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data )
                n=n.next
    #---add element at begin
    def add_begin(self,data):
        new_node=node(data)
        new_node.next=self.head
        self.head=new_node
        
    #---add element at end
    def add_end(self,data):
        new_node=node(data)
        n=self.head
        if n is None:
            self.head=new_node
        else:
            while n.next is not None:
                n=n.next
            n.next=new_node

    #---add element at index
    def add_index(self,index,data):
        new_node=node(data)
        if(self.head==None or index==1):
            self.add_begin(data)
            return
    
        temp=self.head
        for i in range(0,index-1):
            temp=temp.next
        new_node.next=temp.next
        temp.next=new_node  
            
    #---delete element at begin
    def del_begin(self):
        if(self.head==None):
            print("LL is empty")
        if( self.head.next==None):
            print("LL is empty")
        n=self.head
        self.head=n.next

    #---delete element at end
    def del_end(self):
        if(self.head==None):
            print("LL is empty")
        if( self.head.next==None):
            print("LL is empty")
        temp=self.head
        while(temp.next.next!=None):
            temp=temp.next
        temp.next=None

    #---delete element at index
    def del_index(self,index):
        if(self.head==None):
            print("LL is empty")
        if(index==1):
            self.del_begin()
            return
        temp=self.head
        for i in range(0,index-2):
            temp=temp.next
        temp.next=temp.next.next

    #----update data at given index
    def update(self,index,data):
        if(self.head==None):
            print("LL is empty")
        temp=self.head
        for i in range(0,index-1):
            temp=temp.next
        temp.data=data
   
        
n=ll()
n.add_begin(20)
n.add_begin(40)
n.add_begin(80)
n.add_begin(100)
n.add_end(20)
n.add_index(1,500)
n.print()
n.del_begin()
n.del_index(2)
n.del_end()
print("Updated List: \n")
n.update(2,30)
n.print()

        
