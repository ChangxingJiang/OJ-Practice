from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        ans = 0
        n1, n2 = [], []

        for num in nums:
            mod = num % 3
            if mod == 0:
                ans += num
            elif mod == 1:
                n1.append(num)
            else:
                n2.append(num)

        n1.sort()
        n2.sort()

        if len(n1) < len(n2):
            n1, n2 = n2, n1

        if (len(n1) - len(n2)) % 3 == 2:
            return ans + max(sum(n1[2:]) + sum(n2),
                             (sum(n1) + sum(n2[1:])) if len(n1) >= 3 and len(n2) >= 1 else 0)
        elif (len(n1) - len(n2)) % 3 == 1:
            return ans + max(sum(n1[1:]) + sum(n2),
                             (sum(n1) + sum(n2[2:])) if len(n1) >= 3 and len(n2) >= 2 else 0)
        else:
            return ans + sum(n1) + sum(n2)


if __name__ == "__main__":
    print(Solution().maxSumDivThree(nums=[3, 6, 5, 1, 8]))  # 18
    print(Solution().maxSumDivThree(nums=[4]))  # 0
    print(Solution().maxSumDivThree(nums=[1, 2, 3, 4, 4]))  # 12
    print(Solution().maxSumDivThree(nums=[2, 3, 36, 8, 32, 38, 3, 30, 13, 40]))  # 195
