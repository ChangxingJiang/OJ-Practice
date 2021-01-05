import bisect
import math
from typing import List


class Solution:
    # O(NlogN)

    _MOD = 10 ** 9 + 7

    def waysToSplit(self, nums: List[int]) -> int:
        total = sum(nums)

        # 处理全为0的特殊情况
        if total == 0:
            size = len(nums)
            return ((size - 1) * (size - 2) // 2) % self._MOD

        # 计算前缀和
        prefix = []
        for num in nums:
            if not prefix:
                prefix.append(num)
            else:
                prefix.append(prefix[-1] + num)
        # print(prefix)

        # 首先找到mid和right的分界点的最右侧的可能
        d2 = bisect.bisect_right(prefix, math.ceil(total * 2 / 3))
        # print("D2(max):", d2)

        ans = 0

        # 逐渐向左迭代d2（d2位right的最左侧元素的下标）
        while d2 >= 2:  # 如果小于等于2则左边只有一个点，不够分
            v3 = total - prefix[d2 - 1]  # 计算right部分的和
            surplus = prefix[d2 - 1]  # 计算当前left和mid部分的总和
            # print("D2,V3:", d2, v3)

            # 找到left和mid的分界点的最左侧的位置（mid部分的和小于等于right部分的和）
            v2_max = v3
            v1_min = surplus - v2_max
            d1_min = max(1, bisect.bisect_left(prefix, v1_min))  # 处理可能包含0的情况
            if prefix[d1_min - 1] < v1_min:
                d1_min += 1

            # 找到left和mid的分界点的最右侧的位置（left部分的和小于等于mid部分的和）
            v1_max = math.floor(surplus / 2)
            d1_max = bisect.bisect_right(prefix, v1_max)  # 处理可能包含0的情况
            # if d1_max > 1 and prefix[d1_max - 1] == v1_max:
            #     d1_max -= 1

            # print("V1(min):", v1_min, "V1(max):", v1_max, "D1(min):", d1_min, "D1(max):", d1_max)

            # 累加结果总和
            if v1_min <= v1_max:
                ans += d1_max - d1_min + 1

            d2 -= 1

        return ans % self._MOD


if __name__ == "__main__":
    print(Solution().waysToSplit(nums=[1, 1, 1]))  # 1
    print(Solution().waysToSplit(nums=[1, 2, 2, 2, 5, 0]))  # 3
    print(Solution().waysToSplit(nums=[3, 2, 1]))  # 0
    print(Solution().waysToSplit(nums=[2, 3, 5, 10]))  # 3
    print(Solution().waysToSplit(nums=[0] * 100000))  # 999849973  # 第83个测试用例

    print(Solution().waysToSplit(nums=[0, 0, 0, 0, 0]))  # 6
