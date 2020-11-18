import math
from typing import List


def comb(n, m):
    return math.factorial(n) // (math.factorial(n - m) * math.factorial(m))


class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        step_h = destination[1]  # 向右的步数
        step_v = destination[0]  # 向下的步数

        ans = []

        while k and step_h and step_v:
            nums = comb(step_h + step_v - 1, step_v)  # 如果当前位置为H，后续能够提供的最大数量
            # print(step_h + step_v - 1, step_v, "->", nums)
            if k > nums:
                ans.append("V")
                k -= nums
                step_v -= 1
            else:
                ans.append("H")
                step_h -= 1
            # print(ans)

        ans += ["H"] * step_h
        ans += ["V"] * step_v

        return "".join(ans)


if __name__ == "__main__":
    print(Solution().kthSmallestPath(destination=[2, 3], k=1))  # HHHVV
    print(Solution().kthSmallestPath(destination=[2, 3], k=2))  # HHVHV
    print(Solution().kthSmallestPath(destination=[2, 3], k=3))  # HHVVH
