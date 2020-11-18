from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # 滑动窗口判断有多少符合要求的差值
        # 每次: O(N)
        def count(guess):
            total = 0
            l = 0
            for r in range(1, len(nums)):
                while l < r and nums[r] - nums[l] > guess:
                    l += 1
                total += r - l
            # print(guess, "->", total)
            return total

        # 排序列表
        # O(NlogN)
        nums.sort()

        # 二分查找寻找目标值
        # O(NlogW) 其中W为nums中最大值与最小值的差
        ans = 0
        left, right = 0, nums[-1] - nums[0]
        while left <= right:
            mid = (left + right) // 2
            # print(left, right, "->", mid)
            if count(mid) >= k:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans


if __name__ == "__main__":
    # 0
    print(Solution().smallestDistancePair(nums=[1, 3, 1], k=1))

    # 5
    print(Solution().smallestDistancePair(nums=[1, 6, 1], k=3))

    # 36
    print(Solution().smallestDistancePair(nums=[38, 33, 57, 65, 13, 2, 86, 75, 4, 56], k=26))
