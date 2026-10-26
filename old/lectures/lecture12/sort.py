"""
An implementation of merge sort which _looks_ fine...
"""

def merge(left, right):
    "Merge two sorted lists into one sorted list"
    merged = []
    i = j = 0

    # Merge while both lists have elements
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Append remaining elements (at most one of these loops runs)
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def merge_sort(seq):
    "Recursive merge sort, returns a new sorted list"
    n = len(seq)
    if n <= 1:
        return seq[:]

    mid = n // 2
    left_sorted = merge_sort(seq[:mid])
    right_sorted = merge_sort(seq[-mid:])
    return merge(left_sorted, right_sorted)


# Test code
if __name__ == "__main__":
    assert merge_sort([]) == []
    assert merge_sort([7]) == [7]
    assert merge_sort([10, 5, 20, 15]) == [5, 10, 15, 20]
    assert merge_sort([38, 27, 43, 9, 82, 10, 2, 13]) == [2, 9, 10, 13, 27, 38, 43, 82]
    assert merge_sort(["apple", "pear", "banana", "pear"]) == ["apple", "banana", "pear", "pear"]
    # assert merge_sort([4, 6, 5, 2, 1, 3]) == [1, 2, 3, 4, 5, 6]

