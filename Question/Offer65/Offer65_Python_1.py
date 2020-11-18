class Solution:
    def add(self, a: int, b: int) -> int:
        MOD = 0xffffffff
        a, b = a & MOD, b & MOD  # 获取负数补码
        while b:
            a, b = a ^ b, (a & b) << 1 & MOD  # 分别计算：不考虑进位情况下的和，进位值
        return a if a <= 0x7fffffff else ~(a ^ MOD)  # 将补码还原


if __name__ == "__main__":
    print(Solution().add(1, 1))  # 2
    print(Solution().add(5, 3))  # 8
    print(Solution().add(-1, 2))  # 1
