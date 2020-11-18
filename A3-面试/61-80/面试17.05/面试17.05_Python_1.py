from typing import List


class Solution:
    def findLongestSubarray(self, array: List[str]) -> List[str]:
        pass


if __name__ == "__main__":
    # ["A","1","B","C","D","2","3","4","E","5","F","G","6","7"]
    print(Solution().findLongestSubarray(
        ["A", "1", "B", "C", "D", "2", "3", "4", "E", "5", "F", "G", "6", "7", "H", "I", "J", "K", "L", "M"]))

    # []
    print(Solution().findLongestSubarray(["A", "A"]))
