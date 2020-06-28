from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        step = 0
        while len(set(nums)) > 1:
            maximum = max(nums)
            nums.remove(maximum)
            nums = [i + 1 for i in nums]
            nums.append(maximum)
            step += 1
        return step


if __name__ == "__main__":
    print(Solution().minMoves([1, 2, 3]))  # 3
    print(Solution().minMoves([1, 2, 5]))  # 5
