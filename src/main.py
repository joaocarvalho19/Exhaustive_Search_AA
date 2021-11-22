from graph import Graph
#import matplotlib.pyplot as plt


if __name__ == "__main__":

    graph = Graph(5)
    graph.add_edge(0,1)
    graph.add_edge(0,2)
    graph.add_edge(1,3)
    graph.add_edge(2,3)
    graph.add_edge(1,4)

    graph.printMatriz()

    print(graph.getAllPairsOfEdges())