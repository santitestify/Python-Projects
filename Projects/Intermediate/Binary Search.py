#  implementation of binary search algorithm

# we will prove that binary search than naive search!

# naive search: scan entire list and ask if its equal to the target
# if yes, return the index
# if no, then return -1
import random
import time


def naive_search(x, target):
    # example x = [1, 3, 10, 12]
    for i in range(len(x)):
        if x[i] == target:
            return i
    return -1

# binary search uses divide and conquer!
# we will leverage the fact that our list is SORTED


def binary_search(x, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(x) - 1

    if high < low:
        return -1
    # example x = [1, 3, 5, 10, 12] # should return 3
    # midpoint = (len(x)) // 2  # this means how many times to go into length
    midpoint = (low + high) // 2

    if x[midpoint] == target:
        return midpoint
    elif target < x[midpoint]:
        return binary_search(x, target, low, midpoint-1)
    else:
        # target > x[midpoint]
        return binary_search(x, target, midpoint+1, high)


if __name__ == '__main__':
    x = [1, 3, 5, 10, 12]
    target = 10
    print(naive_search(x, target))
    print(binary_search(x, target))

    length = 1000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive search time: ", (end - start)/ length, "seconds")

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("binary search time: ", (end - start) / length, "seconds")
