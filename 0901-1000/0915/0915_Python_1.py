from typing import List


class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        lst1 = []
        lst2 = []
        for n in A:
            if not lst1 or lst1[-1] < n:
                lst1.append(n)
            else:
                lst1.append(lst1[-1])
        for n in A[::-1]:
            if not lst2 or lst2[-1] > n:
                lst2.append(n)
            else:
                lst2.append(lst2[-1])
        lst2.reverse()

        print(lst1, lst2)

        for i in range(len(A) - 1):
            if lst1[i] <= lst2[i + 1]:
                return i + 1


if __name__ == "__main__":
    print(Solution().partitionDisjoint([5, 0, 3, 8, 6]))  # 3
    print(Solution().partitionDisjoint([1, 1, 1, 0, 6, 12]))  # 4
    print(Solution().partitionDisjoint([1, 1]))  # 4
