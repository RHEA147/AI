#RBFS

from myutils import *
infinity = float('inf')
class Node:
    def __init__(self, n, p="", g=0,h=0):
        self.name=n
        self.parent=p
        self.gval=g
        self.fval=h
    
    def getPath(self):
        if self.parent=="":
            return self.name
        else:
            return self.parent + "," + self.name
    
    
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

    def getMax(self, childf,nodef):
        if childf>=nodef:
            return childf
        else:
            return nodef

    def lowest_fvalue_node(self,nodelist):
        min_fval = nodelist[0].fval
        min_fval_node_index=0    
        for n in range(1,len(nodelist)):        
            if nodelist[n].fval < min_fval :
                min_fval_node_index = n
                min_fval = nodelist[n].fval
        return nodelist[min_fval_node_index]

    def second_lowest_fvalue( self, nodelist,lowest_f): 
        secondmin_fval = infinity
        for n in range(0,len(nodelist)):        
            if nodelist[n].fval > lowest_f and nodelist[n].fval < secondmin_fval :            
                secondmin_fval = nodelist[n].fval
        return secondmin_fval
           


def RecursiveBFS(problem) : 
    startnode = Node(problem.init, "", 0, problem.h(problem.init))    
    return RBFS(problem, startnode, infinity)

def RBFS(problem, node, f_limit) : 
    print("\nIn RBFS Function with node ", node.name, " with node's f value = ", node.fval , " and f-limit = ", f_limit)
    if problem.goal_test(node.name) :
        return [node, None]  
    successors = []
    for child in problem.getLinks(node.name):         
        gval = node.gval + problem.citymap[node.name][child]
        hval = problem.h(child)
        childf = problem.getMax(gval+hval , node.fval)        
        childnode = Node(child, node.getPath() ,gval, childf)        
        successors.append(childnode)
        print("added successor - ",childnode.getPath(), ",", childnode.fval)
        
    
    if len(successors) == 0 :
        return [None, infinity]
    while True:        
        best  = problem.lowest_fvalue_node(successors)
        if best.fval > f_limit :
            print("returning from :" , best.name)
            return [None, best.fval]
        alternative = problem.second_lowest_fvalue(successors, best.fval)        
        x = RBFS(problem, best, min(f_limit, alternative))
        result = x[0]        
        print("updating f value of best node ", best.name, " from ", best.fval , " to ", x[1] )
        best.fval = x[1]                    
        if result != None :
            print("returning from :" , best.name)
            return [result, None]

       


       
romania_map = {'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
     'Bucharest': {'Urziceni': 85, 'Pitesti': 101, 'Giurgiu': 90, 'Fagaras': 211},
                               'Craiova': {'Drobeta': 120, 'Rimnicu': 146, 'Pitesti': 138},
                               'Drobeta': {'Mehadia': 75, 'Craiova': 120},
                               'Eforie': {'Hirsova': 86},
                               'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
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
                               'Giurgiu': {'Bucharest': 90},
                               'Mehadia': {'Drobeta': 75, 'Lugoj': 70},
                               'Vaslui': {'Iasi': 92, 'Urziceni': 142},
                               'Neamt': {'Iasi': 87}}


locations = dict(
    Arad=(91, 492), Bucharest=(400, 327), Craiova=(253, 288),
    Drobeta=(165, 299), Eforie=(562, 293), Fagaras=(305, 449),
    Giurgiu=(375, 270), Hirsova=(534, 350), Iasi=(473, 506),
    Lugoj=(165, 379), Mehadia=(168, 339), Neamt=(406, 537),
    Oradea=(131, 571), Pitesti=(320, 368), Rimnicu=(233, 410),
    Sibiu=(207, 457), Timisoara=(94, 410), Urziceni=(456, 350),
    Vaslui=(509, 444), Zerind=(108, 531))



print("\nSolving for arad to bucharest...")
romania = MyGraph(romania_map, locations, 'Arad','Bucharest' )
result = RecursiveBFS(romania)
print("\n == Path",result[0].getPath(), ", cost = ", result[0].gval)


