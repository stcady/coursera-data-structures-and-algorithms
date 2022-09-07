def lcs2(first_sequence, second_sequence):
    first_length = len(first_sequence)
    second_length = len(second_sequence)
    result = [[0 for _ in range(second_length+1)] for _ in range(first_length+1)]
    for i in range(first_length+1):
        for j in range(second_length+1):
            if i == 0 or j == 0:
                result[i][j] = 0
            elif first_sequence[i-1] == second_sequence[j-1]:
                result[i][j] = result[i-1][j-1]+1
            else:
                result[i][j] = max(result[i-1][j], result[i][j-1])
    return result[first_length][second_length]


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
