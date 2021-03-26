import collections
from typing import List


# O(N) O(N)
# 哈希表 数学


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        count = collections.Counter()

        # 统计余数
        for num in arr:
            surplus = num % k
            count[surplus] += 1

        for surplus, num in count.items():
            # 处理余数为0的情况
            if surplus == 0:
                if num % 2 != 0:
                    return False

            # 处理余数不为0的情况
            else:
                if num != count[k - surplus]:
                    return False

        return True


if __name__ == "__main__":
    print(Solution().canArrange(arr=[1, 2, 3, 4, 5, 10, 6, 7, 8, 9], k=5))  # True
    print(Solution().canArrange(arr=[1, 2, 3, 4, 5, 6], k=7))  # True
    print(Solution().canArrange(arr=[1, 2, 3, 4, 5, 6], k=10))  # False
    print(Solution().canArrange(arr=[-10, 10], k=2))  # True
    print(Solution().canArrange(arr=[-1, 1, -2, 2, -3, 3, -4, 4], k=3))  # True
