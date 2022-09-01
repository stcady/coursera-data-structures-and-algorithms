from itertools import combinations


def inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions

def merge_sort(array):
    n = len(array)
    temp_array = [0]*n
    return merge_sort_util(array, temp_array, 0, n-1)

def merge_sort_util(array, temp_array, left, right):
    invariants = 0
    if left < right:
        middle = (left+right)//2
        invariants += merge_sort_util(array, temp_array, left, middle)
        invariants += merge_sort_util(array, temp_array, middle+1, right)
        invariants += merge(array, temp_array, left, middle, right)
    return invariants

def merge(array, temp_array, left, middle, right):
    left_bottom = left
    right_bottom = middle+1
    right_top = right
    temp_bottom = left
    invariants = 0
    while left_bottom <= middle and right_bottom <= right_top:
        if array[left_bottom] <= array[right_bottom]:
            temp_array[temp_bottom] = array[left_bottom]
            temp_bottom+=1
            left_bottom+=1
        else:
            temp_array[temp_bottom] = array[right_bottom]
            invariants += (middle - left_bottom) + 1
            temp_bottom+=1
            right_bottom+=1
    while left_bottom <= middle:
        temp_array[temp_bottom] = array[left_bottom]
        temp_bottom+=1
        left_bottom+=1
    while right_bottom <= right_top:
        temp_array[temp_bottom] = array[right_bottom]
        temp_bottom+=1
        right_bottom+=1
    for i in range(left, right + 1):
        array[i] = temp_array[i]
    return invariants

if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(merge_sort(elements))
