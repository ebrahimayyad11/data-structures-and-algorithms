import sys
sys.path.append("/home/ebrahimayyad11/data-structures-and-algorithms/Data-Structures/graph")
from graph.graph import Graph

def business_trip(graph,city_names):
    cost=0
    verticess= list(graph.adjacency_list.keys())
    adjacent_nodes=set()

    for item in city_names:
        if item not in graph.get_nodes():
            return False


    for i in range(len(city_names)-1):
        print(i)
        for item in verticess:
            if city_names[i]== item.value:
                vertix=item

        for edge in graph.adjacency_list[vertix]:
            adjacent_nodes.add(edge.node.value)
            if edge.node.value == city_names[i+1]:
                    cost+= edge.weight

        if city_names[i+1] not in adjacent_nodes:
            return False

    return f'True, ${cost}'

