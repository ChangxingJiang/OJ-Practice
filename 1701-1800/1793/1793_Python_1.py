from typing import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        size = len(nums)

        i, j = k, k  # 当前左右位置
        now = nums[k]  # 当前最小值

        # 寻找左侧或右侧大于当前最小值的值
        while i > 0 and nums[i - 1] >= now:
            i -= 1
        while j < size - 1 and nums[j + 1] >= now:
            j += 1

        ans = now * (j - i + 1)

        while i > 0 or j < size - 1:
            # 选择左右侧相对大的一个值使当前最小值变小
            if i > 0 and j < size - 1:
                if nums[i - 1] < nums[j + 1]:
                    now = nums[j + 1]
                    j += 1
                else:
                    now = nums[i - 1]
                    i -= 1
            elif i > 0:
                now = nums[i - 1]
                i -= 1
            elif j < size - 1:
                now = nums[j + 1]
                j += 1

            # 寻找左侧或右侧大于当前最小值的值
            while i > 0 and nums[i - 1] >= now:
                i -= 1
            while j < size - 1 and nums[j + 1] >= now:
                j += 1

            ans = max(ans, now * (j - i + 1))

        return ans


if __name__ == "__main__":
    print(Solution().maximumScore(nums=[1, 4, 3, 7, 4, 5], k=3))  # 15
    print(Solution().maximumScore(nums=[5, 5, 4, 5, 4, 1, 1, 1], k=0))  # 20
