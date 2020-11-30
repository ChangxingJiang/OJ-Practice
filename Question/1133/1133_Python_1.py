from typing import List


class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        remove = set()
        number = set()
        for n in A:
            if n not in remove:
                if n not in number:
                    number.add(n)
                else:
                    number.remove(n)
                    remove.add(n)

        return max(number) if number else -1


if __name__ == "__main__":
    # 8
    print(Solution().largestUniqueNumber([5, 7, 3, 9, 4, 9, 8, 3, 1]))

    # -1
    print(Solution().largestUniqueNumber([9, 9, 8, 8]))
