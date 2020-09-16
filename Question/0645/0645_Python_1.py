from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        arr = [0] * (len(nums) + 1)
        for n in nums:
            arr[n] += 1
        more = None
        lost = None
        for i in range(1, len(arr)):
            if arr[i] == 0:
                lost = i
            elif arr[i] == 2:
                more = i
        return [more, lost]


if __name__ == "__main__":
    print(Solution().findErrorNums([1, 2, 2, 4]))  # [2,3]
