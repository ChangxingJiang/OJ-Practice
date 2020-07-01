from typing import List


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        pass


if __name__ == "__main__":
    print(Solution().hasGroupsSizeX([1, 2, 3, 4, 4, 3, 2, 1]))  # True
    print(Solution().hasGroupsSizeX([1, 1, 1, 2, 2, 2, 3, 3]))  # False
    print(Solution().hasGroupsSizeX([1]))  # False
    print(Solution().hasGroupsSizeX([1, 1]))  # True
