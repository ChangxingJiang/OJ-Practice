from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()


if __name__ == "__main__":
    s = ["h", "e", "l", "l", "o"]
    print(Solution().reverseString(s), s)  # ["o","l","l","e","h"]
    s = ["H", "a", "n", "n", "a", "h"]
    print(Solution().reverseString(s), s)  # ["h","a","n","n","a","H"]
