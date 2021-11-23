from graph import Graph
#import matplotlib.pyplot as plt


if __name__ == "__main__":

    graph = Graph(5)
    graph.add_edge(0,1)
    graph.add_edge(1,2)
    graph.add_edge(2,3)
    graph.add_edge(3,4)

    graph.printMatriz()

    all_sol = graph.getAllSolutions()

    print("Minimum edge dominating set: {}".format(graph.findSolution(all_sol)))