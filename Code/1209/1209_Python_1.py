import re


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        s, num = re.subn(r"(.)\1{" + str(k - 1) + "}", "", s)
        while num:
            s, num = re.subn(r"(.)\1{" + str(k - 1) + "}", "", s)
        return s


if __name__ == "__main__":
    print(Solution().removeDuplicates(s="abcd", k=2))  # "abcd"
    print(Solution().removeDuplicates(s="deeedbbcccbdaa", k=3))  # "aa"
    print(Solution().removeDuplicates(s="pbbcggttciiippooaais", k=2))  # "ps"
