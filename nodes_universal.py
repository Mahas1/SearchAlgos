class Node:
    def __init__(self, node_id: int, position: tuple, connections: list):
        self.id = node_id
        self.position = position
        self.heuristic = 0
        self.cost = 0
        self.connections = connections


def calculate_heuristic(node: Node, dest: Node):
    return ((dest.position[1] - node.position[1]) ** 2 + (dest.position[0] - node.position[0]) ** 2) ** 0.5


def make_heuristic(dest: int):
    for node in nodes:
        nodes[node].heuristic = calculate_heuristic(nodes[node], nodes[dest])


def check_solution(path: list, dest: int):
    if path[-1] == dest:
        return True
    else:
        return False


nodes = {
    1: (Node(1, (0, 0), [2])),
    2: (Node(2, (1, 1), [3, 4])),
    3: (Node(3, (1, 2), [4])),
    4: (Node(4, (2, 1), [3])),
}

start = 1
dest = 3
