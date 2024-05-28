
""" Class defining the Node of the Linked List. """
class Node:
    data: float

    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.__next = next
        self.__prev = prev

    def GetNextNode(self):
        return self.__next

    def SetNextNode(self, node=None):
        self.__next = node

    def GetPrevNode(self):
        return self.__prev

    def SetPrevNode(self, node=None):
        self.__prev = node

""" Class building the linked list and operating on it. """
class LinkedList:
    head: Node
    tail: Node
    length: int

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def getLength(self):
        return self.length

    # Insert Node at start of LL
    def insertNodeAtStart(self, data):
        nodeObj = Node(data, self.head)
        self.head = nodeObj
        self.length += 1

    # Insert Node at end of LL
    def insertNodeAtEnd(self, data):
        self.insertNode(data, self.length)

    # Insert Node at a certain index
    def insertNode(self,data,index):
        if index == 0:
            self.insertNodeAtStart(data)
            return

        idx: int = 0
        currNode = self.head
        while idx < index:
            prevNode = currNode
            currNode = currNode.GetNextNode()
            idx+=1
        nodeObj = Node(data,currNode, prevNode)
        prevNode.SetNextNode(nodeObj)
        self.length += 1

    # Removing Node from LL
    def removeNode(self,index):
        if index == 0:
            self.head = self.head.GetNextNode()
            self.head.SetPrevNode(None)
            self.length -= 1
            return

        idx: int = 0
        currNode = self.head
        while idx < index:
            currNode = currNode.GetNextNode()
            idx += 1
        prevNode: Node = currNode.GetPrevNode()
        prevNode.SetNextNode(currNode.GetNextNode())
        self.length -= 1

    # Add list of data
    def insertList(self, data_list):
        for items in data_list:
            self.insertNodeAtStart(items)

    # Print LL
    def printLL(self):
        if self.length == 0:
            print("Empty Linked list")
        else:
            llStr = ''
            currNode = self.head
            while True:
                llStr += str(currNode.data) + "--->"
                currNode = currNode.GetNextNode()
                if currNode.GetNextNode() is None:
                    llStr += str(currNode.data) + " Length:" + str(self.length)
                    break
            print(llStr)


if __name__ == '__main__':
    llObj = LinkedList()
    llObj.insertNodeAtStart(5)
    llObj.insertNodeAtStart(15)
    llObj.insertNodeAtStart(82)
    llObj.insertNodeAtStart(58)
    llObj.printLL()
    llObj.insertNodeAtEnd(52)
    llObj.insertNodeAtEnd(45)
    llObj.printLL()
    llObj.insertNode(95,3)
    llObj.printLL()
    llObj.insertNode(73,5)
    llObj.printLL()
    llObj.removeNode(0)
    llObj.printLL()
    llObj.removeNode(2)
    llObj.printLL()
    llObj.insertList([21,34, 56,65, 82, 70, 32])
    llObj.printLL()