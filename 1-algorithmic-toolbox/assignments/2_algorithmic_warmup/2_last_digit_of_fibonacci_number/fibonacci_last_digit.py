def original_fibonacci_last_digit(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

def fibonacci_last_digit_cycle():
    F = [0 for i in range(60)]
    F[0] = 0
    F[1] = 1
    for n in range(2, 60):
        F[n] = (F[n-1]+F[n-2])%10
    return F

def fibonacci_last_digit(n):
    if n < 0:
        raise Exception("Invalid input. Must be non-negative number.")
    F = fibonacci_last_digit_cycle()
    return F[n%60]

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_last_digit(n))
