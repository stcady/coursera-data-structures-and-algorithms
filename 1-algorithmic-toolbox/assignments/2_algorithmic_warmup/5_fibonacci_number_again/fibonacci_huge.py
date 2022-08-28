def fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def fibonacci_huge(n, m):
    if n < 0:
        raise Exception("Invalid input. Must be non-negative number.")
    if n < 2:
        return n
    arr = [0, 1]
    first, second = 1, 0
    for i in range(n-1):
        second, first = first % m, (first + second) % m
        arr.append(first)
        if first == 1 and second == 0:
            i = (n % (i + 1))
            return arr[i]
    return first

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge(n, m))
