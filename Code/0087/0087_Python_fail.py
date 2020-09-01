class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        # 将s1转换为坐标列表字典
        count = {}
        for i, ch in enumerate(s1):
            if ch not in count:
                count[ch] = [i]
            else:
                count[ch].append(i)

        # 排序列表字典
        for key in count:
            count[key].sort()

        print(count)

        # 使用栈存储当前已经凝聚的节点
        stack = []
        for ch in s2:
            if ch not in count or len(count[ch]) == 0:  # 处理s1中字符数小于s2中字符数的情况
                return False
            idx = count[ch].pop(0)
            if not stack:  # 处理s2中第一个元素的情况
                stack.append((idx, idx))
            else:  # 处理不是s2中第一个元素的情况
                if idx == stack[-1][0] - 1:
                    stack[-1] = (idx, stack[-1][1])
                elif idx == stack[-1][1] + 1:
                    stack[-1] = (stack[-1][0], idx)
                else:
                    stack.append((idx, idx))

            print(ch, "[", idx, "]", "->", stack)

        return len(stack) == 1

if __name__ == "__main__":
    print(Solution().isScramble(s1="great", s2="rgeat"))  # True
    print(Solution().isScramble(s1="abcde", s2="caebd"))  # False
    print(Solution().isScramble(s1="greet", s2="egtre"))  # False
    print(Solution().isScramble(s1="geeet", s2="egtee"))  # True
    print(Solution().isScramble(s1="abcde", s2="baced"))  # True
    print(Solution().isScramble(s1="123456789", s2="215349867"))  # True
    print(Solution().isScramble(s1="ab", s2="aa"))  # False
    print(Solution().isScramble(s1="abb", s2="bba"))  # True
