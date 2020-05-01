#Final Project Implementation
#Liam Iverson
#11192836

from itertools import combinations
import matplotlib.pyplot as plt
import networkx as nx
G = nx.Graph()
cliquesAll = []


def k_cliques(graph):
    # 2-cliques
    cliques = [{i, j} for i, j in graph.edges() if i != j]
    k = 2

    while cliques:
        # result
        yield k, cliques

        # merge k-cliques into (k+1)-cliques
        cliques_1 = set()
        for u, v in combinations(cliques, 2):
            w = u ^ v
            if len(w) == 2 and graph.has_edge(*w):
                cliques_1.add(tuple(u | w))

        # remove duplicates
        cliques = list(map(set, cliques_1))
        k += 1


def get_cliques(graph, size_k):
	global cliquesAll
	for k, cliques in k_cliques(graph):
		if k == size_k:
			print('%d-cliques = %d, %s.' % (k, len(cliques), cliques))
			cliquesAll = cliques


dataSet =[{"Name":"Wayne","Tyler":30,"Aiden":5,"Zack":30,"Graison":4,"Raven":2,"MemeberShip": 0,"Communities":[]},{"Name":"Tyler","Wayne":30,"Aiden":5,"Zack":30,"Graison":4,"Raven":2,"MemeberShip": 0,"Communities":[]},
		  {"Name":"Zack","Tyler":30,"Aiden":5,"Wayne":30,"Graison":4,"MemeberShip": 0,"Communities":[]},{"Name":"Graison","Tyler":4,"Wayne":4,"Aiden":2,"Raven":30,"MemeberShip": 0,"Communities":[]},
		  {"Name":"Aiden","Tyler":5,"Wayne":5,"Zack":5,"Graison":2,"MemeberShip": 0,"Communities":[]},{"Name":"Nick","Andrew":3,"Aaron":3,"Alex":30,"Tyler":1,"Wayne":1,"MemeberShip": 0,"Communities":[]},{"Name":"Andrew","Aaron":10,"Nick":3,"Alex":3,"MemeberShip": 0,"Communities":[]},
		  {"Name":"Aaron","Nick":3,"Andrew":10,"Alex":3,"MemeberShip": 0,"Communities":[]},{"Name":"Alex","Nick":30,"Aaron":3,"Andrew":3,"MemeberShip":0,"Communities":[]},{"Name":"Raven","Graison":30,"Tyler":2,"Wayne":2,"MemeberShip": 0,"Communities":[]}]
nodeLookUpTable = {"Wayne":1,"Tyler":2,"Zack":3,"Graison":4,"Aiden":5,"Nick":6,"Andrew":7,"Aaron":8,"Alex":9,"Raven":10}



color_map = []


nodes, edges = 10, 0
size_k = 4


for i in dataSet:
	name = i["Name"]
	node = nodeLookUpTable[name]
	G.add_node(node)
	for j in i.keys():
		if(j != "Name" and j!="MemeberShip" and j != "Communities"):
			G.add_edge(node,nodeLookUpTable[j],weight=i[j])
			edges+=1
	color_map.append(0)
get_cliques(G, size_k)

count = 0
for i in dataSet:
	name = i["Name"]
	node = nodeLookUpTable[name]
	for j in range(len(cliquesAll)):
		print(i)
		if node in cliquesAll[j]:
			i["MemeberShip"]+=1
			i["Communities"].append(j)
			color_map[count] += j 
	count +=1
print(dataSet)
nx.draw(G,with_labels=True, node_color = color_map)
plt.show()