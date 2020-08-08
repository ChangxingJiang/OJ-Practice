from typing import List


class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        pass


if __name__ == "__main__":
    print(Solution().splitIntoFibonacci("123456579"))  # [123,456,579]
    print(Solution().splitIntoFibonacci("11235813"))  # [1,1,2,3,5,8,13]
    print(Solution().splitIntoFibonacci("112358130"))  # []
    print(Solution().splitIntoFibonacci("0123"))  # []
    print(Solution().splitIntoFibonacci("1101111"))  # [110, 1, 111]
