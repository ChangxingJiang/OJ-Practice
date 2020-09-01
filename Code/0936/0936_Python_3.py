from typing import List


class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        M, N = len(stamp), len(target)
        NN, MM = "#" * N, "#" * M

        # 判断字符串是否符合目标
        def match(s):
            for m in range(M):
                ch = s[m]
                if ch != "#" and ch != stamp[m]:
                    return False
            return True

        ans = []

        # 逆推法匹配结果
        while target != NN:
            find = False
            for i in range(N - M + 1):
                tmp = target[i:i + M]
                if tmp == MM:
                    continue
                if match(tmp):
                    find = True
                    ans.append(i)
                    target = target[:i] + MM + target[i + M:]
            if not find:
                return []

        return list(reversed(ans))


if __name__ == "__main__":
    print(Solution().movesToStamp(stamp="abc", target="ababc"))  # [0,2]
    print(Solution().movesToStamp(stamp="abca", target="aabcaca"))  # [3,0,1]
    print(Solution().movesToStamp(stamp="zbs", target="zbzbsbszbssbzbszbsss"))  # [11,9,17,10,6,5,3,1,16,14,13,8,4,0,15,12,7,2]
