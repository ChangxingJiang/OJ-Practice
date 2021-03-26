from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        size = len(nums)

        end = 0  # 上一步可达位置
        far = 0  # 当前步的下一步的最远距离
        ans = 0  # 当前步数

        for i in range(size - 1):
            # 计算当前步可达到的最远位置
            if i + nums[i] > far:
                far = i + nums[i]

            # print(i, end, far, "->", ans)
            # 上一步已经迈完了
            if i == end:
                ans += 1
                end = far

        return ans


if __name__ == "__main__":
    print(Solution().jump([2, 3, 1, 1, 4]))  # 2

    print(Solution().jump([0]))  # 0
    print(Solution().jump([2, 1]))  # 1
    print(Solution().jump([1, 2, 0, 1]))  # 2
    print(Solution().jump([1, 2, 1, 1, 1]))  # 3
