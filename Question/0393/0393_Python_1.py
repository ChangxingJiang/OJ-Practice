from typing import List


class Solution:
    def validUtf8(self, data: List[int], idx=0) -> bool:
        # 处理到达末尾的情况
        if idx == len(data):
            return True

        # 处理单字节的情况
        if data[idx] & (1 << 7) == 0:
            return self.validUtf8(data, idx + 1)

        # 处理10xxxxxx的错误情况
        if data[idx] & (1 << 6) == 0:
            return False

        # 处理n字节的情况
        for i in range(5, 2, -1):
            if data[idx] & (1 << i) == 0:
                length = 7 - i  # 计算UTF-8字节数
                if len(data) < idx + length:
                    return False
                for j in range(idx + 1, idx + length):
                    if data[j] & (1 << 7) == 0 or data[j] & (1 << 6) != 0:
                        return False
                return self.validUtf8(data, idx + length)

        return False


if __name__ == "__main__":
    print(Solution().validUtf8([197, 130, 1]))  # True
    print(Solution().validUtf8([235, 140, 4]))  # False
    print(Solution().validUtf8([237]))  # False
    print(Solution().validUtf8([250, 145, 145, 145, 145]))  # False
