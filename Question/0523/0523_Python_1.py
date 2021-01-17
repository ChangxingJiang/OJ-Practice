from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        visited = {0: -1}
        last = 0
        for i, num in enumerate(nums):
            last += num
            if k != 0:
                last %= k
            if last not in visited:
                visited[last] = i
            elif i - visited[last] > 1:
                return True
        return False


if __name__ == "__main__":
    print(Solution().checkSubarraySum([23, 2, 4, 6, 7], k=6))  # True
    print(Solution().checkSubarraySum([23, 2, 6, 4, 7], k=6))  # True
    print(Solution().checkSubarraySum([0, 0], k=0))  # True
    print(Solution().checkSubarraySum([0, 0], k=-1))  # True
    print(Solution().checkSubarraySum([23, 2, 4, 6, 7], k=-6))  # True
    print(Solution().checkSubarraySum([1, 0], k=2))  # False
