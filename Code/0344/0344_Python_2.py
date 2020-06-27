from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        i = 0
        j = len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1


if __name__ == "__main__":
    s = ["h", "e", "l", "l", "o"]
    print(Solution().reverseString(s), s)  # ["o","l","l","e","h"]
    s = ["H", "a", "n", "n", "a", "h"]
    print(Solution().reverseString(s), s)  # ["h","a","n","n","a","H"]
