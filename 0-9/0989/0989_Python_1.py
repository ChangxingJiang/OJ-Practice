from typing import List


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        pass


if __name__ == "__main__":
    print(Solution().addToArrayForm(A=[1, 2, 0, 0], K=34))  # [1,2,3,4]
    print(Solution().addToArrayForm(A=[2, 7, 4], K=181))  # [4,5,5]
    print(Solution().addToArrayForm(A=[2, 1, 5], K=806))  # [1,0,2,1]
    print(Solution().addToArrayForm(A=[9, 9, 9, 9, 9, 9, 9, 9, 9, 9], K=1))  # [1,0,0,0,0,0,0,0,0,0,0]
