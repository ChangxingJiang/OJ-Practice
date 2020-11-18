from typing import List


class Solution:
    def findClosedNumbers(self, num: int) -> List[int]:
        # 计算更小的那个数
        i, n = 0, num
        a, b = -1, -1  # 准备移到的位，准备移走的位
        array = []  # 移走的位之后的位
        while n:
            if not n & 1:
                a = i
            if n & 1:
                if a == -1:
                    array.append(i)
                else:
                    b = i
                    break
            i += 1
            n >>= 1

        if a >= 0 and b >= 0:
            ans1 = num - (1 << b) + (1 << a)
            m = a - 1
            for n in array:
                ans1 -= (1 << n)
                ans1 += (1 << m)
                m -= 1
        else:
            ans1 = -1

        # print(a, b, array, "->", ans1)

        # 计算更大的那个数
        i, n = 0, num
        a, b = -1, -1  # 准备移走的位，准备移到的位
        array = []  # 移走的位之后的位
        while n:
            if n & 1:
                a = i
            if not n & 1:
                if a != -1:
                    b = i
                    break
                else:
                    array.append(i)
            i += 1
            n >>= 1
        if b == -1:
            b = i

        if a >= 0 and b >= 0:
            ans2 = num + (1 << b) - (1 << a)
            m = a - 1
            for n in array:
                ans2 += (1 << n)
                ans2 -= (1 << m)
                m -= 1
        else:
            ans2 = -1

        return [ans2, ans1]


if __name__ == "__main__":
    print(Solution().findClosedNumbers(2))  # [4,1]
    print(Solution().findClosedNumbers(1))  # [2,-1]
    print(Solution().findClosedNumbers(1837591841))  # [1837591842,1837591832]
    print(Solution().findClosedNumbers(571603719))  # [571603723,571603696]
    print(Solution().findClosedNumbers(1156403390))  # [1156403407,1156403389]
