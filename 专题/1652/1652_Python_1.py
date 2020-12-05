from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        pass


if __name__ == "__main__":
    print(Solution().decrypt(code=[5, 7, 1, 4], k=3))  # [12,10,16,13]
    print(Solution().decrypt(code=[1, 2, 3, 4], k=0))  # [0,0,0,0]
    print(Solution().decrypt(code=[2, 4, 9, 3], k=-2))  # [12,5,6,13]
