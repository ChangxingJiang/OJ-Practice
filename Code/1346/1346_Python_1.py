from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hashmap = set()
        for n in arr:
            if n * 2 in hashmap or n / 2 in hashmap:
                return True
            else:
                hashmap.add(n)
        else:
            return False


if __name__ == "__main__":
    print(Solution().checkIfExist(arr=[10, 2, 5, 3]))  # True
    print(Solution().checkIfExist(arr=[7, 1, 14, 11]))  # True
    print(Solution().checkIfExist(arr=[3, 1, 7, 11]))  # False
