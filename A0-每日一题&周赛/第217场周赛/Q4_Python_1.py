import heapq
from typing import List


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        min_val, max_val = min(nums), max(nums)
        ans = max_val - min_val

        # 处理最小的奇数
        heapq.heapify(nums)
        while nums[0] % 2 == 1:
            v = heapq.heappop(nums)
            heapq.heappush(nums, v * 2)

            min_val = nums[0]
            if v * 2 > max_val:
                max_val = v * 2
            ans = min(ans, max_val - min_val)

        # 处理最大的偶数
        nums = [-n for n in nums]
        heapq.heapify(nums)
        while nums[0] % 2 == 0:
            v = heapq.heappop(nums)
            heapq.heappush(nums, v // 2)

            max_val = -nums[0]
            if - (v // 2) < min_val:
                min_val = - (v // 2)
            ans = min(ans, max_val - min_val)

        return ans


if __name__ == "__main__":
    print(Solution().minimumDeviation(nums=[1, 2, 3, 4]))  # 1
    print(Solution().minimumDeviation(nums=[4, 1, 5, 20, 3]))  # 3
    print(Solution().minimumDeviation(nums=[2, 10, 8]))  # 3
    print(Solution().minimumDeviation(nums=[7, 8, 9, 10]))  # 3
