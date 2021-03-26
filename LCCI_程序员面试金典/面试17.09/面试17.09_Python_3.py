class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        lst = [0] * k
        lst[0] = 1
        p3 = p5 = p7 = 0  # *3、*5、*7分别乘过的坐标
        for i in range(1, k):
            lst[i] = (min(lst[p3] * 3, lst[p5] * 5, lst[p7] * 7))

            # 通过分别比较3个数实现去重（如果同时是两个的倍数，两个数乘到的位置均加1）
            if lst[i] == lst[p3] * 3:
                p3 += 1
            if lst[i] == lst[p5] * 5:
                p5 += 1
            if lst[i] == lst[p7] * 7:
                p7 += 1

        return lst[k - 1]


if __name__ == "__main__":
    print(Solution().getKthMagicNumber(5))  # 9
    print(Solution().getKthMagicNumber(7))  # 21
