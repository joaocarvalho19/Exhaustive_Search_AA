#import matplotlib.pyplot as plt
from itertools import combinations

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.edges = []

        # Init matrix
        self.incidence_matrix = [[] * num_vertices for n in range(0,num_vertices)]


    # Print the matrix
    def printMatriz(self):
        print(" - Matriz: - ")
        for row in self.incidence_matrix:
            print(row)
        print("-")

    def getAllPairsOfEdges(self):
        all_possible_sol = []
        """zipped_rows = zip(*self.incidence_matrix)
        matriz_T = [list(row) for row in zipped_rows]"""

        print(self.edges)
        for i in range(len(self.edges)):
            all_possible_sol += combinations(self.edges, i+1)
        

        return all_possible_sol

    # Add edges
    def add_edge(self, v1, v2):
        
        self.edges.append(len(self.edges))

        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
        
        for i in range(len(self.incidence_matrix)):
            if i==v1 or i==v2:
                self.incidence_matrix[i].append(1)
            else:
                self.incidence_matrix[i].append(0)

        #self.incidence_matrix[v1][v2] += 1
        #self.incidence_matrix[v2][v1] += 1


    # Remove edges
    """def remove_edge(self, v1, v2):
        if self.incidence_matrix[v1][v2] == 0:
            print("No edge between %d and %d" % (v1, v2))
            return
        self.incidence_matrix[v1][v2] -= 1
        self.incidence_matrix[v2][v1] -= 1"""