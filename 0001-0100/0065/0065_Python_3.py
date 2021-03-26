class Automaton:
    def __init__(self):
        self.stat = 0
        self.table = {
            -1: [-1, -1, -1, -1, -1],  # 已确定无效的状态
            0: [0, 1, 3, 2, -1],  # 初始状态，尚无符号、小数点和有效数字
            1: [-1, -1, 3, 2, -1],  # 已有符号，尚无小数点、有效数字
            2: [-1, -1, 4, -1, -1],  # 已有符号、小数点，尚无有效数字
            3: [8, -1, 3, 4, 5],  # 已有符号、有效数字，尚无小数部分
            4: [8, -1, 4, -1, 5],  # 已有符号、有效数字和小数部分
            5: [-1, 6, 7, -1, -1],  # 已有e，尚无e后的符号和有效数字
            6: [-1, -1, 7, -1, -1],  # 已有e和e后的符号，尚无e后的有效数字
            7: [8, -1, 7, -1, -1],  # 已有e和e后的符号、有效数字
            8: [8, -1, -1, -1, -1],  # 已结束匹配数字部分
        }
        self.final = [False, False, False, False, True, True, False, False, True, True]  # [-1,8]

    def get(self, ch: str):
        # 计算当前状态
        if ch.isspace():
            self.stat = self.table[self.stat][0]
        elif ch == "+" or ch == "-":
            self.stat = self.table[self.stat][1]
        elif ch.isdigit():
            self.stat = self.table[self.stat][2]
        elif ch == ".":
            self.stat = self.table[self.stat][3]
        elif ch == "e":
            self.stat = self.table[self.stat][4]
        else:
            self.stat = -1

    def end(self):
        return self.final[self.stat + 1]


class Solution:
    def isNumber(self, s: str) -> bool:
        automaton = Automaton()
        for ch in s:
            automaton.get(ch)
        # print(s, ":", automaton.stat)
        return automaton.end()


if __name__ == "__main__":
    print(Solution().isNumber("0"))  # True
    print(Solution().isNumber(" 0.1 "))  # True
    print(Solution().isNumber("abc"))  # False
    print(Solution().isNumber("1 a"))  # False
    print(Solution().isNumber("2e10"))  # True
    print(Solution().isNumber(" -90e3   "))  # True
    print(Solution().isNumber(" 1e"))  # False
    print(Solution().isNumber("e3"))  # False
    print(Solution().isNumber(" 6e-1"))  # True
    print(Solution().isNumber(" 99e2.5 "))  # False
    print(Solution().isNumber("53.5e93"))  # True
    print(Solution().isNumber(" --6 "))  # False
    print(Solution().isNumber("-+3"))  # False
    print(Solution().isNumber("95a54e53"))  # False
    print(Solution().isNumber(".1"))  # True
    print(Solution().isNumber("3."))  # True
