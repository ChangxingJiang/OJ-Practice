from typing import List


class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        is_block = False  # 是否在被多行屏蔽的情况下
        in_line = False  # 当前是否换行

        ans = []

        idx = 0
        while idx < len(source):
            line = source[idx]  # 读取当前行信息

            if is_block:  # 处理当前正在多行屏蔽的情况下
                if "*/" in line:
                    is_block = False
                    source[idx] = line[line.index("*/") + 2:]
                else:
                    idx += 1
            else:
                content = ans.pop() if in_line and ans else ""  # 当前行结果

                idx_1 = line.index("//") if "//" in line else float("inf")
                idx_2 = line.index("/*") if "/*" in line else float("inf")

                if idx_1 < idx_2:
                    in_line = False
                    content += line[:line.index("//")]
                    if content:
                        ans.append(content)
                    idx += 1
                elif idx_1 > idx_2:
                    is_block, in_line = True, True
                    ans.append(content + line[:line.index("/*")])
                    source[idx] = line[line.index("/*") + 2:]
                else:
                    in_line = False
                    content += line
                    if content:
                        ans.append(content)
                    idx += 1
        return ans


if __name__ == "__main__":
    # ["int main()","{ ","  ","int a, b, c;","a = b + c;","}"]
    print(Solution().removeComments(
        source=["/*Test program */",
                "int main()",
                "{ ",
                "  // variable declaration ",
                "int a, b, c;",
                "/* This is a test",
                "   multiline  ",
                "   comment for ",
                "   testing */",
                "a = b + c;", "}"]))

    # ["ab"]
    print(Solution().removeComments(source=["a/*comment", "line", "more_comment*/b"]))

    # ["struct Node{","    ","    int size;","    int val;","};"]
    print(Solution().removeComments(source=["struct Node{", "    /*/ declare members;/**/", "    int size;", "    /**/int val;", "};"]))

    # ["void func(int k) {","   k = k*2/4;","   k = k/2;*/","}"]
    print(Solution().removeComments(source=["void func(int k) {", "// this function does nothing /*", "   k = k*2/4;", "   k = k/2;*/", "}"]))

    # ["a","blank","d/f"]
    print(Solution().removeComments(source=["a//*b//*c", "blank", "d/*/e*//f"]))

    # ["ae*"]
    print(Solution().removeComments(source=["a/*/b//*c", "blank", "d/*/e*//f"]))

    # ["class test{","public: ","   int x = 1;","   ","   char c;","};"]
    print(Solution().removeComments(source=["class test{", "public: ", "   int x = 1;", "   /*double y = 1;*/", "   char c;", "};"]))
