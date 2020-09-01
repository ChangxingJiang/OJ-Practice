INT_MIN = -2 ** 31
INT_MAX = 2 ** 31 - 1


class Automaton:
    def __init__(self):
        self.stat = "start"
        self.sign = 1
        self.ans = 0
        self.table = {
            "start": ["start", "signed", "number", "end"],
            "signed": ["end", "end", "number", "end"],
            "number": ["end", "end", "number", "end"],
            "end": ["end", "end", "end", "end"],
        }

    def get(self, ch: str):
        # 计算当前状态
        if ch.isspace():
            self.stat = self.table[self.stat][0]
        elif ch == "+" or ch == "-":
            self.stat = self.table[self.stat][1]
        elif ch.isdigit():
            self.stat = self.table[self.stat][2]
        else:
            self.stat = self.table[self.stat][3]
        # 计算当前变化
        if self.stat == "number":
            self.ans = 10 * self.ans + int(ch)
            self.ans = min(self.ans, INT_MAX) if self.sign == 1 else min(self.ans, -INT_MIN)
        elif self.stat == "signed":
            self.sign = 1 if ch == "+" else -1


class Solution:
    def myAtoi(self, str: str) -> int:
        automaton = Automaton()
        for ch in str:
            automaton.get(ch)
        return automaton.sign * automaton.ans


if __name__ == "__main__":
    print(Solution().myAtoi("42"))  # 42
    print(Solution().myAtoi("   -42"))  # -42
    print(Solution().myAtoi("4193 with words"))  # 4193
    print(Solution().myAtoi("words and 987"))  # 0
    print(Solution().myAtoi("-91283472332"))  # -2147483648
    print(Solution().myAtoi("+1"))  # 1
    print(Solution().myAtoi("  0000000000012345678"))  # 12345678
    print(Solution().myAtoi("-000000000000000001"))  # -1
    print(Solution().myAtoi("   +0 123"))  # 0
    print(Solution().myAtoi("0-1"))  # 0
    print(Solution().myAtoi("010"))  # 10
