from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = [first]
        for n in encoded:
            ans.append(ans[-1] ^ n)
        return ans


if __name__ == "__main__":
    print(Solution().decode(encoded=[1, 2, 3], first=1))  # [1,0,2,1]
    print(Solution().decode(encoded=[6, 2, 7, 3], first=4))  # [4,2,0,7,4]
