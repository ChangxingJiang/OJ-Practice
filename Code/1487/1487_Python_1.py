from typing import List


class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        name_set = set()
        ans = []
        for name in names:
            # 处理还没有重名的情况
            if name not in name_set:
                name_set.add(name)
                ans.append(name)

            # 处理出现重名的情况
            else:
                # 计算当前文件夹名的名称部分和计数部分
                word = name
                num = 1

                # 调整当前文件夹名的数量至没有重名
                while word + "(" + str(num) + ")" in name_set:
                    num += 1
                new_name = word + "(" + str(num) + ")"
                name_set.add(new_name)
                ans.append(new_name)
        return ans


if __name__ == "__main__":
    # ["pes","fifa","gta","pes(2019)"]
    print(Solution().getFolderNames(names=["pes", "fifa", "gta", "pes(2019)"]))

    # ["pes","fifa","gta","pes(2019)","pes(1)"]
    print(Solution().getFolderNames(names=["pes", "fifa", "gta", "pes(2019)", "pes"]))

    # ["gta","gta(1)","gta(2)","avalon"]
    print(Solution().getFolderNames(names=["gta", "gta(1)", "gta", "avalon"]))

    # ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece(4)"]
    print(Solution().getFolderNames(names=["onepiece", "onepiece(1)", "onepiece(2)", "onepiece(3)", "onepiece"]))

    # ["kaido","kaido(1)","kaido(2)","kaido(1)(1)"]
    print(Solution().getFolderNames(names=["kaido", "kaido(1)", "kaido", "kaido(1)"]))
