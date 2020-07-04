from typing import List


def two_sums(array, target) -> List[int]:
    dict_ = {}  # number: index

    for i in range(len(array)):
        dif = target - array[i]
        
        if dif in dict_:
            return [dict_[dif], i]
        else:
            dict_[array[i]] = i


arr = [1,2,3,4,5,6,7]
print(two_sums(arr, 13))
