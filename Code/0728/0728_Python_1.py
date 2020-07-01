from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left, right + 1):
            s = str(i)
            if "0" not in s and all([i % int(c) == 0 for c in s]):
                ans.append(i)
        return ans


if __name__ == "__main__":
    print(Solution().selfDividingNumbers(1, 22))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
