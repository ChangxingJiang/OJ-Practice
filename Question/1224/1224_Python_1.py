import collections
from typing import List


class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        size = len(set(nums))
        count1 = collections.Counter()
        count2 = collections.Counter({0: size})

        ans = 1
        for i, n in enumerate(nums):
            count2[count1[n]] -= 1
            count1[n] += 1
            count2[count1[n]] += 1

            lst1 = [v for k, v in count2.items() if k != 0 and v != 0]
            lst2 = [k for k, v in count2.items() if k != 0 and v != 0]

            # print(i, ":", count1, count2, "->", lst1, lst2)

            # 如果当前所有的数出现次数都是相同的
            if len(lst1) == 1:
                # 如果它们每个数的出现次数不是1
                if lst1[0] != 1:
                    # 那么如果它们不只1个数，则无法实现
                    if lst2[0] != 1:
                        continue

            # 如果当前所有的数有两种不同的出现次数
            if len(lst1) == 2:
                # 如果出现少的一种出现次数的出现次数的不是1个，则无法实现
                if min(lst1) != 1:
                    continue
                # 如果两个出现次数均是出现一次，且他们相差1，则可以实现
                if not (lst1[0] == lst1[1] == 1 and abs(lst2[0] - lst2[1]) == 1):
                    # 但是，如果即使出现少的一种出现次数的出现次数是1个，但是它不能通过删除一个数变成那个出现次数更高的出现次数，或变为0，则无法实现
                    i1 = lst1.index(1)
                    i2 = 1 if i1 == 0 else 0
                    if lst2[i1] - lst2[i2] != 1 and lst2[i1] != 1:
                        continue

            # 如果当前所有的数有三种不同的出现次数，则注定无法实现
            if len(lst1) > 2:
                continue

            ans = max(ans, i + 1)

        return ans


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
