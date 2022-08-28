from sys import stdin


def optimal_value(capacity, weights, values):
    if len(weights) != len(values):
        raise Exception("Weights and Values must be the same size.")
    total = 0
    norm = [(values[i]/weights[i], i) for i in range(len(weights))]
    ordered_norm = sorted(norm, reverse=True)
    for rate, i in ordered_norm:
        if capacity < weights[i]:
            total += capacity*rate
            break
        total += values[i]
        capacity -= weights[i]
        if capacity == 0:
            break
    return total


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
