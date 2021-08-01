class Vertix:
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return self.value

class Edge:
    def __init__(self, vertix , weight):
        self.vertix = vertix
        self.weight = weight


class Graph:
    
    def __init__(self):
        self.adjacency_list = {}
    
    def add_node(self, value):
        v = Vertix(value)
        self.adjacency_list[v] = []
        return v
    
    def add_edge(self, start_node, end_node, weight=0):
        # TODO: Check if both are in the graph
        if start_node in self.adjacency_list and end_node in self.adjacency_list:
            edge = Edge(end_node, weight)
            self.adjacency_list[start_node].append(edge)
        else:
            return 'one of the nodes is not exist'
    
    def get_nodes(self):
        '''
        return all the nodes in the graph
        '''
        new_list = []
        for i in self.adjacency_list.keys():
            new_list.append(i.value)
        return new_list
    
    def get_neighbors(self, node):
        '''
        return all the nodes that are connected with the node
        '''
        new_list = []
        for i in self.adjacency_list[node]:
            new_list.append(i.vertix.value)
        return new_list
    
    def size(self):
        return len(list(self.adjacency_list.keys()))

    def __str__(self):
        output = ''
        for vertix in self.adjacency_list.keys():
            # Concatenate the value of vertix
            output += vertix.value
            # Iterate over all edges of this vertix
            for edge in self.adjacency_list[vertix]:
                output += ' -> ' + edge.vertix.value 
            # Add a new line
            output += '\n'
        return output
