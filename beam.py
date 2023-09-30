from nodes_universal import *


def traverse(start: int, dest: int, width: int, path: list):
    path = path + [start]

    if start == dest:
        return path

    next_nodes = sort_by_heuristic(list(nodes[start].connections.keys()))

    count = 0
    for node in next_nodes:
        if count >= width:
            break
        if node not in path:
            return traverse(node, dest, width, path)


results = traverse(start, dest, 2, [])
print(results)
