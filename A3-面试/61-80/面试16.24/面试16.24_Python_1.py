from typing import List


class Solution:
    def pairSums(self, nums: List[int], target: int) -> List[List[int]]:
        pass


if __name__ == "__main__":
    # [[5,6]]
    print(Solution().pairSums(nums=[5, 6, 5], target=11))

    # [[5,6],[5,6]]
    print(Solution().pairSums(nums=[5, 6, 5, 6], target=11))
