import collections


class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        # 计算两个字符串的字符位置
        S = collections.defaultdict(list)
        for i, ch in enumerate(s):
            S[int(ch)].append(i)
        T = collections.defaultdict(list)
        for i, ch in enumerate(t):
            T[int(ch)].append(i)

        # 每次升序只能让小的向前移动，让大的向后移动；而不能让大的向后移动
        for n in range(10):  # 遍历10个字符
            # 如果字符数量不相等则直接报错
            if len(S[n]) != len(T[n]):
                return False

            # 检查是否可以通过排序生成
            last_idx1 = 0
            last_idx2 = 0
            total_num1 = 0
            total_num2 = 0
            for i in range(len(S[n])):
                idx1 = S[n][i]
                idx2 = T[n][i]
                total_num1 += sum([1 if int(s[j]) < n else 0 for j in range(last_idx1, idx1)])
                total_num2 += sum([1 if int(t[j]) < n else 0 for j in range(last_idx2, idx2)])
                if total_num1 > total_num2:
                    # print("错误原因:", n, S[n], T[n])
                    return False
                last_idx1, last_idx2 = idx1, idx2

        return True


if __name__ == "__main__":
    print(Solution().isTransformable(s="84532", t="34852"))  # True
    print(Solution().isTransformable(s="34521", t="23415"))  # True
    print(Solution().isTransformable(s="12345", t="12435"))  # False
    print(Solution().isTransformable(s="1", t="2"))  # False
    print(Solution().isTransformable(s="2032", t="0223"))  # True
