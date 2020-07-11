"""
in an array of unsorted integer, find the median
"""
import heapq


def continuous_median(list_: iter):
    if not list_:
        return None

    lower_heap = []  # max heap
    higher_heap = []  # min heap
    median = []

    for i in list_:
        add_number(i, lower_heap, higher_heap)
        rebalance(lower_heap, higher_heap)
        median.append(calculate_median(lower_heap, higher_heap))

    return median


def add_number(value, lower_heap, higher_heap):
    if not lower_heap or value <= -lower_heap[0]:
        heapq.heappush(lower_heap, -value)
    else:
        heapq.heappush(higher_heap, value)


def rebalance(lower_heap, higher_heap):
    dif = len(higher_heap) - len(lower_heap)
    # +ve means higher has more, -ve means lower has more
    if dif > 1:
        popped = heapq.heappop(higher_heap)
        heapq.heappush(lower_heap, -popped)
    elif dif < -1:
        popped = -heapq.heappop(lower_heap)
        heapq.heappush(higher_heap, popped)


def calculate_median(lower_heap, higher_heap):
    dif = len(higher_heap) - len(lower_heap)
    if dif == 0:
        return -lower_heap[0] + (higher_heap[0]+lower_heap[0])/2
    elif dif == 1:
        return higher_heap[0]
    elif dif == -1:
        return -lower_heap[0]
    else:
        return None


inputs = [12, 4, 5, 3, 8, 7]
print(continuous_median(inputs))







