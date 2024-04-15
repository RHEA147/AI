#AStar

from myutils import *
infinity = float('inf')
class MyGraph:
    def __init__(self, cmap, lcs, i, g):
        self.citymap = cmap
        self.init = i
        self.goal = g
        self.locs = lcs
    def goal_test(self,anode):
        if anode==self.goal:
            return True
        else:
            return False
    def getLinks(self, anode):
        return list(self.citymap[anode].keys())

    def h(self, node):        
        if self.locs:
            return int(distance(self.locs[node], self.locs[self.goal]))             
        else:
            return infinity

    def getMin(self,alist):       
        minind=-1
        minf=list(alist[0])[0] #first f value from the list
        for i in range(0, len(alist)) :            
            t = list(alist[i])[0]         
            if minf >= t:
                minf= t
                minind = i
        return minind
    
def astar_search(problem): # based on fig 3.24
    node = problem.init
    if problem.goal_test(node):
        return node
    gval = 0 # start to node n
    hval = problem.h(node) # estimated cheapest from n to goal
    #each entry in list represents a dictionary item with key as f-val and value as node with path   
    nodelist = [{gval+hval:[node]}]    
    while nodelist:
        print("\nNodelist :\n", nodelist)
        min = problem.getMin(nodelist)        
        entry = nodelist[min]
        minnode = entry[list(entry.keys())[0]][-1]
        minfval = list(entry.keys())[0]
        print("-- minimum distance - ", minfval, ", min node ", minnode)
        if(problem.goal_test(minnode)):            
            return entry[list(entry.keys())[0]] , minfval
        entry = nodelist.pop(min)        
        for child in problem.getLinks(minnode):
            # gvalue of child equals cost of minnode to child + f cost of minnode - h cost of minnode
            gval =  problem.citymap[minnode][child] + minfval - problem.h(minnode)
            hval = problem.h(child)            
            newlist = entry[list(entry.keys())[0]].copy()            
            newlist.append(child)            
            nodelist.append( {gval+hval : newlist})        
        input("press any key to continue...")
    return "not found"

romania_map = {'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},     
     'Bucharest': {'Urziceni': 85, 'Pitesti': 101, 'Giurgiu': 90, 'Fagaras': 211},
     'Craiova': {'Drobeta': 120, 'Rimnicu': 146, 'Pitesti': 138},
     'Drobeta': {'Mehadia': 75, 'Craiova': 120},
     'Eforie': {'Hirsova': 86},'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
     'Hirsova': {'Urziceni': 98, 'Eforie': 86},
     'Iasi': {'Vaslui': 92, 'Neamt': 87},
     'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
     'Oradea': {'Zerind': 71, 'Sibiu': 151},
     'Pitesti': {'Rimnicu': 97, 'Bucharest': 101, 'Craiova': 138},
     'Rimnicu': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
     'Urziceni': {'Vaslui': 142, 'Bucharest': 85, 'Hirsova': 98},
     'Zerind': {'Arad': 75, 'Oradea': 71},
     'Sibiu': {'Arad': 140, 'Fagaras': 99, 'Oradea': 151, 'Rimnicu': 80},
     'Timisoara': {'Arad': 118, 'Lugoj': 111},
     'Giurgiu': {'Bucharest': 90}, 'Mehadia': {'Drobeta': 75, 'Lugoj': 70},
     'Vaslui': {'Iasi': 92, 'Urziceni': 142},    'Neamt': {'Iasi': 87}}

locations = dict( Arad=(91, 492), Bucharest=(400, 327), Craiova=(253, 288),
    Drobeta=(165, 299), Eforie=(562, 293), Fagaras=(305, 449),
    Giurgiu=(375, 270), Hirsova=(534, 350), Iasi=(473, 506),
    Lugoj=(165, 379), Mehadia=(168, 339), Neamt=(406, 537),
    Oradea=(131, 571), Pitesti=(320, 368), Rimnicu=(233, 410),
    Sibiu=(207, 457), Timisoara=(94, 410), Urziceni=(456, 350),
    Vaslui=(509, 444), Zerind=(108, 531))
    


print("\nSolving for arad to bucharest...")
romania = MyGraph(romania_map, locations, 'Arad','Bucharest' )
result = astar_search(romania)
print("\n == Path",result[0], ", cost = ", result[1])



