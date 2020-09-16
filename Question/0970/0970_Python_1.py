from typing import List


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        ans = set()
        for i in range(20):
            pi = pow(x, i)
            if pi > bound:
                break
            for j in range(20):
                pj = pow(y, j)
                if pj > bound:
                    break
                t = pi + pj
                if t > bound:
                    break
                ans.add(t)

        return list(ans)


if __name__ == "__main__":
    print(Solution().powerfulIntegers(2, 3, 10))  # [2,3,4,5,7,9,10]
    print(Solution().powerfulIntegers(3, 5, 15))  # [2,4,6,8,10,14]
