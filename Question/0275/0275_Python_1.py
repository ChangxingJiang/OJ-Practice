from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0

        left, right = 0, len(citations)
        while left < right:
            mid = (left + right + 1) // 2
            if citations[-mid] < mid:
                right = mid - 1
            else:
                left = mid
        return left


if __name__ == "__main__":
    print(Solution().hIndex(citations=[0, 1, 3, 5, 6]))  # 3
    print(Solution().hIndex(citations=[0, 1]))  # 1
    print(Solution().hIndex(citations=[1]))  # 1
    print(Solution().hIndex(citations=[11, 15]))  # 2
