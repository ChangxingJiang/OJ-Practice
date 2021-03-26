from typing import List


class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        removing = False  # 是否在被多行屏蔽的情况下
        ans = []
        idx = 0
        in_line = False
        while idx < len(source):
            line = source[idx]  # 读取当前行信息
            if removing:
                if "*/" in line:
                    removing = False
                    source[idx] = line[line.index("*/") + 2:]
                else:
                    idx += 1
            else:
                N = len(line)
                idx_1 = line.index("//") if "//" in line else N
                idx_2 = line.index("/*") if "/*" in line else N
                if idx_1 < idx_2 and "//" in line:
                    if in_line and ans:
                        content = ans.pop() + line[:line.index("//")]
                        in_line = False
                    else:
                        content = line[:line.index("//")]
                    if content:
                        ans.append(content)
                    idx += 1
                elif idx_1 > idx_2:
                    if in_line and ans:
                        ans.append(ans.pop() + line[:line.index("/*")])
                    else:
                        ans.append(line[:line.index("/*")])
                    source[idx] = line[line.index("/*") + 2:]
                    removing = True
                    in_line = True
                else:
                    if in_line and ans:
                        content = ans.pop() + line
                        in_line = False
                    else:
                        content = line
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
