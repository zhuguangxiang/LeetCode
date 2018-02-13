def topological_sort(unsorted_graph):
    '''
    idea from http://blog.jupo.org/2012/04/06/topological-sorting-acyclic-directed-graphs/
    deal with a node only if all it's children are sorted, in other words, start from the latest appeared nodes, build
    from there. A cycle is defined when in any iteration, none of the node can be solved, i.e 2 nodes point to each other
    :param unsorted_graph: list[tuple(node, list[children])]
    :return: sorted graph
    '''
    sorted_nodes = []

    while graph_unsorted:
        acyclic = False
        for idx, (node, children_list) in enumerate(unsorted_graph):

            for children in children_list:
                if children not in sorted_nodes:
                    # do not deal with the node who has unsorted child
                    break
            else:
                # if all children been sorted, move this node to sorted list
                acyclic = True
                sorted_nodes.append(node)
                unsorted_graph.remove(unsorted_graph[idx])

        if acyclic is False:
            raise RuntimeError("Cycle formed in the graph")
    return sorted_nodes[::-1]

if __name__=="__main__":
    graph_unsorted = [(2, []),
                      (5, [11]),
                      (11, [2, 9, 10]),
                      (7, [11, 8]),
                      (9, []),
                      (10, []),
                      (8, [9]),
                      (3, [10, 8])]
    sorted_list = topological_sort(graph_unsorted)
    print(sorted_list)
