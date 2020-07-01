from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left, right, count = {}, {}, {}
        for i in range(len(nums)):
            n = nums[i]
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
            if n not in left:
                left[n] = i
            right[n] = i

        degree = max(count.values())
        
        ans = len(nums)
        for n in count:
            if count[n] == degree:
                ans = min(ans, right[n] - left[n] + 1)

        return ans


if __name__ == "__main__":
    print(Solution().findShortestSubArray([1, 2, 2, 3, 1]))  # 2
    print(Solution().findShortestSubArray([1, 2, 2, 3, 1, 4, 2]))  # 6
