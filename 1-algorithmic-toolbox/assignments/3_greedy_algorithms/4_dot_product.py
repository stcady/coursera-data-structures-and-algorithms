from itertools import permutations


def naive_max_dot_product(first_sequence, second_sequence):
    max_product = 0
    for permutation in permutations(second_sequence):
        dot_product = sum(first_sequence[i] * permutation[i] for i in range(len(first_sequence)))
        max_product = max(max_product, dot_product)

    return max_product

def max_dot_product(first_sequence, second_sequence):
    if len(first_sequence) != len(second_sequence):
        raise Exception("First and second sequences must be the same size.")
    total = 0
    for _ in range(len(first_sequence)):
        first_max = max(first_sequence)
        first_sequence.remove(first_max)
        second_max = max(second_sequence)
        second_sequence.remove(second_max)
        total += first_max*second_max
    return total

if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product(prices, clicks))
    
