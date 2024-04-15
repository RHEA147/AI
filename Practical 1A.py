#BFS

from collections import deque
class MyGraph():
    def __init__(self,cmap,i,g):
        self.citymap=cmap
        self.init=i
        self.goal=g
    def goal_test(self,anode):
        if anode ==  self.goal:
            return True
        else:
            return False
    def getLinks(self,anode):
        #return a list of nodes connected with the given node
        return list(self.citymap[anode].keys())
    
def breadth_first_search(citygraph):
    node=citygraph.init
    if citygraph.goal_test(node):
        return node
    frontier = deque ([node])
    explored = set()

    while frontier:
        node=frontier.popleft()
        explored.add(node)

        if citygraph.goal_test(node):
            return node
        for action in citygraph.getLinks(node):
            child = action
            if child not in explored and child not in frontier:
                if citygraph.goal_test(child):
                    return child
                frontier.append(child)

cities={
    'Jaipur':{'Mumbai':500,'Nashik':650},
    'Mumbai':{'Jaipur':500,'Pune':150, 'Delhi':230},
    'Nashik':{'Jaipur' :789 ,'Agra':450 },
    'Pune' : {'Mumbai':100, 'Hyderabad':120}
}
incities = MyGraph(cities,'Mumbai','Jaipur')
finalnode = breadth_first_search(incities)
if  finalnode is not None:
    print("path exists")
else:
    print("path doesnt exists")