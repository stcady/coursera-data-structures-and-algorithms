def lcs3(first_sequence, second_sequence, third_sequence):
    first_length = len(first_sequence)
    second_length = len(second_sequence)
    third_length = len(third_sequence)
    result = [[[0 for _ in range(third_length+1)] for _ in range(second_length+1)] for _ in range(first_length+1)]
    for i in range(first_length+1):
        for j in range(second_length+1):
            for k in range(third_length+1):
                if i == 0 or j == 0 or k == 0:
                    result[i][j][k] = 0
                elif first_sequence[i-1] == second_sequence[j-1] and first_sequence[i-1] == third_sequence[k-1]:
                    result[i][j][k] = result[i-1][j-1][k-1]+1
                else:
                    result[i][j][k] = max(result[i-1][j][k], result[i][j-1][k], result[i][j][k-1])
    return result[first_length][second_length][third_length]

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))
