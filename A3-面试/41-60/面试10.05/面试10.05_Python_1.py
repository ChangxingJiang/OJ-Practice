from typing import List


class Solution:
    def findString(self, words: List[str], s: str) -> int:
        pass


if __name__ == "__main__":
    # -1
    print(Solution().findString(words=["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""], s="ta"))

    # 4
    print(Solution().findString(words=["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""], s="ball"))
