class Node:
    def __init__(self, node_id: int, position: tuple, connections: dict):
        self.id = node_id
        self.position = position
        self.heuristic = 0
        self.cost = 0
        self.connections = connections  # dict(node_id: cost)
        self.cost = 0


def calculate_heuristic(node: Node, dest: Node) -> float:
    return ((dest.position[1] - node.position[1]) ** 2 + (dest.position[0] - node.position[0]) ** 2) ** 0.5


def make_heuristic(dest: int):
    for node in nodes:
        nodes[node].heuristic = calculate_heuristic(nodes[node], nodes[dest])


def check_solution(path: list, dest: int) -> bool:
    if path[-1] == dest:
        return True
    else:
        return False


def sort_by_heuristic(given_nodes: list[int]) -> list[int]:
    given_nodes.sort(key=lambda x: nodes[x].heuristic)
    return given_nodes


def sort_by_cost_heuristic(given_nodes: list[int]) -> list[int]:
    given_nodes.sort(key=lambda x: nodes[x].heuristic + nodes[x].cost)
    return given_nodes


def sort_by_cost(connections: dict) -> list[tuple[int, int]]:
    return sorted(connections.items(), key=lambda x: x[1])


nodes = {
    1: (Node(1, (0, 0), {2: 1})),
    2: (Node(2, (1, 1), {3: 1, 4: 1})),
    3: (Node(3, (1, 2), {4: 1})),
    4: (Node(4, (2, 1), {3: 1})),
}

start = 1
dest = 3
