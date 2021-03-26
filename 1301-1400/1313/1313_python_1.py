from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(0, len(nums), 2):
            ans += [nums[i + 1]] * nums[i]
        return ans


if __name__ == "__main__":
    print(Solution().decompressRLElist(nums=[1, 2, 3, 4]))  # [2,4,4,4]
    print(Solution().decompressRLElist(nums=[1, 1, 2, 3]))  # [1,3,3]
