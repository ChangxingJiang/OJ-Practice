from typing import List


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        # 计算各位之间的差
        lst = [nums[i + 1] - nums[i] for i in range(len(nums) - 1)]

        # 计算前缀值和后缀值
        pre1 = [(i + 1) * lst[i] for i in range(len(lst))]
        suf1 = [(len(lst) - i) * lst[i] for i in range(len(lst))]

        # 计算前缀积的前缀值、后缀值的后缀和
        now = 0
        pre2 = [0]
        for i in range(len(pre1)):
            now += pre1[i]
            pre2.append(now)
        now = 0
        suf2 = [0]
        for i in range(len(suf1) - 1, -1, -1):
            now += suf1[i]
            suf2.append(now)
        suf2.reverse()

        # 计算最终结果
        ans = []
        for i in range(len(nums)):
            ans.append(pre2[i] + suf2[i])
        return ans


if __name__ == "__main__":
    print(Solution().getSumAbsoluteDifferences([2, 3, 5]))  # [4,3,5]
    print(Solution().getSumAbsoluteDifferences([1, 4, 6, 8, 10]))  # [24,15,13,15,21]
