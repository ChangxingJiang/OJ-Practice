from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0] * len(code)
        elif k > 0:
            res = []
            for i in range(len(code)):
                val = 0
                for j in range(i + 1, i + k + 1):
                    j %= len(code)
                    val += code[j]
                res.append(val)
            return res
        else:
            res = []
            for i in range(len(code)):
                val = 0
                for j in range(i + k, i):
                    j = (j + len(code)) % len(code)
                    val += code[j]
                res.append(val)
            return res


if __name__ == "__main__":
    print(Solution().decrypt(code=[5, 7, 1, 4], k=3))  # [12,10,16,13]
    print(Solution().decrypt(code=[1, 2, 3, 4], k=0))  # [0,0,0,0]
    print(Solution().decrypt(code=[2, 4, 9, 3], k=-2))  # [12,5,6,13]
