class Node():
    def __init__ (self):
        self.data=None
        self.link=None

def printNodes(start):
    count=0
    current=start
    if current.link==None:
        return
    print(current.data, end=' ')
    while True:
        count=count+1
        if count>=100:
            break
        current=current.link
        print(current.data, end=' ')
    print()

memory=[]
head,current,pre=None,None,None
dataArray=["다현","정연","쯔위","사나","지효","현규"]

if __name__ == "__main__":
    
    node=Node()
    node.data=dataArray[0]
    head=node
    node.link=head
    memory.append(node)

    for data in dataArray[1:]:
        pre=node
        node=Node()
        node.data=data
        node.num=cnt
        pre.link=node
        node.link=head
        memory.append(node)

    printNodes(head)

