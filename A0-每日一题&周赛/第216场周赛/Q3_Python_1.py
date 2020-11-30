from typing import List


class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:

        t1, t2 = 0, 0
        for i, n in enumerate(nums):
            if i % 2 == 1:
                t1 += n
            else:
                t2 += n

        # print("奇数和:", t1, "偶数和:", t2)

        ans = 0

        n1, n2 = 0, 0
        for i, n in enumerate(nums):
            s1 = t1 - n1
            s2 = t2 - n2
            if i % 2 == 1:
                s1 -= n
            else:
                s2 -= n

            if n1 + s2 == n2 + s1:
                ans += 1

            if i % 2 == 1:
                n1 += n
            else:
                n2 += n

        return ans


if __name__ == "__main__":
    print(Solution().waysToMakeFair([6, 1, 7, 4, 1]))  # 0
    print(Solution().waysToMakeFair([2, 1, 6, 4]))  # 1
    print(Solution().waysToMakeFair([1, 1, 1]))  # 3
    print(Solution().waysToMakeFair([1, 2, 3]))  # 0
