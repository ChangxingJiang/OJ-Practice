from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        ans = [max(nums[:k])]
        for i in range(k, len(nums)):
            if nums[i] >= ans[-1]:
                ans.append(nums[i])
            elif nums[i - k] == ans[-1]:
                ans.append(max(nums[i - k + 1:i + 1]))
            else:
                ans.append(ans[-1])

        return ans


if __name__ == "__main__":
    print(Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))  # [3,3,5,5,6,7]
