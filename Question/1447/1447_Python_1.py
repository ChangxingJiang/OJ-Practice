import math
from typing import List


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                if math.gcd(i, j) == 1:
                    ans.append(str(i) + "/" + str(j))
        return ans


if __name__ == "__main__":
    print(Solution().simplifiedFractions(2))  # ["1/2"]
    print(Solution().simplifiedFractions(3))  # ["1/2","1/3","2/3"]
    print(Solution().simplifiedFractions(4))  # ["1/2","1/3","1/4","2/3","3/4"]
    print(Solution().simplifiedFractions(1))  # []
