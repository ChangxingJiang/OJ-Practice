import math


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        lst = [str(i) for i in range(1, n + 1)]
        ans = []
        k -= 1

        while n > 1:
            num = math.factorial(n - 1)
            idx = k // num  # 第一位的数值坐标
            ans.append(lst.pop(idx))
            n -= 1
            k %= num
        ans.append(lst.pop())

        return "".join(ans)


if __name__ == "__main__":
    print(Solution().getPermutation(3, 3))  # "213"
    print(Solution().getPermutation(3, 1))  # "123"
    print(Solution().getPermutation(3, 5))  # "312"
    print(Solution().getPermutation(3, 6))  # "321"
    print(Solution().getPermutation(4, 9))  # "2314"
