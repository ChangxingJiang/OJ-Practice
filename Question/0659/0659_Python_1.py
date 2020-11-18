import heapq
from typing import List


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        # 格式化数组
        lst = []
        now = nums[0] - 1
        for n in nums:
            if n == now:
                lst[-1] += 1
            elif n == now + 1:
                lst.append(1)
                now = n
            else:
                lst.append(0)
                lst.append(1)
                now = n
        lst.append(0)

        # 维护起点堆
        heap = []
        for i2 in range(len(lst)):
            while lst[i2] > len(heap):
                heapq.heappush(heap, i2)
            while lst[i2] < len(heap):
                i1 = heapq.heappop(heap)
                if i2 - i1 < 3:
                    return False

        return True


if __name__ == "__main__":
    print(Solution().isPossible([1, 2, 3, 3, 4, 5]))  # True
    print(Solution().isPossible([1, 2, 3, 3, 4, 4, 5, 5]))  # True
    print(Solution().isPossible([1, 2, 3, 4, 4, 5]))  # False

    print(Solution().isPossible([1, 2, 3, 10, 11, 12]))  # True
