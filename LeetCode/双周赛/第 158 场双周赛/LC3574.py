import math
from typing import List


class Solution:
    def maxGCDScore(self, nums: List[int], k: int) -> int:
        # 计算每个数包含因子 2 的数量
        factor_list = []
        for num in nums:
            i = 0
            while num % 2 == 0:
                num //= 2
                i += 1
            factor_list.append(i)
        # print(factor_list)

        # 遍历所有的可能组合
        n = len(nums)
        result = n
        for i in range(n):
            j = i
            gcd = nums[i]  # 当前的最大公约数
            min_factor_2 = factor_list[i]  # 包含最少的因子 2 的数量
            min_factor_cnt = 1  # 包含最少的因子 2 数量的数的数量

            # 计算当前值
            mul = 1
            if k >= min_factor_cnt:  # 可以全部翻倍
                mul = 2
            result = max(result, gcd * (j - i + 1) * mul)

            while j + 1 < n:
                # 更新值
                j += 1
                gcd = math.gcd(gcd, nums[j])
                if factor_list[j] < min_factor_2:
                    min_factor_2 = factor_list[j]
                    min_factor_cnt = 1
                elif factor_list[j] == min_factor_2:
                    min_factor_cnt += 1

                # 计算当前值
                mul = 1
                if k >= min_factor_cnt:  # 可以全部翻倍
                    mul = 2
                result = max(result, gcd * (j - i + 1) * mul)

                # 剪枝逻辑
                if gcd * (n - i) * 2 < result:
                    break

        return result


if __name__ == "__main__":
    print(Solution().maxGCDScore(nums=[2, 4], k=1))  # 8
    print(Solution().maxGCDScore(nums=[3, 5, 7], k=2))  # 14
    print(Solution().maxGCDScore(nums=[5, 5, 5], k=1))  # 15
