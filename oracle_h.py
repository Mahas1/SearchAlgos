from nodes_universal import *


def traverse(start: int, dest: int, oracle: tuple, oracle_cost: int, path: tuple, current_cost: int, solutions: dict):
    path = path + (start,)
    if start == dest:
        if path not in solutions:
            solutions[path] = current_cost
            if not oracle:
                oracle = path
                oracle_cost = current_cost
            elif current_cost < oracle_cost:
                oracle = path
                oracle_cost = current_cost


    for node, cost in sort_by_cost_heuristic(nodes[start].connections):

        if node not in path:
            oracle, oracle_cost, solutions = traverse(node, dest, oracle, oracle_cost, path,
                                                      current_cost + nodes[start].connections[node],
                                                      solutions)
    return oracle, oracle_cost, solutions


if __name__ == "__main__":
    make_heuristic(dest)

    final_oracle, final_oracle_cost, final_solutions = traverse(1, 3, (), 0, (), 0, {})
    print("Oracle:", final_oracle)
    print("Oracle Cost:", final_oracle_cost)

    print("All solutions:")
    print("\n".join([str(i) + " with cost " + str(final_solutions[i]) for i in final_solutions]))
