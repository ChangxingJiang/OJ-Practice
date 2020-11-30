from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        pass


if __name__ == "__main__":
    # ["0->2","4->5","7"]
    print(Solution().summaryRanges(nums=[0, 1, 2, 4, 5, 7]))

    #["0","2->4","6","8->9"]
    print(Solution().summaryRanges(nums = [0,2,3,4,6,8,9]))

    # []
    print(Solution().summaryRanges(nums = []))

    # ["-1"]
    print(Solution().summaryRanges(nums = [-1]))

    # ["0"]
    print(Solution().summaryRanges(nums = [0]))