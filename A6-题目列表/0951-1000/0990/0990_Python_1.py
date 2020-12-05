from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        pass


if __name__ == "__main__":
    print(Solution().equationsPossible(["a==b", "b!=a"]))  # False
    print(Solution().equationsPossible(["b==a", "a==b"]))  # True
    print(Solution().equationsPossible(["a==b", "b==c", "a==c"]))  # True
    print(Solution().equationsPossible(["a==b", "b!=c", "c==a"]))  # False
    print(Solution().equationsPossible(["c==c", "b==d", "x!=z"]))  # True
