"""
Description:
Author:qxy
Date: 2019-06-15 11:38
File: 00242_valid_anagram 
"""

"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
说明:
你可以假设字符串只包含小写字母。

进阶:
如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
"""


def isAnagram(s: str, t: str) -> bool:

    if len(s) != len(t):
        return False

    s_set = set(s)
    s_dict = {x: 0 for x in s_set}
    for i in s:
        if i in s_dict:
            s_dict[i] += 1

    for i in s_set:
        t = t.replace(i, '', s_dict[i])

    if len(t) != 0:
        return False
    else:
        return True


print(isAnagram('ab', 'a'))


"""
执行用时 :64 ms, 在所有Python3提交中击败了91.50%的用户
内存消耗 :12.9 MB, 在所有Python3提交中击败了99.66%的用户
"""