from typing import List


class Solution:
    def fraction(self, cont: List[int]) -> List[int]:
        n1, n2 = cont.pop(), 1

        while cont:
            n1, n2 = n2, n1
            n1 += n2 * cont.pop()

        return [n1, n2]


if __name__ == "__main__":
    print(Solution().fraction(cont=[3, 2, 0, 2]))  # [13, 4]
    print(Solution().fraction(cont=[0, 0, 3]))  # [3, 1]
