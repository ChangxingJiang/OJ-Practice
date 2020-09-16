from typing import List


class Solution:
    def ambiguousCoordinates(self, S: str) -> List[str]:
        # 转换为小数格式（如无法转换则返回None）
        def change_to_num(n1, n2):
            if int(n1) > 0 and n1[0] == "0":
                return None
            if int(n1) == 0 and len(n1) > 1:
                return None
            if n2 and (int(n2) == 0 or n2[-1] == "0"):
                return None
            if not n2:
                return n1
            else:
                return n1 + "." + n2

        S = S[1:-1]

        ans = []

        for i in range(1, len(S)):
            a = S[:i]
            b = S[i:]
            for j in range(1, len(a) + 1):
                aa = change_to_num(a[:j], a[j:])
                if aa:
                    for k in range(1, len(b) + 1):
                        bb = change_to_num(b[:k], b[k:])
                        if bb:
                            ans.append("(" + aa + ", " + bb + ")")
        return ans


if __name__ == "__main__":
    print(Solution().ambiguousCoordinates("(123)"))  # ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]
    print(Solution().ambiguousCoordinates("(00011)"))  # ["(0.001, 1)", "(0, 0.011)"]
    print(Solution().ambiguousCoordinates("(0123)"))  # ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"]
    print(Solution().ambiguousCoordinates("(100)"))  # [(10, 0)]
