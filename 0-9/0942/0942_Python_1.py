from typing import List


class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        pass


if __name__ == "__main__":
    print(Solution().diStringMatch("IDID"))  # [0,4,1,3,2]
    print(Solution().diStringMatch("III"))  # [0,1,2,3]
    print(Solution().diStringMatch("DDI"))  # [3,2,0,1]
