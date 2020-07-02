from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        odd = []
        even = []
        for a in A:
            if a % 2 == 0:
                even.append(a)
            else:
                odd.append(a)
        return even+odd


if __name__ == "__main__":
    print(Solution().sortArrayByParity([3, 1, 2, 4]))  # [2,4,3,1]
