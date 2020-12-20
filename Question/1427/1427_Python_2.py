from typing import List


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        num = 0
        for direction, amount in shift:
            if direction == 1:
                num += amount
            else:
                num -= amount

        num %= len(shift)

        if num > 0:
            s = s[len(s) - num:] + s[:len(s) - num]
        else:
            s = s[num:] + s[:num]

        return s


if __name__ == "__main__":
    print(Solution().stringShift(s="abc", shift=[[0, 1], [1, 2]]))  # "cab"
    print(Solution().stringShift(s="abcdefg", shift=[[1, 1], [1, 1], [0, 2], [1, 3]]))  # "efgabcd"
