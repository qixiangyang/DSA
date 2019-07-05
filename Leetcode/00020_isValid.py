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

输入："(([]){})"
输出：false

'(())[()]'
"[({}[])]"
"""


def isValid(s: str) -> bool:

    symbol_dict = {')': "(", "}": "{", "]": "["}
    special_symbol = [')', "}", "]"]

    symbol_list = []

    for symbol in s:
        if symbol in special_symbol:
            symbol_list.append(symbol)

    print(symbol_list)

    for i in symbol_list:
        i_index = s.index(i)

        if s[i_index-1] != symbol_dict[i]:
            return False
        else:
            s_list = list(s)
            s_list.pop(i_index)
            s_list.pop(i_index - 1)

            s = ''.join(s_list)

            print(s)

    if len(s) > 0:
        return False
    else:
        return True


print(isValid('(([]){})'))


"""
网友解法
class Solution:
    def isValid(self, s):
        while '{}' in s or '()' in s or '[]' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ''
"""



