class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        size1, size2 = len(pattern), len(value)

        # 处理value为空的特殊情况
        if size2 == 0:
            return size1 == 1

        for i1 in range(size2 + 1):
            p1, s1 = pattern[0], value[:i1]  # 模式值、对应的字符串值
            j1 = 1  # 当前模式中的位置
            i2 = i1  # 当前字符串中的位置

            # 连续匹配当前值
            right = True
            while j1 < size1 and i2 < size2 and pattern[j1] == p1:
                if value[i2:i2 + i1] == s1:
                    j1 += 1
                    i2 += i1
                else:
                    right = False
                    break

            # 处理已经匹配完成的情况
            if j1 >= size1 or i2 >= size2:
                if p1 not in pattern[j1:] and i2 == size2 and right:
                    return True
                else:
                    continue

            # 未能匹配则跳过
            if not right:
                continue

            for i3 in range(i2 + 1, size2 + 1):
                p2, s2 = pattern[j1], value[i2:i3]

                j2 = j1 + 1
                i4 = i3
                # 检查当前情况是否正确
                right = True
                while j2 < size1 and i4 <= size2:
                    if pattern[j2] == p1:
                        if i1 > 0:
                            if value[i4:i4 + i1] == s1:
                                j2 += 1
                                i4 += i1
                            else:
                                right = False
                                break
                        else:
                            j2 += 1
                    else:
                        if i3 - i2 > 0:
                            if value[i4:i4 + (i3 - i2)] == s2:
                                j2 += 1
                                i4 += (i3 - i2)
                            else:
                                right = False
                                break
                        else:
                            j2 += 1

                # print(right, "第1个:", s1, "第2个:", s2, "(", j2, "/", size1, ")", "(", i4, "/", size2, ")")

                # 如果匹配成功则返回
                if right and j2 == size1 and i4 == size2:
                    return True

        return False


if __name__ == "__main__":
    print(Solution().patternMatching(pattern="abba", value="dogcatcatdog"))  # True
    print(Solution().patternMatching(pattern="abba", value="dogcatcatfish"))  # False
    print(Solution().patternMatching(pattern="aaaa", value="dogcatcatdog"))  # False
    print(Solution().patternMatching(pattern="abba", value="dogdogdogdog"))  # True
    print(Solution().patternMatching(pattern="bbba", value="xxxxxx"))  # True
    print(Solution().patternMatching(pattern="bbb", value="xxxxxx"))  # True
    print(Solution().patternMatching(pattern="bbba", value="xxxxxxy"))  # True

    # True
    print(Solution().patternMatching(pattern="bbbbbbbbbbbbbbabbbbb",
                                     value="ppppppppppppppjsftcleifftfthiehjiheyqkhjfkyfckbtwbelfcgihlrfkrwireflijkjyppppg"))
