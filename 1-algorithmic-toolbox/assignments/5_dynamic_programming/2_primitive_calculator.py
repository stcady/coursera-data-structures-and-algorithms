def compute_operations(n):
    count = [0]*(n+1)
    count[1] = 1
    for i in range(2,n+1):
        indices = [i-1]
        if i%2 == 0:
            indices.append(i//2)
        if i%3 == 0:
            indices.append(i//3)
        min_count = min([count[x] for x in indices])
        count[i] = min_count+1
    curr = n
    seq = [curr]
    while curr != 1:
        options = [curr - 1]
        if curr % 2 == 0:
            options.append(curr // 2)
        if curr % 3 == 0:
            options.append(curr // 3)
        curr = min([(c, count[c]) for c in options], key=lambda x: x[1])[0]
        seq.append(curr)
    return seq[::-1]


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
