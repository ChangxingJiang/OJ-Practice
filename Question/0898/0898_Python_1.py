from typing import List


class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        ans = set()
        now = {0}
        for x in A:
            now = {x | y for y in now} | {x}
            ans |= now
        return len(ans)


if __name__ == "__main__":
    print(Solution().subarrayBitwiseORs([0]))  # 1
    print(Solution().subarrayBitwiseORs([1, 1, 2]))  # 3
    print(Solution().subarrayBitwiseORs([1, 2, 4]))  # 6
