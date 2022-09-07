def naive_fibonacci_number(n):
    if n <= 1:
        return n

    return naive_fibonacci_number(n - 1) + naive_fibonacci_number(n - 2)

def non_space_efficient_fibonacci_number(n):
    if n < 2:
        return n
    F = [0 for i in range(n)]
    F[0] = 0
    F[1] = 1
    for n in range(2, n):
        F[n] = F[n-1]+F[n-2]
    return F[n]

def fibonacci_number(n):
    if n < 0:
        raise Exception("Invalid input. Must be non-negative number.")
    if n < 2:
        return n
    first = 1
    second = 0
    for _ in range(2,n+1):
        current = first + second
        second = first
        first = current
    return current

if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
