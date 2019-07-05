"""
Description:
Author:qxy
Date: 2019-06-10 16:34
File: 00205_isomorphic_strings 
"""

"""
给定两个字符串 s 和 t，判断它们是否是同构的。

如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。

所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。

示例 1:

输入: s = "egg", t = "add"
输出: true
示例 2:

输入: s = "foo", t = "bar"
输出: false
示例 3:

输入: s = "paper", t = "title"
输出: true
说明:
你可以假设 s 和 t 具有相同的长度。

"""


def isIsomorphic(s: str, t: str) -> bool:



    # t_dict = {}
    # t_index = 0
    # t_list = []
    #
    # for alphabet in set(t):
    #     t_dict[alphabet] = []
    #
    # for i in t:
    #     t_dict[i].append(t_index)
    #     t_index += 1
    #
    # for m in t_dict.values():
    #     t_list.append(m)
    #
    #
    # s_dict = {}
    # s_index = 0
    # s_list = []
    #
    # for alphabet in set(s):
    #     s_dict[alphabet] = []
    #
    # for i in s:
    #     s_dict[i].append(s_index)
    #     s_index += 1
    #
    # for m in s_dict.values():
    #     s_list.append(m)
    #
    #
    # print(t_list, s_list)
    # if str(t_list) == str(s_list):
    #     return True
    # else:
    #     return False

    # t_list = []
    #
    # for i in t:
    #     temp_tlist = []
    #     t_index = 0
    #     for m in t:
    #         if i == m:
    #             temp_tlist.append(t_index)
    #         t_index += 1
    #     t_list.append(temp_tlist)
    #
    # s_list = []
    #
    # for i in s:
    #     temp_slist = []
    #     s_index = 0
    #     for m in s:
    #         if i == m:
    #             temp_slist.append(s_index)
    #         s_index += 1
    #     s_list.append(temp_slist)
    #
    # if str(t_list) == str(s_list):
    #     return True
    # else:
    #     return False


print(isIsomorphic(s="foo", t="bar"))



"""
执行用时 :56 ms, 在所有Python3提交中击败了94.83% 的用户。 内存消耗 :13.2 MB, 在所有Python3提交中击败了87.09%的用户。 哈希表的知识，注意特殊情况

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = {}
        for i, char in enumerate(s):
            if char not in dic:
                if t[i] in dic.values():  # 特殊情况，比如s='ab',t='aa'
                    return False
                else:
                    dic[char] = t[i]
            else:
                if t[i] != dic[char]:
                    return False
        
        return True
"""