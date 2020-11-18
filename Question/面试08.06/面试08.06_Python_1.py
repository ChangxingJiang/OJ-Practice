from typing import List


class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        while A:
            B.append(A.pop())
        while B:
            C.append(B.pop())


if __name__ == "__main__":
    a, b, c = [2, 1, 0], [], []
    Solution().hanota(a, b, c)
    print(c)

    a, b, c = [1, 0], [], []
    Solution().hanota(a, b, c)
    print(c)
