from nodes_universal import *


def traverse(start: int, dest: int, path: list, solutions: list):
    path = path + [start]
    found = 0
    if start == dest:
        if path not in solutions:
            solutions.append(path)
            found = 1

    if found:
        # preemptive exit
        return solutions

    for node in nodes[start].connections.keys():
        # same level nodes
        if node not in path:
            if check_solution(path + [node], dest):
                found = 1
                solutions.append(path + [node])
    if not found:
        for node in nodes[start].connections:
            # deeper nodes
            if node not in path:
                solutions = traverse(node, dest, path, solutions)
    return solutions


results = (traverse(start, dest, [], []))
for i in results:
    print(i)
