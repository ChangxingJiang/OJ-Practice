from typing import List


# 枚举所有可能的组合
def enumeration(nums):
    size = len(nums)
    ans = [0 for _ in range(1 << size)]  # 2**n种可能
    for i in range(size):
        for j in range(1 << i):
            ans[(1 << i) + j] = nums[i] + ans[j]
    return ans


class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        # 切分数组并枚举所有可能
        size = len(nums)
        part1 = enumeration(nums[:size // 2])
        part2 = enumeration(nums[size // 2:])

        # 排序所有可能
        part1.sort()
        part2.sort()

        ans = abs(goal)
        i, j = 0, len(part2) - 1
        while i < len(part1) and j >= 0:
            now = part1[i] + part2[j]
            ans = min(ans, abs(now - goal))
            # 贪心的策略
            if now > goal:  # 超了，大的就小一点
                j -= 1
            elif now < goal:  # 小了，小的就大一点
                i += 1
            else:  # 相等了，直接就是0了
                return 0

        return ans


if __name__ == "__main__":
    print(Solution().minAbsDifference(nums=[5, -7, 3, 5], goal=6))  # 0
    print(Solution().minAbsDifference(nums=[7, -9, 15, -2], goal=-5))  # 1
    print(Solution().minAbsDifference(nums=[1, 2, 3], goal=-7))  # 7
