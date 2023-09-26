from nodes_universal import *

from hill_climb import sort_by_heuristic


def traverse(start: int, dest: int, width: int, path: list):
    path = path + [start]
    found = 0
    if start == dest:
        return path

    next_nodes = sort_by_heuristic(nodes[start].connections)

    count = 0
    for node in next_nodes:
        if count >= width:
            break
        if node not in path:
            return traverse(node, dest, width, path)


results = traverse(start, dest, 2, [])
print(results)
