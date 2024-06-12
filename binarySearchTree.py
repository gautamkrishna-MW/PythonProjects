import random

"""
Implementing a binary search tree to sort numbers in ascending order.
"""
class binaryTree:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def addChild(self, data):
        if self.data == data:
            return

        if self.data > data:
            if self.leftChild:
                self.leftChild.addChild(data)
            else:
                self.leftChild = binaryTree(data)
        else:
            if self.rightChild:
                self.rightChild.addChild(data)
            else:
                self.rightChild = binaryTree(data)

    def treeTraverse(self):
        elements = []

        if self.leftChild:
            elements += self.leftChild.treeTraverse()
        elements.append(self.data)
        if self.rightChild:
            elements += self.rightChild.treeTraverse()

    def printTreeOrder(self):
        elements = []
        if self.leftChild:
            elements += self.leftChild.printTreeOrder()
        elements.append(self.data)
        if self.rightChild:
            elements += self.rightChild.printTreeOrder()
        return elements

def buildTree(inputArr):
    rootNode = binaryTree(inputArr[0])
    for idx in range(1,len(inputArr)):
        rootNode.addChild(inputArr[idx])

    return rootNode

if __name__ == '__main__':
    eleNum = 100
    eleArr = []
    for i in range(eleNum):
        eleArr.append(random.randint(-1000,1000))

    print(f"Input Array ({len(eleArr)}): {eleArr}")
    rootNode = buildTree(eleArr)
    outputArr = rootNode.printTreeOrder()
    print(f"Output Array ({len(outputArr)}): {outputArr}")

    # Comparing the sorted numbers with a sorted set to remove duplications.
    if outputArr == sorted(set(eleArr)):
        print("Sorted!!!")

