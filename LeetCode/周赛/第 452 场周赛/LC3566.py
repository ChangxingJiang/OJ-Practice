from typing import List


class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        # 不可能拆分的场景
        total = 1
        for num in nums:
            total *= num
        if target * target != total:
            return False

        # 枚举所有场景
        n = len(nums)
        for stat in range(1 << n):
            n1 = 0
            n2 = 0
            v1 = 1
            v2 = 1
            for i, num in enumerate(nums):
                if (1 << i) & stat:
                    n1 += 1
                    v1 *= num
                else:
                    n2 += 1
                    v2 *= num
            if n1 > 0 and n2 > 0 and v1 == target and v2 == target:
                return True

        return False


if __name__ == "__main__":
    print(Solution().checkEqualPartitions(nums=[3, 1, 6, 8, 4], target=24))  # True
    print(Solution().checkEqualPartitions(nums=[2, 5, 3, 7], target=15))  # False
