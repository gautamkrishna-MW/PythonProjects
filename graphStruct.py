
class graphStruct:

    def __init__(self, edges):
        self.edges = edges
        self.dictGraph = {}
        for src,dst in self.edges:
            if src in self.dictGraph:
                self.dictGraph[src].append(dst)
            else:
                self.dictGraph[src] = [dst]

    def getPaths(self, src, dst):
        outputList = []
        if dst in self.dictGraph[src]:
            outputList.append(src)
            outputList.append(dst)
        else:
            for newSrcIdx in self.dictGraph[src]:
                if newSrcIdx in self.dictGraph:
                    outputSubList = self.getPaths(newSrcIdx, dst)
                    if outputSubList:
                        outputList.append(src)
                        outputList.append(outputSubList)
        return outputList

    def printGraph(self):
        print(self.dictGraph)


if __name__ == '__main__':

    routes = [
        ("Mumbai","Pune"),
        ("Mumbai", "Surat"),
        ("Surat", "Bangaluru"),
        ("Pune","Hyderabad"),
        ("Pune","Mysuru"),
        ("Hyderabad","Bangaluru"),
        ("Hyderabad", "Chennai"),
        ("Mysuru", "Bangaluru"),
        ("Chennai", "Bangaluru"),
        ("Chennai", "Mumbai")
    ]

    graphObj = graphStruct(routes)
    graphObj.printGraph()
    print(graphObj.getPaths("Mumbai", "Bangaluru"))
    print(graphObj.getPaths("Mumbai", "Chennai"))
    print(graphObj.getPaths("Chennai", "Hyderabad"))
