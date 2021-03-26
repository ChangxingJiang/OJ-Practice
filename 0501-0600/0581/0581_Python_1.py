from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stack = []
        reverse_min_idx = None
        reverse_max_idx = None
        for i in range(len(nums)):
            n = nums[i]
            if len(stack) == 0 or n >= stack[-1]:
                stack.append(n)
            else:
                reverse_end_idx = i
                reverse_start_idx = i

                # 使用临时栈到倒序部分升序
                temp_stack = []
                while len(stack) > 0 and n < stack[-1]:
                    reverse_start_idx -= 1
                    temp_stack.append(stack.pop(-1))
                temp_stack.append(n)

                while temp_stack:
                    stack.append(temp_stack.pop(-1))

                # 更新升序数组起始坐标和升序数组结尾坐标
                if reverse_min_idx is None or reverse_start_idx < reverse_min_idx:
                    reverse_min_idx = reverse_start_idx
                if reverse_max_idx is None or reverse_end_idx > reverse_max_idx:
                    reverse_max_idx = reverse_end_idx

        if reverse_min_idx is not None and reverse_max_idx is not None:
            return reverse_max_idx - reverse_min_idx + 1
        else:
            return 0


if __name__ == "__main__":
    print(Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))  # 5
    print(Solution().findUnsortedSubarray([2, 1]))  # 2
    print(Solution().findUnsortedSubarray([3, 2, 3, 2, 4]))  # 4
    print(Solution().findUnsortedSubarray([2, 3, 3, 2, 4]))  # 3
    print(Solution().findUnsortedSubarray([1, 2, 3, 3, 3]))  # 0
    print(Solution().findUnsortedSubarray([1, 2, 4, 5, 3]))  # 3
    print(Solution().findUnsortedSubarray([1, 3, 5, 2, 4]))  # 4
