from typing import List


class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        ans = []
        level = 0
        for ch in seq:
            if ch == "(":
                ans.append(level % 2)
                level += 1
            else:
                level -= 1
                ans.append(level % 2)
        return ans


if __name__ == "__main__":
    # [0,1,1,1,1,0]
    print(Solution().maxDepthAfterSplit(seq="(()())"))

    # [0,0,0,1,1,0,1,1]
    print(Solution().maxDepthAfterSplit(seq="()(())()"))
