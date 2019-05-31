"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true
"""

def isValid(s: str) -> bool:

    symbol_dict = {"(": ")", "{": "}", "[": "]"}

    while len(s) > 0:

        if s[0] in symbol_dict:
            value = symbol_dict[s[0]]
            try:
                index = s.index(value)
            except Exception as e:
                # print(e)
                return False

            if (index-1) % 2 != 0:
                return False

            else:
                m = list(s)
                m.pop(index)
                m.pop(0)

                s = ''.join(m)

                if len(s) == 0:
                    return True
        else:
            return False
    else:
        return True


print(isValid("(([]){})"))



