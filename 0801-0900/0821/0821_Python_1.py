from typing import List


class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        ans = [float("inf") for _ in range(len(S))]
        for i in range(len(S)):
            if S[i] == C:
                ans[i] = 0
            elif i > 0:
                ans[i] = ans[i - 1] + 1
        for i in range(len(S) - 1, -1, -1):
            if S[i] == C:
                ans[i] = 0
            elif i < len(S) - 1:
                ans[i] = min(ans[i], ans[i + 1] + 1)
        return ans


if __name__ == "__main__":
    print(Solution().shortestToChar("loveleetcode", "e"))  # [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
