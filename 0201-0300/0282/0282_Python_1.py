from typing import List


class Solution:
    def __init__(self):
        self.size = 0
        self.num = []
        self.now = []
        self.sign = []

    def addOperators(self, num: str, target: int) -> List[str]:
        if not num:
            return []

        self.size = len(num)
        self.num = num
        self.now.append(num[0])
        self.dfs(0, num[0] == "0")

        ans = []
        for ss in self.sign:
            if eval(ss) == target:
                ans.append(ss)
        return ans

    def dfs(self, i, zero_start):
        if i == self.size - 1:
            self.sign.append("".join(self.now))
        else:
            # 递归+
            self.now.extend(["+", self.num[i + 1]])
            self.dfs(i + 1, self.num[i + 1] == "0")
            self.now.pop()
            self.now.pop()

            # 递归-
            self.now.extend(["-", self.num[i + 1]])
            self.dfs(i + 1, self.num[i + 1] == "0")
            self.now.pop()
            self.now.pop()

            # 递归*
            self.now.extend(["*", self.num[i + 1]])
            self.dfs(i + 1, self.num[i + 1] == "0")
            self.now.pop()
            self.now.pop()

            # 递归空
            if not zero_start:
                self.now.extend([self.num[i + 1]])
                self.dfs(i + 1, False)
                self.now.pop()


if __name__ == "__main__":
    print(Solution().addOperators(num="123", target=6))  # ["1+2+3", "1*2*3"]
    print(Solution().addOperators(num="232", target=8))  # ["2*3+2", "2+3*2"]
    print(Solution().addOperators(num="105", target=5))  # ["1*0+5","10-5"]
    print(Solution().addOperators(num="00", target=0))  # ["0+0", "0-0", "0*0"]
    print(Solution().addOperators(num="3456237490", target=9191))  # []
