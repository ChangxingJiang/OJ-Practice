import collections
from typing import List


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        size = len(nums)

        ans = []

        right = 0

        queue = collections.deque()
        while k > 0:
            for _ in range(right, size - k + 1):
                while queue and queue[-1] > nums[right]:
                    queue.pop()
                queue.append(nums[right])
                right += 1

            ans.append(queue.popleft())
            k -= 1

        return ans


if __name__ == "__main__":
    print(Solution().mostCompetitive(nums=[3, 5, 2, 6], k=2))  # [2,6]
    print(Solution().mostCompetitive(nums=[2, 4, 3, 3, 5, 4, 9, 6], k=4))  # [2,3,3,4]

    print(Solution().mostCompetitive(nums=[1], k=1))  # [1]
    print(Solution().mostCompetitive(nums=[2, 1], k=2))  # [2,1]
