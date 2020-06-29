from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        block = []
        hashmap = {}
        for n in nums2:
            while len(block) > 0:
                if n > block[-1]:
                    hashmap[block.pop(-1)] = n
                else:
                    break
            block.append(n)
        else:
            for n in block:
                hashmap[n] = -1

        return [hashmap[n] for n in nums1]


if __name__ == "__main__":
    print(Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))  # [-1,3,-1]
    print(Solution().nextGreaterElement([2, 4], [1, 2, 3, 4]))  # [3,-1]
