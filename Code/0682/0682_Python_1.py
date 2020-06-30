from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        marks = []
        for p in ops:
            if p == "+":
                marks.append(marks[-1] + marks[-2])
            elif p == "D":
                marks.append(2 * marks[-1])
            elif p == "C":
                marks.pop(-1)
            else:
                marks.append(int(p))
        return sum(marks)


if __name__ == "__main__":
    print(Solution().calPoints(["5", "2", "C", "D", "+"]))  # 30
    print(Solution().calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))  # 27
