"""
Description:
Author:qxy
Date: 2019-06-15 10:56
File: 00118 
"""

"""
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""


def generate(numRows: int):
    if numRows == 1:
        return [1]
    elif numRows == 2:
        return [1, 1]
    else:
        for