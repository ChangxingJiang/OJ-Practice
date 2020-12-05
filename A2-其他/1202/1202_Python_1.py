from typing import List


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        pass


if __name__ == "__main__":
    # "bacd"
    print(Solution().smallestStringWithSwaps(s="dcab", pairs=[[0, 3], [1, 2]]))

    # "abcd"
    print(Solution().smallestStringWithSwaps(s="dcab", pairs=[[0, 3], [1, 2], [0, 2]]))

    # "abc"
    print(Solution().smallestStringWithSwaps(s="cba", pairs=[[0, 1], [1, 2]]))
