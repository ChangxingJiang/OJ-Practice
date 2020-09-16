class Solution:
    def queryString(self, S: str, N: int) -> bool:
        # 先将二进制转换为数字，去除不可能的N
        if int(S, base=2) < N:
            return False

        # 暴力解法
        for i in range(N, 0, -1):
            if str(bin(i))[2:] not in S:
                return False

        return True


if __name__ == "__main__":
    print(Solution().queryString(S="0110", N=3))  # True
    print(Solution().queryString(S="0110", N=4))  # False
