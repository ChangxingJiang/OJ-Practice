from typing import List


class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        i, i1, i2 = m + n - 1, m - 1, n - 1
        while True:
            if i1 >= 0 and i2 >= 0:
                if A[i1] >= B[i2]:
                    A[i] = A[i1]
                    i -= 1
                    i1 -= 1
                else:
                    A[i] = B[i2]
                    i -= 1
                    i2 -= 1
            elif i1 >= 0:
                A[i] = A[i1]
                i -= 1
                i1 -= 1
            elif i2 >= 0:
                A[i] = B[i2]
                i -= 1
                i2 -= 1
            else:
                break


if __name__ == "__main__":
    # [1,2,2,3,5,6]
    A, B = [1, 2, 3, 0, 0, 0], [2, 5, 6]
    Solution().merge(A=A, m=3, B=B, n=3)
    print(A)
