from graph import Graph
import matplotlib.pyplot as plt
import time
import random
import networkx as nx
import sys
import getopt

def getRandomVer(n):
    return [random.randint(0, 9) for i in range(n)]

def getRandomEdges(n, ver):
    pass

def main(num_vertices, search_type):
    graph = Graph(num_vertices)
    G = nx.Graph()
    G.add_nodes_from([x for x in range(0, num_vertices)])

    chosen_edges = {}
    begin = time.time()
    for i in range(0,num_vertices):
            n_iters = random.choice([x for x in range(1,num_vertices)])
            used_vertices = []
            for iteration in range(0, n_iters):
                j = []
                if i in chosen_edges:
                    j = list( set([ x for x in range(num_vertices) if x != i]) - set(chosen_edges[i]) - set(used_vertices))
                else:
                    j = list( set([ x for x in range(num_vertices) if x != i]) - set(used_vertices))
                
                j_choice = None
                if j:
                    j_choice = random.choice(j)
                
                #print("Creating edge: G[%d][%d]" %  (i,j))
                if j_choice:
                    graph.add_edge(i,j_choice)
                    G.add_edge(i,j_choice)
                    if j_choice not in chosen_edges.keys():
                        chosen_edges[j_choice] = set([i])
                    else:
                        chosen_edges[j_choice].add(i)

                    used_vertices.append(j_choice)
    
    """graph.add_edge(0,1)
    graph.add_edge(1,2)
    graph.add_edge(2,3)
    graph.add_edge(3,4)
    graph.add_edge(3,1)
    G.add_edge(0,1)
    G.add_edge(1,2)
    G.add_edge(2,3)
    G.add_edge(3,4)
    G.add_edge(3,1)"""
            
    graph.printMatriz()
    graph.getEdgesAdjacency()
    nx.draw(G, with_labels=True)
    
    #all_sol = graph.getAllSolutions()
    if search_type == "greedy":
        result = graph.findGreedySolution()
        print("Minimum edge dominating set ({} algorithm): {}".format(search_type, result))
    else:
        result = graph.findExhaustiveSolution(graph.getAllSolutions())
        print("Minimum edge dominating set ({} algorithm): {}".format(search_type, result))
    
    print("Time: {}".format(time.time() - begin))
    
    plt.show()

if __name__ == "__main__":
    num_vertices = None
    search_type = None      #  greedy | exhaustive

    try:
        num_vertices = int(sys.argv[1])
        search_type = sys.argv[2]
    except Exception as err:
        print("Usage: python3 main.py <generate random graph with N vertices (int)> <algorithm type (str: 'greedy' | str: 'exhaustive')>")

    if not isinstance(num_vertices, int):
        print("Vertices not int!")
        print("Usage: python3 main.py <generate random graph with N vertices (int)> <algorithm type (str: 'greedy' | str: 'exhaustive')>")
        sys.exit(2)
    
    if num_vertices and (search_type == 'greedy' or search_type == 'exhaustive'):
        main(num_vertices, search_type)
    else:
        print("Usage: python3 main.py <generate random graph with N vertices (int)> <algorithm type (str: 'greedy' | str: 'exhaustive')>")