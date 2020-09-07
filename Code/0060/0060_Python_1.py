import math


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        lst = [str(i) for i in range(1, n + 1)]

        def build(nn, kk):
            # 处理已经完成递归的情况
            if nn == 1:
                return [lst.pop()]

            # 处理当前最靠前的一位
            num = math.factorial(nn - 1)  # 第一位每变化一次需要的序列数
            idx = kk // num  # 第一位的数值坐标
            return [lst.pop(idx)] + build(nn - 1, kk % num)

        return "".join(build(n, k - 1))


if __name__ == "__main__":
    print(Solution().getPermutation(3, 3))  # "213"
    print(Solution().getPermutation(3, 1))  # "123"
    print(Solution().getPermutation(3, 5))  # "312"
    print(Solution().getPermutation(3, 6))  # "321"
    print(Solution().getPermutation(4, 9))  # "2314"
