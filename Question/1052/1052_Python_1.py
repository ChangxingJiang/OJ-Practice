from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        size = len(customers)

        lst1 = []
        lst2 = []
        for i in range(size):
            if grumpy[i] == 0:
                lst1.append(customers[i])
                lst2.append(0)
            else:
                lst1.append(0)
                lst2.append(customers[i])

        left = right = now = ans = 0
        while right < size:
            now += lst2[right]
            if right - left + 1 > X:
                now -= lst2[left]
                left += 1
            right += 1
            ans = max(ans, now)

        return sum(lst1) + ans


if __name__ == "__main__":
    print(Solution().maxSatisfied(customers=[1, 0, 1, 2, 1, 1, 7, 5], grumpy=[0, 1, 0, 1, 0, 1, 0, 1], X=3))  # 16
