from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        lst = [0] * 101
        for n in nums:
            for i in range(min(n + 1, 101)):
                lst[i] += 1
        for i, n in enumerate(lst):
            if i == n:
                return i
        return -1


if __name__ == "__main__":
    print(Solution().specialArray([3, 5]))  # 2
    print(Solution().specialArray([0, 0]))  # -1
    print(Solution().specialArray([0, 4, 3, 0, 4]))  # 3
    print(Solution().specialArray([3, 6, 7, 7, 0]))  # -1
    print(Solution().specialArray([1, 101, 2]))  # -1
