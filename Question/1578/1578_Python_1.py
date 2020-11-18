from typing import List


class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        ans = 0
        i, j = 0, 0
        while i < len(s) and j < len(s):
            if s[j] == s[i]:
                j += 1
            else:
                if j - i > 1:
                    ans += sum(cost[i:j]) - max(cost[i:j])
                i = j
        else:
            if j - i > 1:
                ans += sum(cost[i:j]) - max(cost[i:j])
        return ans


if __name__ == "__main__":
    print(Solution().minCost("abaac", [1, 2, 3, 4, 5]))  # 3
    print(Solution().minCost("abc", [1, 2, 3]))  # 0
    print(Solution().minCost("aabaa", [1, 2, 3, 4, 1]))  # 2
    print(Solution().minCost("bbbaaa", [4, 9, 3, 8, 8, 9]))  # 23
