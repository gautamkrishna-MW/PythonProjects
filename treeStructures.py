
"""
Build this tree:

|--Nilupul (CEO)
  |--Chinmay (CTO)
    |--Vishwa (Infra Head)
      |--Dhaval (Cloud Manager)
      |--Abhijit (App Manager)
    |--Aamir (Application Head)
  |--Gels (HR Head)
    |--Peter (Recruitment Head)
    |--Waqas (Policy Manager)

"""
class TreeNode:
    def __init__(self, data, desig):
        self.data = data
        self.desig = desig
        self.children = []
        self.parent = None

    def addChild(self, child):
        child.parent = self
        self.children.append(child)

    def getDepth(self):
        depthVal = 0
        currNode = self
        while currNode.parent is not None:
            depthVal += 1
            currNode = currNode.parent
        return depthVal

    def printTree(self):
        print((" "*self.getDepth()*2) + f"|--{self.data} ({self.desig})")
        for child in self.children:
            child.printTree()



def buildTree():
    rootNode = TreeNode("Nilupul", "CEO")
    rootNode.addChild(TreeNode("Chinmay", "CTO"))
    rootNode.addChild(TreeNode("Gels", "HR Head"))

    rootNode.children[0].addChild(TreeNode("Vishwa", "Infra Head"))
    rootNode.children[0].addChild(TreeNode("Aamir", "Application Head"))
    rootNode.children[1].addChild(TreeNode("Peter", "Recruitment Head"))
    rootNode.children[1].addChild(TreeNode("Waqas", "Policy Manager"))

    rootNode.children[0].children[0].addChild(TreeNode("Dhaval", "Cloud Manager"))
    rootNode.children[0].children[0].addChild(TreeNode("Abhijit", "App Manager"))

    return rootNode

if __name__ == "__main__":
    rootNode = buildTree()
    rootNode.printTree()