"""
Description:
Author:qxy
Date: 2019-06-04 15:41
File: 00005_longestPalindrome 
"""

"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
"""


def longestPalindrome(s: str) -> str:

    if s == '':
        return ''

    def is_Palindrom(temp):

        lenth = len(temp)
        k = 0
        for index, value in enumerate(temp):
            if temp[index] == temp[-index-1]:
                k += 1
        if lenth == k:
            return True
        else:
            return False

    def find_str(s):
        character_dict = {}
        len_dict = {}
        for i, info in enumerate(list(s)):

            if info in character_dict:
                temp_str = s[character_dict[info]: i+1]
                length = i - character_dict[info]
                len_dict[temp_str] = length

            character_dict[info] = i

        return sorted(len_dict.items(), key=lambda d: d[1], reverse=True)

    str_list = find_str(s)
    print(str_list)
    if len(str_list) == 0:
        return s[0]

    else:
        for str_info in str_list:
            data = is_Palindrom(str_info[0])
            if data is True:
                return str_info[0]


print(longestPalindrome('ccc'))