from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # 计算余数
        # O(N)
        total = sum(nums)
        surplus = total % p
        # print("目标余数:", surplus)

        # 处理余数为0的情况
        if surplus == 0:
            return 0

        # 前缀余哈希表
        hashmap = {}

        ans = -1

        # 计算前缀余
        # O(N)
        last = 0
        hashmap[0] = -1
        for i, num in enumerate(nums):
            last += num
            last %= p
            hashmap[last] = i

            # 检查是否构成目标余数
            aim_val = (p + last - surplus) % p
            if aim_val in hashmap:
                now = i - hashmap[aim_val]
                if ans == -1 or ans > now:
                    ans = now

        return ans if ans < len(nums) else -1


if __name__ == "__main__":
    print(Solution().minSubarray(nums=[3, 1, 4, 2], p=6))  # 1
    print(Solution().minSubarray(nums=[6, 3, 5, 2], p=9))  # 2
    print(Solution().minSubarray(nums=[1, 2, 3], p=3))  # 0
    print(Solution().minSubarray(nums=[1, 2, 3], p=7))  # -1
    print(Solution().minSubarray(nums=[1000000000, 1000000000, 1000000000], p=3))  # 0
    print(Solution().minSubarray(nums=[8, 32, 31, 18, 34, 20, 21, 13, 1, 27, 23, 22, 11, 15, 30, 4, 2], p=148))  # 7
    print(Solution().minSubarray(nums=[4, 4, 2], p=7))  # -1
