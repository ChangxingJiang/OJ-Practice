from typing import List


class Solution:
    def reverseWords(self, s: List[str]) -> None:
        s[:] = list(" ".join(reversed("".join(s).split(" "))))


if __name__ == "__main__":
    # ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
    lst = ["t", "h", "e", " ", "s", "k", "y", " ", "i", "s", " ", "b", "l", "u", "e"]
    Solution().reverseWords(lst)
    print(lst)
