class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        # 处理密码为空的情况
        if not password:
            return 6

        size = len(password)

        # 统计密码中是否存在小写、大写和数字
        lower = any(ch.islower() for ch in password)
        upper = any(ch.isupper() for ch in password)
        number = any(ch.isnumeric() for ch in password)

        # 计算缺失字符的最小修改数量（补齐小写、大写和数字）
        need1 = 3 - (lower + upper + number)

        # 统计所有连续超过3个的字符的位置
        continuities = {}
        i = 0
        while i < size:
            now = 1
            while i + 1 < size and password[i] == password[i + 1]:
                now += 1
                i += 1
            if now >= 3:
                continuities[i] = now
            i += 1

        # 处理密码长度小于6的情况
        if size < 6:
            return max(6 - size, need1)

        # 处理密码长度大于等于6且小于等于20的情况
        elif size <= 20:
            need2 = sum(n // 3 for n in continuities.values())  # 计算处理连续字符的最小修改数
            return max(need1, need2)

        # 处理密码长度大于20的情况
        else:
            m0, m1, m2 = {}, {}, {}
            ans = need1
            for i in continuities:
                if continuities[i] % 3 == 2:
                    m2[i] = continuities[i]
                elif continuities[i] % 3 == 1:
                    m1[i] = continuities[i]
                else:
                    m0[i] = continuities[i]

            for i in m2:  # 先转换 %3==2的
                while m2[i] >= 3 and need1 > 0:  # 转换一次减少3个连续值
                    need1 -= 1
                    m2[i] -= 3
                if need1 == 0:
                    break
            for i in m1:  # 再转换 %3==1的
                while m1[i] >= 3 and need1 > 0:
                    need1 -= 1
                    m1[i] -= 3
                if need1 == 0:
                    break
            for i in m0:  # 最后转换 %3==0的
                while m0[i] >= 3 and need1 > 0:
                    need1 -= 1
                    m0[i] -= 3
                if need1 == 0:
                    break
            if need1 > 0:  # 转换完后x仍然大于0，说明连续的用光了，随便找一数转换为缺失数种类，再删掉多余的数即可，
                return ans + (size - 20)

            # 缺失值补充完后仍有连续值，则先删 m0,再删m1,最后删m2
            while m0 or m1 or m2:
                k0 = list(m0.keys())
                for i in k0:
                    a = m0.pop(i)  # 删掉i
                    if a >= 3:
                        size -= 1
                        ans += 1
                        m2[i] = a - 1  # 余数变为2
                    if size == 20:
                        break

                if size > 20:  # n>20说明删m0不够
                    k1 = list(m1.keys())
                    for i in k1:  # 再删m1
                        a = m1.pop(i)
                        if a >= 3:
                            size -= 2
                            ans += 2
                            m2[i] = a - 2  # 每次删2个，余数变为2
                        if size == 20:
                            break
                        if size == 19:  # 剩19个说明多删了，只需要删1个，省下连续的后面再处理
                            size += 1
                            ans -= 1
                            m0[i] = a - 1  # 删2个变为删1个
                            m2.pop(i)  # 删去刚刚增加的m2的值
                            break

                if size > 20:  # 删m1没结束
                    k2 = list(m2.keys())
                    for i in k2:  # 最后删m2
                        a = m2.pop(i)
                        if a >= 3:
                            size -= 3
                            ans += 3
                            m2[i] = a - 3
                        if size == 20:
                            break
                        elif size == 19:  # 假如剩下22个，删3个变为删2个
                            size += 1
                            ans -= 1
                            m0[i] = a - 2
                            m2.pop(i)
                            break
                        elif size == 18:  # 剩下21个，删3个变为删1个
                            size += 2
                            ans -= 2
                            m1[i] = a - 1
                            m2.pop(i)
                            break
                if size <= 20:  # 删除到固定长度
                    break

            if size > 20:  # 连续的用完了，删去多余的值即可
                return ans + size - 20
            for i in m2:  # 还有连续的，则检查连续值，依次替换得结果
                ans += m2[i] // 3
            for i in m1:
                ans += m1[i] // 3
            for i in m0:
                ans += m0[i] // 3
            return ans


if __name__ == "__main__":
    print(Solution().strongPasswordChecker("ABABABABABABABABABAB1"))  # 2
    print(Solution().strongPasswordChecker("bbaaaaaaaaaaaaaaacccccc"))  # 8
