import bisect
from typing import List


class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        s1, s2 = len(target), len(arr)

        # 计算target中每个数值的位置
        count = {}
        for i in range(s1):
            count[target[i]] = i

        # 将arr转换为位置序列
        lst = []
        for i in range(s2):
            if arr[i] in count:
                lst.append(count[arr[i]])

        # 计算最长递增子序列
        queue = []
        for n in lst:
            if not queue or queue[-1] < n:
                queue.append(n)
            else:
                idx = bisect.bisect_right(queue, n)
                if idx == 0 or (queue[idx - 1] != n):
                    queue[idx] = n

        return s1 - len(queue)


if __name__ == "__main__":
    print(Solution().minOperations(target=[5, 1, 3], arr=[9, 4, 2, 3, 4]))  # 2
    print(Solution().minOperations(target=[6, 4, 8, 1, 3, 2], arr=[4, 7, 6, 2, 3, 8, 6, 1]))  # 3
    print(Solution().minOperations(target=[6, 4, 8, 1, 3, 2], arr=[4, 7, 6, 2, 3, 8, 6, 1]))  # 3
