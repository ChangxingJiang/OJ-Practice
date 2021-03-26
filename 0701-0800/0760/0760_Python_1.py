from typing import List


class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        count = {}
        for i, n in enumerate(B):
            count[n] = i

        return [count[n] for n in A]


if __name__ == "__main__":
    # [1, 4, 3, 2, 0]
    print(Solution().anagramMappings(A=[12, 28, 46, 32, 50],
                                     B=[50, 12, 32, 46, 28]))
