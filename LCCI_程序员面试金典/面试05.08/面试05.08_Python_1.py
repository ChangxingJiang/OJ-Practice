from typing import List


class Solution:
    def drawLine(self, length: int, w: int, x1: int, x2: int, y: int) -> List[int]:
        height = length * 32 // w
        width = w // 32
        # print("高度:", height)

        ans = []

        for i in range(height):
            if i == y:
                line = []

                total = (2 ** (x2 - x1 + 1) - 1) << (w - x2 - 1)

                for _ in range(width):
                    # print(bin(total))
                    # 处理正数的情况
                    if not (total >> 31) & 1:
                        # print("处理正数:", total & ((1 << 31) - 1))
                        line.append(total & ((1 << 31) - 1))
                    # 处理负数的情况
                    else:
                        # print("处理负数:", total & ((1 << 31) - 1), (1 << 31))
                        line.append((total & ((1 << 31) - 1)) - (1 << 31))
                    total >>= 32
                ans += line[::-1]

            else:
                ans += [0] * width

        return ans


if __name__ == "__main__":
    # [3]
    print(Solution().drawLine(length=1, w=32, x1=30, x2=31, y=0))

    # [-1,-1,-1]
    print(Solution().drawLine(length=3, w=96, x1=0, x2=95, y=0))

    # [0,0,0,0,0,32767,0,0,0,0,0,0,0,0,0]
    print(Solution().drawLine(length=15, w=96, x1=81, x2=95, y=1))
