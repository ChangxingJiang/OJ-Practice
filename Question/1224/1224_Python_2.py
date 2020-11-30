import collections
from math import inf
from typing import List


class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        nums += [inf]
        count = collections.Counter(nums)

        # 从后往前遍历
        for i in reversed(range(len(nums))):
            count[nums[i]] -= 1
            lst = sorted(filter(lambda x: x > 0, count.values()))  # 剔除掉是0的出现频率
            if len(lst) == 1 or (lst[0] == 1 and lst[1] == lst[-1]) or (lst[0] == lst[-2] == lst[-1] - 1):
                return i


if __name__ == "__main__":
    # 7
    print(Solution().maxEqualFreq(nums=[2, 2, 1, 1, 5, 3, 3, 5]))

    # 13
    print(Solution().maxEqualFreq(nums=[1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5]))

    # 5
    print(Solution().maxEqualFreq(nums=[1, 1, 1, 2, 2, 2]))

    # 8
    print(Solution().maxEqualFreq(nums=[10, 2, 8, 9, 3, 8, 1, 5, 2, 3, 7, 6]))

    # 13
    print(Solution().maxEqualFreq(nums=[1, 2, 3, 1, 2, 3, 4, 4, 4, 4, 1, 2, 3, 5, 6]))

    # 2
    print(Solution().maxEqualFreq(nums=[1, 1]))

    # 7
    print(Solution().maxEqualFreq(nums=[1, 1, 1, 2, 2, 2, 3, 3, 3]))

    # 2
    print(Solution().maxEqualFreq(nums=[1, 2]))
