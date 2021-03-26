from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        size = len(nums)
        nums += nums
        stack = []
        for i in range(len(nums) - 1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            stack.append(nums[i])
            nums[i] = stack[-2] if len(stack) > 1 else -1
        return nums[:size]


if __name__ == "__main__":
    print(Solution().nextGreaterElements([1, 2, 1]))  # [2,-1,2]
