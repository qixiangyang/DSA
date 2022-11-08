"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。
"""


def longestCommonPrefix(strs) -> str:

    s = ""

    if len(strs) == 0:
        return s

    else:
        strs_len_list = [len(x) for x in strs]
        first_str_index = strs_len_list.index(min(strs_len_list))

        first_str = strs[first_str_index]
        first_str_len = len(first_str)

        ioc = []
        for i in range(first_str_len):
            for str in strs:
                # print(first_str[i], str[i])
                if first_str[i] != str[i]:
                    ioc.append(i)

        if len(ioc) == 0:
            return first_str
        elif ioc[0] == 0:
            return s
        else:
            s += first_str[0:ioc[0]]
            return s


print(longestCommonPrefix(["flower","flow","flight"]))