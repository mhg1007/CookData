class Node():
    def __init__ (self):
        self.data=None
        self.link=None
        self.num=0

def printNodes(start):
    count=0
    current=start
    if current.link==None:
        return
    print(current.data, end=' ')
    while current.link != start:
        current=current.link
        print(current.data, end=' ')
    print()

def findNode(findData):
    global memory,head,current,pre

    current=head
    if current.data==findData:
        return current
    while current.link != head:
        current=current.link
        if current.data==findData:
            return current
    return Node()

memory=[]
head,current,pre=None,None,None
dataArray=["다현","정연","쯔위","사나","지효"]

if __name__ == "__main__":
    count=0
    
    node=Node()
    node.data=dataArray[0]
    count=count+1
    node.num=count
    head=node
    node.link=head
    memory.append(node)

    for data in dataArray[1:]:
        pre=node
        node=Node()
        node.data=data
        count=count+1
        node.num=count
        pre.link=node
        node.link=head
        memory.append(node)

    printNodes(head)

    while True:
        fNode=findNode(input("데이터 위치 찾기 ==>"))
        
        if fNode.num>0:
            print(fNode.num, end='번째 노드')
            print()
        else:
            print("없는 데이터")
            break
        
