from typing import List


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        hashmap = {}
        for d in deck:
            if d not in hashmap:
                hashmap[d] = 1
            else:
                hashmap[d] += 1

        nums = list(hashmap.values())
        i = 2
        while i <= min(nums):
            for n in nums:
                if n % i != 0:
                    break
            else:
                return True
            i += 1
        return False


if __name__ == "__main__":
    print(Solution().hasGroupsSizeX([1, 2, 3, 4, 4, 3, 2, 1]))  # True
    print(Solution().hasGroupsSizeX([1, 1, 1, 2, 2, 2, 3, 3]))  # False
    print(Solution().hasGroupsSizeX([1]))  # False
    print(Solution().hasGroupsSizeX([1, 1]))  # True
    print(Solution().hasGroupsSizeX([1, 1, 2, 2, 2, 2]))  # True
