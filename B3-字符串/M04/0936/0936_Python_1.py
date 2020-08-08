from typing import List


class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        pass


if __name__ == "__main__":
    print(Solution().movesToStamp(stamp="abc", target="ababc"))  # [0,2]
    print(Solution().movesToStamp(stamp="abca", target="aabcaca"))  # [3,0,1]
