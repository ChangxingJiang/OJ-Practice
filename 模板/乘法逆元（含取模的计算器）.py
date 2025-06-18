"""
包含取模的计算器

原理参考文档：
https://leetcode.cn/discuss/post/3584387/fen-xiang-gun-mo-yun-suan-de-shi-jie-dan-7xgu/
"""


class ModularComputer:
    """包含取模的计算器，支持四则运算、阶乘、排列数和组合数计算（阶乘计算时会自动进行缓存）"""

    def __init__(self, mod=10 ** 9 + 7) -> None:
        self._mod = mod
        self._factorial = [1]  # 阶乘结果的缓存器：self._factorial[i] 表示 i 的阶乘

    def plus(self, a: int, b: int) -> int:
        """加法运算：(a + b) MOD m = ( (a MOD m) + (b MOD m) ) MOD m"""
        return ((a % self._mod) + (b % self._mod)) % self._mod

    def multiple(self, a: int, b: int) -> int:
        """乘法运算：(a * b) MOD m = ( (a MOD m) ⋅* (b MOD m)) MOD m"""
        return ((a % self._mod) * (b % self._mod)) % self._mod

    def sub(self, a: int, b: int) -> int:
        """减法运算：(a − b) MOD m = ( (a MOD m) − (b MOD m) + m) MOD m"""
        return (a - b) % self._mod

    def divide(self, a: int, b: int) -> int:
        """除法运算：(a / b) MOD m = (a * (b ** (p - 2))) % MOD m"""
        return self.multiple(a, pow(b, self._mod - 2, self._mod))

    def factorial(self, n: int) -> int:
        """阶乘计算：(n!) MOD m"""
        if n > len(self._factorial):
            for i in range(len(self._factorial), n + 1):
                self._factorial.append(self.multiple(self._factorial[-1], i))
        return self._factorial[n]

    def arrange(self, n: int, m: int) -> int:
        """排列数计算：A_n^m = n! / (n - m)!"""
        return self.divide(self.factorial(n), self.factorial(n - m))

    def combine(self, n: int, m: int) -> int:
        """组合数计算：C_n^m = ( n! / (n - m)! ) / m!"""
        return self.divide(self.arrange(n, m), self.factorial(m))


if __name__ == "__main__":
    computer = ModularComputer()
    print(computer.combine(4, 2))  # 6
    print(computer.combine(6, 2))  # 15
    print(computer.combine(100, 50))  # 538992043
