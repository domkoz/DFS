from collections import deque


def dfs(graph: dict, starting_node: str) -> list:
    """ This function returns the list of nodes order by depth first search algorithm.
    _________________________________________________________________________________________
    :type graph: dict
    :type starting_node: str
    :param graph: Graph that need's to be ordered.
    :param starting_node: Any node from the graph.
    :return : list of nodes
    """

    if not isinstance(graph, dict):
        raise ValueError("Graph must be a dictionary.")

    if not isinstance(starting_node, str):
        raise ValueError("Starting_node must be a String.")

    visited = []
    stack = deque()

    visited.append(starting_node)
    stack.append(starting_node)

    while stack:
        current_node = stack.pop()

        for node in graph[current_node]:
            if node not in visited:
                stack.append(node)

        if current_node not in visited:
            visited.append(current_node)

    return visited

