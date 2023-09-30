from nodes_universal import *

start = 1
dest = 3


def traverse(start: int, dest: int, path: list):
    path = path + [start]
    found = 0
    if start == dest:
        return path

    for node in nodes[start].connections.keys():
        if node not in path:
            return traverse(node, dest, path)


result = (traverse(start, dest, []))
print(result)
