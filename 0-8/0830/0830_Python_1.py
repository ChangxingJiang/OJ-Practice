from typing import List


class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        pass


if __name__ == "__main__":
    print(Solution().largeGroupPositions("abbxxxxzzy"))  # [[3,6]]
    print(Solution().largeGroupPositions("abc"))  # []
    print(Solution().largeGroupPositions("abcdddeeeeaabbbcd"))  # [[3,5],[6,9],[12,14]]
