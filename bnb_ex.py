from nodes_universal import *

from oracle import traverse as oracle_traverse


# branched and bound

def traverse(start: int, dest: int, oracle_cost: int, paths: dict[tuple:int], expanded_nodes: list):
    if not paths:
        paths = {(start,): 0}

    to_expand, current_cost = sort_by_cost(paths)[0]
    while to_expand[-1] in expanded_nodes:
        del paths[to_expand]  # don't expand nodes already visited
        to_expand, current_cost = sort_by_cost(paths)[0]  # one with the least cost

    if current_cost > oracle_cost:
        return -1

    del paths[to_expand]  # delete this entry so we can add the updated ones

    for node, cost in nodes[to_expand[-1]].connections.items():
        paths[to_expand + (node,)] = current_cost + cost

        if node == dest:
            return {to_expand + (node,): current_cost + cost}

    return traverse(start, dest, oracle_cost, paths, expanded_nodes)




if __name__ == "__main__":
    _, oracle_cost, _ = oracle_traverse(1, 3, (), 0, (), 0, {})
    result = traverse(start, dest, oracle_cost, {}, [])
    print(result)
