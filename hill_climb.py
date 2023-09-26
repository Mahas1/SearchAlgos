from nodes_universal import *

start = 1
dest = 3

make_heuristic(dest)


def sort_by_heuristic(given_nodes: list[int]):
    given_nodes.sort(key=lambda x: nodes[x].heuristic)
    return given_nodes


def traverse(start: int, dest: int, path: list):
    path = path + [start]

    if start == dest:
        return path

    next_nodes = sort_by_heuristic(nodes[start].connections)

    for node in next_nodes:
        if node not in path:
            return traverse(node, dest, path)


if __name__ == "__main__":
    result = (traverse(start, dest, []))
    print(result)