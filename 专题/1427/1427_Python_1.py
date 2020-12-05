from typing import List


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        pass


if __name__ == "__main__":
    print(Solution().stringShift(s="abc", shift=[[0, 1], [1, 2]]))  # "cab"
    print(Solution().stringShift(s="abcdefg", shift=[[1, 1], [1, 1], [0, 2], [1, 3]]))  # "efgabcd"
