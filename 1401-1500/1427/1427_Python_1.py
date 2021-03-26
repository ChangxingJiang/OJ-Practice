from typing import List


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        for direction, amount in shift:
            if direction == 1:
                s = s[len(s) - amount:] + s[:len(s) - amount]
            else:
                s = s[amount:] + s[:amount]
        return s


if __name__ == "__main__":
    print(Solution().stringShift(s="abc", shift=[[0, 1], [1, 2]]))  # "cab"
    print(Solution().stringShift(s="abcdefg", shift=[[1, 1], [1, 1], [0, 2], [1, 3]]))  # "efgabcd"
