from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s1 = set()
        s2 = set()
        for n in nums:
            if n not in s2:
                if n in s1:
                    s1.remove(n)
                    s2.add(n)
                else:
                    s1.add(n)

        return s1.pop()


if __name__ == "__main__":
    print(Solution().singleNumber([3, 4, 3, 3]))  # 4
    print(Solution().singleNumber([9, 1, 7, 9, 7, 9, 7]))  # 1
