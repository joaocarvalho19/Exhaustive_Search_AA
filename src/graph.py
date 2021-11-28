#import matplotlib.pyplot as plt
from itertools import combinations

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.edges = []
        self.edge_adjacency = {}

        # Init matrix
        self.incidence_matrix = [[] * num_vertices for n in range(0,num_vertices)]


    # Print the matrix
    def printMatriz(self):
        print(" - Incidence Matrix: - ")
        for row in self.incidence_matrix:
            print(row)
        print("-")

    # Get all combinations
    def getAllSolutions(self):
        all_possible_sol = []

        for i in range(len(self.edges)):
            all_possible_sol += combinations(self.edges, i+1)
        
        return all_possible_sol


    def findExhaustiveSolution(self, all_possible_sol):
        res = []
        for sol in all_possible_sol:
            adj_edges = set()
            
            for e in sol:
                adj_edges.add(e)
                adj_edges.update(set(self.edge_adjacency[e]))
            if len(list(adj_edges)) == len(self.edges):
                res.append(sol)
        
        return min(res, key = lambda t: len(t))
    
    def findGreedySolution(self):
        sorted_dictionary = dict(sorted(self.edge_adjacency.items(), key = lambda t: len(t[1]), reverse=True))       # Sort by length of the list(edge adjacency)

        res = []
        while sorted_dictionary:
            edge_max = list(sorted_dictionary.keys())[0]
            edge_list = sorted_dictionary[edge_max]
            # Add the edge with the bigger adjacency list size
            res.append(edge_max)

            # Remove the edge and its adjacent edges
            del sorted_dictionary[edge_max]
            for e in edge_list:
                if e in sorted_dictionary.keys():
                    del sorted_dictionary[e]
            
        return res


    # Add edges
    def add_edge(self, v1, v2):
        self.edges.append(len(self.edges))

        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
            return
        
        for i in range(len(self.incidence_matrix)):
            if i==v1 or i==v2:
                self.incidence_matrix[i].append(1)
            else:
                self.incidence_matrix[i].append(0)
                
    
    def getEdgesAdjacency(self):
        zipped_rows = zip(*self.incidence_matrix)
        matriz_T = [list(row) for row in zipped_rows]
        for i in range(len(self.edges)):
            adj_edges = []
            for j in range(len(matriz_T[i])):
                if matriz_T[i][j] == 1:
                    adj_edges += [e for e in range(len(self.incidence_matrix[j])) if self.incidence_matrix[j][e] == 1 and e not in adj_edges and e != i]
            
            self.edge_adjacency[i] = sorted(adj_edges)


    # Remove edges
    """def remove_edge(self, v1, v2):
        if self.incidence_matrix[v1][v2] == 0:
            print("No edge between %d and %d" % (v1, v2))
            return
        self.incidence_matrix[v1][v2] -= 1
        self.incidence_matrix[v2][v1] -= 1"""