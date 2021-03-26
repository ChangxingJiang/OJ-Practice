from typing import List


class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        n1 = 0  # 局部倒置
        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
                n1 += 1
        n2 = 0  # 全局倒置
        for i in range(len(A)):
            if A[i] > i:
                n2 += (A[i] - i + 1) * (A[i] - i) // 2
        return n1 >= n2


if __name__ == "__main__":
    print(Solution().isIdealPermutation(A=[1, 0, 2]))  # True
    print(Solution().isIdealPermutation(A=[1, 2, 0]))  # False
    print(Solution().isIdealPermutation(A=[2, 1, 0]))  # False
