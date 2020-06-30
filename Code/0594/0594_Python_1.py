from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        hashmap = {}
        for n in nums:
            if n not in hashmap:
                hashmap[n] = 1
            else:
                hashmap[n] += 1
        maximum = 0
        for k in hashmap:
            if k - 1 in hashmap:
                v = hashmap[k] + hashmap[k - 1]
                if v > maximum:
                    maximum = v
        return maximum


if __name__ == "__main__":
    print(Solution().findLHS([1, 3, 2, 2, 5, 2, 3, 7]))  # [3,2,2,2,3]
