"""
Description:
Author:qxy
Date: 2019-06-25 19:22
File: 00131_palindrome_partitioning 
"""

"""
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回 s 所有可能的分割方案。

示例:

输入: "aab"
输出:
[
  ["aa","b"],
  ["a","a","b"]
]

"""


from typing import List


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if len(s) == 0:
            return [[]]
        if len(s) == 1:
            return [[s]]
        res = []
        s_len = len(s)
        for i in range(1, s_len):
            left = s[:i]
            right = s[i:]
            if left == left[::-1]:
                m = self.partition(right)
                for b in m:
                    res.append([left] + b)
        return res


data = Solution()
print(data.partition('aab'))