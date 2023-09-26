from nodes_universal import *


def traverse(start: int, dest: int, path: list, solutions: list):
    path = path + [start]
    if start == dest:
        if path not in solutions:
            solutions.append(path)
    for node in nodes[start].connections:
        if node not in path:
            solutions = traverse(node, dest, path, solutions)
    return solutions


results = (traverse(start, dest, [], []))
for i in results:
    print(i)
