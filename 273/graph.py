import heapq

BIG_NUMBER = 1e50


def shortest_path(graph, start, end):
    """
       Input: graph: a dictionary of dictionary
              start: starting city   Ex. a
              end:   target city     Ex. b

       Output: tuple of (distance, [path of cites])
       Ex.   (distance, ['a', 'c', 'd', 'b])
    """

    distance_vector = {node: BIG_NUMBER for node in graph.keys()}
    enter_from_vector = {node: "" for node in graph.keys()}
    distance_vector[start] = 0
    exploration_queue = [(0, start, "")]
    visited_nodes = {start}

    while exploration_queue:
        current_node_distance, current_node_name, from_node = heapq.heappop(exploration_queue)

        if current_node_distance < distance_vector[current_node_name]:
            distance_vector[current_node_name] = current_node_distance
            enter_from_vector[current_node_name] = from_node

        for to_node, edge_distance in graph[current_node_name].items():
            total_distance = current_node_distance + edge_distance
            if to_node not in visited_nodes and total_distance <= distance_vector[to_node]:
                heapq.heappush(exploration_queue, (total_distance, to_node, current_node_name))

        visited_nodes.add(current_node_name)

    path = [end]
    while path[-1] != start:
        path.append(enter_from_vector[path[-1]])
    path.reverse()

    return distance_vector[end], path
