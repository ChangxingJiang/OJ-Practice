from typing import List


# 线段树
# 超出时间限制


class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort(reverse=True)

        times = [0] * len(nums)

        for left, right in requests:
            for i in range(left, right + 1):
                times[i] += 1

        times.sort(reverse=True)

        ans = 0
        for i in range(len(nums)):
            ans += nums[i] * times[i]
            if times[i] == 0:
                break

        return ans % (10 ** 9 + 7)


if __name__ == "__main__":
    print(Solution().maxSumRangeQuery(nums=[1, 2, 3, 4, 5], requests=[[1, 3], [0, 1]]))  # 19
    print(Solution().maxSumRangeQuery(nums=[1, 2, 3, 4, 5, 6], requests=[[0, 1]]))  # 11
    print(Solution().maxSumRangeQuery(nums=[1, 2, 3, 4, 5, 10], requests=[[0, 2], [1, 3], [1, 1]]))  # 47
