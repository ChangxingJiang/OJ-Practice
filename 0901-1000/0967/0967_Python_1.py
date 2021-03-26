from typing import List


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        bit = 10 ** (n - 1)
        ans = []

        def dfs(now):
            if now < bit:
                v1 = now % 10
                for v2 in {v1 - k, v1 + k}:
                    if 0 <= v2 <= 9:
                        dfs(now * 10 + v2)
            else:
                ans.append(now)

        for i in range(1, 10):
            dfs(i)

        return ans


if __name__ == "__main__":
    # [181,292,707,818,929]
    print(Solution().numsSameConsecDiff(3, 7))

    # [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
    print(Solution().numsSameConsecDiff(2, 1))
