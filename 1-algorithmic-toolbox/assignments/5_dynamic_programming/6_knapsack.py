from sys import stdin


def maximum_gold(capacity, weights):
    weights = [0] + weights
    dp_weights = [[0 for _ in range(capacity + 1)] for _ in range(len(weights))]
    for i in range(1,len(weights)):
        for j in range(1, capacity + 1):
            dp_weights[i][j] = dp_weights[i-1][j]
            if weights[i] <= j:
                new_weight = dp_weights[i-1][j-weights[i]] + weights[i]
                if dp_weights[i][j] < new_weight:
                    dp_weights[i][j] = new_weight
    return dp_weights[-1][-1]

if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
