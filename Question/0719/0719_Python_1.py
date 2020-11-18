import heapq
from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # 排序列表
        # O(NlogN)
        nums.sort()

        # 定义从每个位置开始累加的距离之和的堆
        # O(N)
        heap = [(nums[i + 1] - nums[i], i, i + 1) for i in range(len(nums) - 1)]
        heapq.heapify(heap)

        # 生成第K个绝对差值（使第K个绝对差值成为堆顶）
        # O(KlogN)
        for j in range(k - 1):
            distance, i1, i2 = heapq.heappop(heap)
            if i2 + 1 < len(nums):
                heapq.heappush(heap, (nums[i2 + 1] - nums[i1], i1, i2 + 1))

        # 返回第K个绝对差值
        return heapq.heappop(heap)[0]


if __name__ == "__main__":
    # 0
    print(Solution().smallestDistancePair(nums=[1, 3, 1], k=1))

    # 36
    print(Solution().smallestDistancePair(nums=[38, 33, 57, 65, 13, 2, 86, 75, 4, 56], k=26))
