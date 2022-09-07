def optimal_summands(n):
    summands = []
    curr = 1
    total = 1
    summands.append(curr)
    while n - total > summands[-1]:
        summands.append(summands[-1] + 1)
        total += summands[-1]
    summands[-1] += (n - total)
    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
