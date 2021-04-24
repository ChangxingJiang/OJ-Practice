from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        s1 = set()
        s2 = set()
        for num in nums:
            if num not in s2:
                if num not in s1:
                    s1.add(num)
                else:
                    s1.remove(num)
                    s2.add(num)
        return sum(s1)


if __name__ == "__main__":
    print(Solution().sumOfUnique([1, 2, 3, 2]))  # 4
    print(Solution().sumOfUnique([1, 1, 1, 1, 1]))  # 0
    print(Solution().sumOfUnique([1, 2, 3, 4, 5]))  # 15
