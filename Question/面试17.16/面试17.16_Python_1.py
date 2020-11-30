from typing import List


class Solution:
    def massage(self, nums: List[int]) -> int:
        a, b = [0, 0]
        for n in nums:
            a, b = b, max(a + n, b)
        return b


if __name__ == "__main__":
    print(Solution().massage([1, 2, 3, 1]))  # 4
    print(Solution().massage([2, 7, 9, 3, 1]))  # 12
    print(Solution().massage([2, 1, 4, 5, 3, 1, 1, 3]))  # 12
