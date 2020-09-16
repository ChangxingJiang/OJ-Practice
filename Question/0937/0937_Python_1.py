from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def info(lg):
            idx = lg.index(" ")
            return lg[idx + 1:] + lg[:idx]

        d_logs = []  # 数字日志
        a_logs = []  # 字母日志
        for log in logs:
            if log[log.index(" ") + 1].isalpha():
                a_logs.append(log)
            else:
                d_logs.append(log)

        a_logs.sort(key=info)

        return a_logs + d_logs


if __name__ == "__main__":
    print(Solution().reorderLogFiles(["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]))
    # ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
