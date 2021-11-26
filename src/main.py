from graph import Graph
import matplotlib.pyplot as plt
import time
import random
import networkx as nx
import sys

def getRandomVer(n):
    return [random.randint(0, 9) for i in range(n)]

def getRandomEdges(n, ver):
    pass

def main(num_vertices):
    graph = Graph(num_vertices)
    G = nx.Graph()
    G.add_nodes_from([x for x in range(0, num_vertices)])

    x = getRandomVer(num_vertices)
    y = getRandomVer(num_vertices)
    print(x)
    print(y)
    chosen_edges = {}
    begin = time.time()
    for i in range(0,num_vertices):
            n_iters = random.choice([x for x in range(0,num_vertices)])
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
            
    graph.printMatriz()
    nx.draw(G, with_labels=True)
    
    all_sol = graph.getAllSolutions()
    
    graph.findGreedySolution()

    #res = graph.findExhaustiveSolution(all_sol)
    #print("Minimum edge dominating set: {}".format(res))
    #print("Time: {}".format(time.time() - begin))
    
    plt.show()
if __name__ == "__main__":
    num_vertices = None
    try:
        num_vertices = int(sys.argv[1])
    except Exception as err:
        print("Usage: python3 main.py \n\t-v <generate random graph with N vertices: int>")

    main(num_vertices)