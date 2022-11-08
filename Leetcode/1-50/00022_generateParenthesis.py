"""
Description:
Author:qxy
Date: 2019-06-03 22:41
File: 00022_generateParenthesis 
"""

"""
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

"""
"""
暂时不会

"""

def generateParenthesis(n: int):
    resull_list = []
    symbol = '()'
    dd = ''

    for i in range(n):
        print(len(dd))
        for m in range(len(dd)):
            mm = dd[:m] + symbol + dd[m:]
            resull_list.append(mm)
        dd += '()'

    return resull_list


print(generateParenthesis(4))