from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        ans = 0
        now = []
        for n in arr:
            if len(now) == 0:
                now.append(n)
                ans = max(ans, len(now))
            elif len(now) == 1:
                if now[-1] != n:
                    now.append(n)
                    ans = max(ans, len(now))
                else:
                    pass
            elif len(now) == 2 and (now[-1] - now[-2]) * (n - now[-1]) > 0:
                now = [now[-1], n]
            elif (now[-1] - now[-2]) * (n - now[-1]) < 0:
                now.append(n)
                ans = max(ans, len(now))
            else:
                now = [now[-1], n]
        return ans


if __name__ == "__main__":
    print(Solution().maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9]))  # 5
    print(Solution().maxTurbulenceSize([4, 8, 12, 16]))  # 2
    print(Solution().maxTurbulenceSize([100]))  # 1
    print(Solution().maxTurbulenceSize([9, 9]))  # 1
    print(Solution().maxTurbulenceSize([0, 1, 1, 0, 1, 0, 1, 1, 0, 0]))  # 5
    print(Solution().maxTurbulenceSize([2, 0, 2, 4, 2, 5, 0, 1, 2, 3]))  # 6
