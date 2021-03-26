import re


class Solution:
    def isValid(self, code: str) -> bool:
        # 正则表达式判断是否被一个标签包含
        if not re.match(r"^<([A-Z]{1,9})>.*</\1>$", code, re.S):
            return False

        # 正则表达式移除CDATA
        code = re.sub(r'<!\[CDATA\[.*?\]\]>', "", code)

        # 使用正则式移除所有最内层标签
        code, num = re.subn(r"<([A-Z]{1,9})>[^<]*</\1>", "", code)
        while num:
            code, num = re.subn(r"<([A-Z]{1,9})>[^<]*</\1>", "", code)
        return not code


if __name__ == "__main__":
    print(Solution().isValid("<DIV>This is the first line <![CDATA[<div>]]></DIV>"))  # True
    print(Solution().isValid("<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>"))  # True
    print(Solution().isValid("<A>  <B> </A>   </B>"))  # False
    print(Solution().isValid("<DIV>  div tag is not closed  <DIV>"))  # False
    print(Solution().isValid("<DIV>  unmatched <  </DIV>"))  # False
    print(Solution().isValid("<DIV> closed tags with invalid tag name  <b>123</b> </DIV>"))  # False
    print(Solution().isValid("<DIV> closed tags with invalid tag name  <B>123</B> </DIV>"))  # True
    print(Solution().isValid(
        "<DIV> unmatched tags with invalid tag name  </1234567890> and <CDATA[[]]>  </DIV>"))  # False
    print(Solution().isValid("<DIV>  unmatched start tag <B>  and unmatched end tag </C>  </DIV>"))  # False
    print(Solution().isValid("<![CDATA[wahaha]]]><![CDATA[]> wahaha]]>"))  # False
    print(Solution().isValid("<A></A><B></B>"))  # False
    print(Solution().isValid("<![CDATA[ABC]]><TAG>sometext</TAG>"))  # False
    print(Solution().isValid(
        "<DIV>This is the first line <![CDATA[<div> <![cdata]> [[]]</div>   ]]>  <DIV> <A>  <![CDATA[<b>]]>  </A>  <A> <C></C></A></DIV>    </DIV>"))  # True
