from typing import List


class Solution:
    def expand(self, S: str) -> List[str]:
        pass


if __name__ == "__main__":
    print(Solution().expand("{a,b}c{d,e}f"))  # ["acdf","acef","bcdf","bcef"]
    print(Solution().expand("abcd"))  # ["abcd"]
