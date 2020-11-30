import collections


class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        size1, size2 = len(pattern), len(value)

        # 处理value为空的特殊情况
        if size2 == 0:
            return size1 == 1

        count = collections.Counter(pattern)
        count1, count2 = count["a"], count["b"]

        # 如果有一个模式的出现频数为1，则令该模式为整串即可
        if count1 == 1 or count2 == 1:
            return True

        # 处理只出现一种模式的情况
        if count1 == 0 or count2 == 0:
            if size2 % (count1 + count2) != 0:
                return False
            p = size2 // (count1 + count2)
            for l in range(0, size2 - p, p):
                if value[l:l + p] != value[l + p:l + 2 * p]:
                    return False
            return True

        # 处理两种模式均有出现的情况
        for l1 in range(size2 // count1 + 1):
            if (size2 - count1 * l1) % count2 != 0:
                continue
            l2 = (size2 - count1 * l1) // count2
            a, b = "", ""
            j1, j2 = 0, 0
            while j1 < size1 and j2 < size2:
                if pattern[j1] == "a":
                    if j2 + l1 > size2:
                        break
                    ch = value[j2:j2 + l1]
                    j2 += l1
                    if a == "":
                        a = ch
                    else:
                        if a != ch:
                            break
                else:
                    if j2 + l2 > size2:
                        break
                    ch = value[j2:j2 + l2]
                    j2 += l2
                    if b == "":
                        b = ch
                    else:
                        if b != ch:
                            break
                j1 += 1
            else:
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
