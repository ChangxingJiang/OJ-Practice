import collections
from typing import List


class Solution:
    def maxGroupNumber(self, tiles: List[int]) -> int:
        count = collections.Counter(tiles)
        nums = sorted(count.keys())

        ans = 0

        n1, n2 = -3, -2
        l1, l2 = 0, 0
        for n3 in nums:
            l3 = count[n3]

            print(n1, n2, n3, ":", l1, l2, l3, "=", ans)

            # 第3个数字与第二个数字间隔1个以上的情况
            # 例如：1 2 . 4
            if n3 >= n2 + 2:
                ans += l1 // 3 + l2 // 3
                n1, n2 = n3 - 1, n3
                l1, l2 = 0, l3

            # 三个相邻数字的情况
            # 例如：1 2 3
            else:  # n3 == n2 + 1
                group = min(l1, l2, l3)
                s1, s2 = l1 - group, l2 - group

                # 例如l1,l2,l3：4 2 2
                if s1 % 3 == 2 and group >= 1:
                    l2 -= (group - 1)
                    l3 -= (group - 1)
                    ans += (group - 1) + (s1 + 1) // 3

                # 例如l1,l2,l3：2 4 2
                elif s2 % 3 == 2 and group >= 1:
                    l2 -= (group - 1)
                    l3 -= (group - 1)
                    ans += (group - 1) + (s1 + 1) // 3

                # 例如l1,l2,l3：3 3 2
                elif s1 % 3 == 1 and s2 % 3 == 1 and group >= 2:
                    l2 -= (group - 2)
                    l3 -= (group - 2)
                    ans += (group - 2) + (s1 + 2) // 3

                else:
                    l2 -= group
                    l3 -= group
                    ans += group + s1 // 3

                n1, n2 = n2, n3
                l1, l2 = l2, l3

        ans += l1 // 3 + l2 // 3

        return ans


if __name__ == "__main__":
    print(Solution().maxGroupNumber([2, 2, 2, 3, 4]))  # 1
    print(Solution().maxGroupNumber([2, 2, 2, 3, 4, 1, 3]))  # 2

    # 自制用例
    print(Solution().maxGroupNumber([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 4, 4, 5, 5]))  # 4
    print(Solution().maxGroupNumber([1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 4, 4, 5, 5]))  # 4
    print(Solution().maxGroupNumber([1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4]))  # 5
    print(Solution().maxGroupNumber([1, 1, 2, 2, 3, 3, 5, 5, 5, 6, 6, 6]))  # 4
    print(Solution().maxGroupNumber([1, 1, 2, 2, 2, 2, 3, 3, 4, 5]))  # 3
    print(Solution().maxGroupNumber([1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5]))  # 5
