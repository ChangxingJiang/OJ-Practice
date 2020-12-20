from typing import List


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        pass


if __name__ == "__main__":
    print(Solution().simplifiedFractions(2))  # ["1/2"]
    print(Solution().simplifiedFractions(3))  # ["1/2","1/3","2/3"]
    print(Solution().simplifiedFractions(4))  # ["1/2","1/3","1/4","2/3","3/4"]
    print(Solution().simplifiedFractions(1))  # []
