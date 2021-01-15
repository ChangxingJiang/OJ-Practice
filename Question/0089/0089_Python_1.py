from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = []

        gray = 0
        while len(ans) < 2 ** n:
            ans.append(gray)
            gray ^= 1
            ans.append(gray)
            gray ^= (gray & -gray) << 1

        return ans


if __name__ == "__main__":
    print(Solution().grayCode(2))  # [0,1,3,2]
    print(Solution().grayCode(0))  # [0]
