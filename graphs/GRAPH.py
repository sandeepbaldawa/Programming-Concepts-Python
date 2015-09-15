""" A Python Class
A simple Python graph class, demonstrating the essential 
facts and functionalities of graphs.
"""
import networkx as nx
import matplotlib.pyplot as plt



class Graph(object):

    def __init__(self, graph_dict={}):
        """ initializes a graph object """
        self.__graph_dict = graph_dict

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.__graph_dict.keys())

    def edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in 
            self.__graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary. 
            Otherwise nothing has to be done. 
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list; 
            between two vertices can be multiple edges! 
        """
        #edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        """ A static method generating the edges of the 
            graph "graph". Edges are represented as sets 
            with one (a loop back to the vertex) or two 
            vertices 
        """
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append((vertex, neighbour))
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res
    
    def draw_graph(self, graph, labels=None, graph_layout='shell',
               node_size=1600, node_color='blue', node_alpha=0.3,
               node_text_size=12,
               edge_color='blue', edge_alpha=0.3, edge_tickness=1,
               edge_text_pos=0.3,
               text_font='sans-serif'):

        # create networkx graph
        G=nx.Graph()

        # add edges
        for edge in graph:
            G.add_edge(edge[0], edge[1])

        # these are different layouts for the network you may try
        # shell seems to work best
        if graph_layout == 'spring':
            graph_pos=nx.spring_layout(G)
        elif graph_layout == 'spectral':
            graph_pos=nx.spectral_layout(G)
        elif graph_layout == 'random':
            graph_pos=nx.random_layout(G)
        else:
            graph_pos=nx.shell_layout(G)

        # draw graph
        nx.draw_networkx_nodes(G,graph_pos,node_size=node_size, 
                               alpha=node_alpha, node_color=node_color)
        nx.draw_networkx_edges(G,graph_pos,width=edge_tickness,
                               alpha=edge_alpha,edge_color=edge_color)
        nx.draw_networkx_labels(G, graph_pos,font_size=node_text_size,
                                font_family=text_font)

        if labels is None:
            labels = range(len(graph))

        edge_labels = dict(zip(graph, labels))
        nx.draw_networkx_edge_labels(G, graph_pos, edge_labels=edge_labels, 
                                     label_pos=edge_text_pos)

        # show graph
        plt.show()



if __name__ == "__main__":

    g = { "a" : ["d"],
          "b" : ["c"],
          "c" : ["b", "c", "d", "e"],
          "d" : ["a", "c"],
          "e" : ["c"],
          "f" : []
        }


    graph = Graph(g)

    print("Vertices of graph:")
    print(graph.vertices())

    print("Edges of graph:")
    print(graph.edges())

    print("Add vertex:")
    graph.add_vertex("z")

    print("Vertices of graph:")
    print(graph.vertices())
 
    print("Add an edge:")
    graph.add_edge({"a","z"})
    
    print("Vertices of graph:")
    print(graph.vertices())

    print("Edges of graph:")
    print(graph.edges())

    print('Adding an edge {"x","y"} with new vertices:')
    graph.add_edge({"x","y"})
    print("Vertices of graph:")
    print(graph.vertices())
    print("Edges of graph:")
    print(graph.edges())
    graph.draw_graph(graph.edges())
