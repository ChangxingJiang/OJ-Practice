import collections
from typing import List


class Solution:
    def maxGroupNumber(self, tiles: List[int]) -> int:
        count = collections.Counter(tiles)
        nums = sorted(count.keys())

        ans1 = 0
        for n in nums:
            if count[n] > 3:
                if count[n] % 3 == 0:
                    ans1 += count[n] // 3 - 1
                    count[n] = 3
                else:
                    ans1 += count[n] // 3
                    count[n] %= 3

        n2 = -2

        dp1 = {(0, 0): 0}  # dp[i]=[前2个数，前1个数，当前牌组数]

        for n3 in nums:
            l3 = count[n3]
            print(n3, l3, ":", dp1)

            # 第3个数字与第二个数字间隔1个以上的情况
            # 例如：1 2 . 4
            if n3 >= n2 + 2:
                res = 0
                for (l1, l2) in dp1:
                    v = dp1[(l1, l2)]
                    res = max(res, v + l1 // 3 + l2 // 3)
                dp1 = {(0, l3): res}
                n2 = n3
                continue

            # 三个相邻数字的情况
            # 例如：1 2 3

            dp2 = {}

            for (l1, l2), v in dp1.items():
                group = min(l1, l2, l3)

                # 使用当前可能的最大顺子组
                ll2, ll3 = l2 - group, l3 - group
                if (ll2, ll3) not in dp2 or dp2[(ll2, ll3)] < v + group:
                    dp2[(ll2, ll3)] = v + group + (l1 - group) // 3

                # 使用当前最大顺子组-1
                if group >= 1:
                    ll2, ll3 = l2 - (group - 1), l3 - (group - 1)
                    if (ll2, ll3) not in dp2 or dp2[(ll2, ll3)] < v + (group - 1):
                        dp2[(ll2, ll3)] = v + (group - 1) + (l1 - group + 1) // 3

                # 使用当前最大顺子组-2
                if group >= 2:
                    ll2, ll3 = l2 - (group - 2), l3 - (group - 2)
                    if (ll2, ll3) not in dp2 or dp2[(ll2, ll3)] < v + (group - 2):
                        dp2[(ll2, ll3)] = v + (group - 2) + (l1 - group + 2) // 3

                # 使用当前最大顺子组-3
                if group >= 3:
                    ll2, ll3 = l2 - (group - 3), l3 - (group - 3)
                    if (ll2, ll3) not in dp2 or dp2[(ll2, ll3)] < v + (group - 3):
                        dp2[(ll2, ll3)] = v + (group - 3) + (l1 - group + 3) // 3

            dp1 = dp2
            n2 = n3

        # 选择最大的结果
        ans2 = 0
        for (l1, l2), v in dp1.items():
            ans2 = max(ans2, v + l1 // 3 + l2 // 3)

        return ans1 + ans2


if __name__ == "__main__":
    print(Solution().maxGroupNumber([2, 2, 2, 3, 4]))  # 1
    print(Solution().maxGroupNumber([2, 2, 2, 3, 4, 1, 3]))  # 2

    # 自制用例
    print(Solution().maxGroupNumber([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 4, 4, 5, 5]))  # 4
    print(Solution().maxGroupNumber([1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 4, 4, 5, 5]))  # 4
    print(Solution().maxGroupNumber([1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4]))  # 4
    print(Solution().maxGroupNumber([1, 1, 2, 2, 3, 3, 5, 5, 5, 6, 6, 6]))  # 4
    print(Solution().maxGroupNumber([1, 1, 2, 2, 2, 2, 3, 3, 4, 5]))  # 3
    print(Solution().maxGroupNumber([1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5]))  # 4
    print(Solution().maxGroupNumber([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5]))  # 4
    print(Solution().maxGroupNumber([1]))  # 1
    print(Solution().maxGroupNumber(
        [1, 1,
         2, 2, 2, 2, 2,
         3, 3, 3, 3,
         4, 4, 4, 4, 4, 4,
         5, 5,
         6, 6, 6, 6, 6,
         7, 7, 7, 7,
         8, 8, 8,
         9, 9,
         10, 10, 10, 10,
         11, 11, 11, 12]))  # 1
