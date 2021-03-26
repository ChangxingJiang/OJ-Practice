from typing import List


class Solution:
    def __init__(self):
        self.ans = []
        self.now = []
        self.s = ""
        self.is_palindrome = []
        self.size = 0

    def partition(self, s: str) -> List[List[str]]:
        self.size = len(s)
        self.s = s

        # 计算是否为回文串
        self.is_palindrome = [[False] * self.size for _ in range(self.size)]
        for r in range(self.size):
            for l in range(r, -1, -1):
                if s[l] == s[r] and (r - l <= 2 or self.is_palindrome[l + 1][r - 1]):
                    self.is_palindrome[l][r] = True

        self.dfs(0, 0)
        return self.ans

    def dfs(self, i1, i2):
        if i2 == self.size - 1:
            if self.is_palindrome[i1][i2]:
                self.now.append(self.s[i1:i2 + 1])
                self.ans.append(list(self.now))
                self.now.pop()
        else:
            # 在当前位置切分
            if self.is_palindrome[i1][i2]:
                self.now.append(self.s[i1:i2 + 1])
                self.dfs(i2 + 1, i2 + 1)
                self.now.pop()

            # 不在当前位置切分
            self.dfs(i1, i2 + 1)


if __name__ == "__main__":
    # [
    #   ["aa","b"],
    #   ["a","a","b"]
    # ]
    print(Solution().partition("aab"))
