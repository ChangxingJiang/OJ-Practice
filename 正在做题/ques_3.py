from collections import deque
from typing import List

from sortedcontainers import SortedList

MOD = 10 ** 9 + 7


class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # 计算每个位置的窗口长度
        window_1 = deque()  # 插入顺序
        window_2 = SortedList()  # 排序顺序
        dp_1 = []
        for num in nums:
            window_1.append(num)
            window_2.add(num)
            while window_2[-1] - window_2[0] > k:
                old_num = window_1.popleft()
                window_2.remove(old_num)
            dp_1.append(len(window_1))

        # 计算最终结果
        dp_2 = [0, 1]  # 结果值
        acc = [0, 1]  # 结果值的前缀和
        for i in range(n):
            j = i + 2
            dp_2.append((acc[j - 1] - acc[j - dp_1[i] - 1]) % MOD)
            acc.append((acc[j - 1] + dp_2[j]) % MOD)

        return dp_2[-1] % MOD


if __name__ == "__main__":
    print(Solution().countPartitions([9, 4, 1, 3, 7], 4))  # 6
    print(Solution().countPartitions([3, 3, 4], 0))  # 2
