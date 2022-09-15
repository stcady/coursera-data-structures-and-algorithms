# python3

def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    swaps = []
    for i in range((len(data)//2)-1, -1, -1):
        sift_down(data, i, swaps)
    return swaps
        
def sift_down(data, index, swaps):
    left_child = 2*index+1
    right_child = 2*index+2
    min_index = index
    if left_child < len(data) and data[left_child] < data[min_index]:
        min_index = left_child
    if right_child < len(data) and data[right_child] < data[min_index]:
        min_index = right_child
    if index != min_index:
        data[index], data[min_index] = data[min_index], data[index]
        swaps.append((index, min_index))
        sift_down(data, min_index, swaps)

def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
