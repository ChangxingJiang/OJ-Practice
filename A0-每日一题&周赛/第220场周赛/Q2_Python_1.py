from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        size = len(nums)

        count = set()
        left, right = 0, 0
        total = 0

        ans = 0

        while right < size:
            # 如果当前值已经在窗口中
            if nums[right] in count:
                # 则移动窗口左侧边缘至当前元素
                while nums[left] != nums[right]:
                    total -= nums[left]
                    count.remove(nums[left])
                    left += 1
                # 移除当前元素
                total -= nums[left]
                count.remove(nums[left])
                left += 1

            # 将当前值添加到窗口
            total += nums[right]
            count.add(nums[right])
            right += 1

            ans = max(ans, total)

        return ans


if __name__ == "__main__":
    print(Solution().maximumUniqueSubarray([4, 2, 4, 5, 6]))  # 17
    print(Solution().maximumUniqueSubarray([5, 2, 1, 2, 5, 2, 1, 2, 5]))  # 8
