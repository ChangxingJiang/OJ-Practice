import bisect
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        queue = []
        for num in nums:
            if not queue or queue[-1] < num:
                queue.append(num)
            else:
                idx = bisect.bisect_right(queue, num)
                if idx == 0 or (queue[idx - 1] != num):
                    queue[idx] = num
        return len(queue)


if __name__ == "__main__":
    print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # 4
