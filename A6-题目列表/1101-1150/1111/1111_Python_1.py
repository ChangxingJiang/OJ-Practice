from typing import List


class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        pass


if __name__ == "__main__":
    # [0,1,1,1,1,0]
    print(Solution().maxDepthAfterSplit(seq="(()())"))

    # [0,0,0,1,1,0,1,1]
    print(Solution().maxDepthAfterSplit(seq="()(())()"))
