class Node:
    def __init__(self,data):
        self.data= data
        self.next= None
        self.prve =None
class Doublylinkedlist:
    def __init__(self):
        self.head=None

    def setdata(self,data):
        self.data=data
    def getdata(self):
        return self.data
    def setnext(self,next):
        self.next=next
    def getnext(self):
        return self.next
dllist=Doublylinkedlist()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(2)
dllist.append(5)



