from typing import List


class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        hashmap = set()
        for a in A:
            if a not in hashmap:
                hashmap.add(a)
            else:
                return a


if __name__ == "__main__":
    print(Solution().repeatedNTimes([1, 2, 3, 3]))  # 3
    print(Solution().repeatedNTimes([2, 1, 2, 5, 3, 2]))  # 2
    print(Solution().repeatedNTimes([5, 1, 5, 2, 5, 3, 5, 4]))  # 5
