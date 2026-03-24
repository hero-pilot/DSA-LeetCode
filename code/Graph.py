class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for k , v in self.adj_list.items():
            print(k, ":", v)

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edge(self,v1,v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            if v1 not in self.adj_list[v2] and v2 not in self.adj_list[v1]:
                self.adj_list[v1].append(v2)
                self.adj_list[v2].append(v1)
                return True
        return False
    
    def remove_edge(self, v1,v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            if v1 in self.adj_list[v2] and v2 in self.adj_list[v1]:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
                return True
        return False

    
    def remove_vertex(self,vertex):
        if vertex in self.adj_list.keys():
            for v in self.adj_list[vertex]:
                self.adj_list[v].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False

graph = Graph()

graph.add_vertex("A")
graph.add_vertex("B")
graph.add_edge("A", "B")
graph.print_graph()
graph.remove_vertex("A")
graph.print_graph()