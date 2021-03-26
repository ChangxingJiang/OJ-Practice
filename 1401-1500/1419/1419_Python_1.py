class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        ans = 0
        a, b, c, d = 0, 0, 0, 0  # 四个叫声状态的数量
        for ch in croakOfFrogs:
            # 计算当前叫声状态
            if ch == "c":
                a += 1
                total = a + b + c + d
                if total > ans:
                    ans = total
            elif ch == "r":
                a -= 1
                b += 1
                if a < 0:
                    return -1
            elif ch == "o":
                b -= 1
                c += 1
                if b < 0:
                    return -1
            elif ch == "a":
                c -= 1
                d += 1
                if c < 0:
                    return -1
            else:
                d -= 1
                if d < 0:
                    return -1

        # 判断所有叫声是否结束
        if a != 0 or b != 0 or c != 0 or d != 0:
            return -1
        else:
            return ans


if __name__ == "__main__":
    print(Solution().minNumberOfFrogs(croakOfFrogs="croakcroak"))  # 1
    print(Solution().minNumberOfFrogs(croakOfFrogs="crcoakroak"))  # 2
    print(Solution().minNumberOfFrogs(croakOfFrogs="croakcrook"))  # -1
    print(Solution().minNumberOfFrogs(croakOfFrogs="croakcroa"))  # -1
