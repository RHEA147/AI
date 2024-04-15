#Iterative Depth First Search

class MyGraph:
    def __init__(self, cmap, i, g):
        self.citymap = cmap
        self.init = i
        self.goal = g
    def goal_test(self,anode):
        if anode==self.goal:
            return True
        else:
            return False
    def getLinks(self, anode):
        return list(self.citymap[anode].keys())

def recursive_dls2(node, citygraph, limit,nodelist):  
    if citygraph.goal_test(node):
        return node
    elif limit == 0:
        return 'cutoff'
    else:
        cutoff_occurred = False        
        for child in citygraph.getLinks(node):
            if not child in nodelist :
                nodelist.append(child)                
                result = recursive_dls2(child, citygraph, limit - 1, nodelist)
                if result == 'cutoff':
                    cutoff_occurred = True
                elif result is not None:
                    return result
        return 'cutoff' if cutoff_occurred else 'Not found'

def depth_limited_search(citymap, limit=50):    
    return recursive_dls2(citymap.init, citymap, limit,[citymap.init])
   
def iterative_deepening_search(citymap, limit):
    for depth in range(0,limit):
        print("checking with depth :", depth)
        result = depth_limited_search(citymap, depth)
        print("result : ", result)
       
cities  = {    
            'Jaipur':{'Mumbai':500, 'Nashik':650},
            'Mumbai': {'Jaipur':500, 'Pune' :150, 'Nashik':100, 'Ratnagiri':300},
            'Nashik': {'Jaipur':650, 'Mumbai':100, 'Pune':200},
            'Pune': {'Nashik':200, 'Mumbai':150, 'Ratnagiri':130},
            'Ratnagiri': {'Mumbai':300, 'Pune':130}    
        }

print("Conducting search from Jaipur to Ratnagiri upto level 3")
route = MyGraph(cities, 'Jaipur','Ratnagiri' )
iterative_deepening_search(route, 3)

