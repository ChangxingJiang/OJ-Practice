from typing import List


class Solution:
    def splitLoopedString(self, strs: List[str]) -> str:
        lst = []
        for s in strs:
            if s > s[::-1]:
                lst.append(s)
            else:
                lst.append(s[::-1])

        ans = "".join(lst)

        for i, s in enumerate(lst):
            other = "".join(lst[i + 1:] + lst[:i])
            for j in range(len(s)):
                head = s[j:]
                tail = s[:j]
                ans = max(ans, head + other + tail, tail[::-1] + other + head[::-1])

        return ans


if __name__ == "__main__":
    print(Solution().splitLoopedString(["abc", "xyz"]))  # "zyxcba"
    print(Solution().splitLoopedString(["yzy", "aba"]))  # "zyabay"
    print(Solution().splitLoopedString(["lc", "evol", "cdy"]))  # "ylclovecd"
