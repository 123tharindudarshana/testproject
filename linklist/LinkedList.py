from Node import Node
class linkedist:
    def __init__(self):
        self.head=Node()
    def listlenth(self):
        current=self.head
        count=0
        while current is not None:
            count=count+1
            #print(current. getData())
            current =current.getNext()
        return count


    def addNodeBeginning(self,data):
        newNode=Node()
        newNode.setData(data)

        if self.head is None:
            self.head=newNode
        else:
            newNode.setNext(self.head)
            self.head=newNode
        self.length+1





        def addNodeEnd(self,data):
            newNode=Node()
            newNode.setData(data)

            if self.head is None:
                self.head=newNode
            else:
                current=self.head
                while current is not None:
                    current =current.getNext()
                current.setNext(newNode)
                newNode.setNext(None)
            self.length+=1




    def addNodeInpos(self,pos,data):
        if pos>self.length-1 or pos<0:
            return None
        elif pos==0:
            self.addNodeBeginning(data)
        elif pos == self.length -1:
            self.addNodeEnd(data)
        elif pos ==self.length-1:
            self.addNodeEnd(data)
        else:
            newNode=Node()
            newNode.setData(data)
            count=0
            current =self.head

           # while count !=pos -1:
                #count=0
                #current=










