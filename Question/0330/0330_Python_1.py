from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        # 处理数组为空的情况
        if not nums:
            ans = 0
            total = 0
            while total < n:
                total += (total + 1)
                ans += 1
            return ans

        # 处理数组不为空的情况
        else:
            ans = 0

            # 处理第1个数之前的情况
            total = 0
            while total < nums[0] - 1:
                total += (total + 1)
                ans += 1

            total += nums[0]
            # 处理数组中间的数
            for i in range(1, len(nums)):
                if nums[i] > n:
                    break
                while total < nums[i] - 1:
                    total += (total + 1)
                    ans += 1
                total += nums[i]

            # 处理最后1个数之后的情况
            while total < n:
                total += (total + 1)
                ans += 1

            return ans


if __name__ == "__main__":
    print(Solution().minPatches(nums=[1, 3], n=6))  # 1
    print(Solution().minPatches(nums=[1, 5, 10], n=20))  # 2
    print(Solution().minPatches(nums=[1, 2, 2], n=5))  # 0
    print(Solution().minPatches(nums=[1, 7, 21, 31, 34, 37, 40, 43, 49, 87, 90, 92, 93, 98, 99], n=12))  # 2
