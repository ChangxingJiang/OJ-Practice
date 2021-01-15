from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return [int(i) for i in sorted(str(i) for i in range(1, n + 1))]


if __name__ == "__main__":
    # [1,10,11,12,13,2,3,4,5,6,7,8,9]
    print(Solution().lexicalOrder(13))
