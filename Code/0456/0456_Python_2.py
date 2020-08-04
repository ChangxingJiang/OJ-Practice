from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # 生成当前之前最小值表
        min_lst = []
        now = float("inf")
        for n in nums:
            if n < now:
                now = n
            min_lst.append(now)

        # 从后向前遍历，维护单调栈
        stack = []
        for i in range(len(nums) - 1, -1, -1):
            # 移除栈内小于当前最小值的值
            while stack and stack[-1] <= min_lst[i]:
                stack.pop()

            # 判断是否已有解
            if stack and nums[i] > stack[-1]:
                return True

            # 更新栈
            elif not stack or nums[i] < stack[-1]:
                stack.append(nums[i])

        return False


if __name__ == "__main__":
    print(Solution().find132pattern([1, 2, 3, 4]))  # False
    print(Solution().find132pattern([3, 1, 4, 2]))  # True
    print(Solution().find132pattern([-1, 3, 2, 0]))  # True
    print(Solution().find132pattern([5, 6, 4, 7, 3, 8, 2, 9, 1]))  # False
    print(Solution().find132pattern([1, 0, 1, -4, -3]))  # False
    print(Solution().find132pattern([-2, 1, -2]))  # False
