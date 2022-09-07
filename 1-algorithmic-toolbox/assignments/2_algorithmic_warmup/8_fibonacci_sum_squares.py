def naive_fibonacci_sum_squares(n):
    if n <= 1:
        return n

    previous, current, sum = 0, 1, 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10

def fibonacci_last_digit_cycle():
    F = [0 for i in range(60)]
    F[0] = 0
    F[1] = 1
    for n in range(2, 60):
        F[n] = (F[n-1]+F[n-2])%10
    return F

def fibonacci_sum_squares(n):
    if n < 0:
        raise Exception("Invalid input. Must be non-negative number.")
    F = fibonacci_last_digit_cycle()
    return (F[n%60]*F[(n+1)%60])%10

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares(n))
