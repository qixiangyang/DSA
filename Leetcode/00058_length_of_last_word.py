"""
Description:
Author:qxy
Date: 2019-06-09 14:07
File: 00058_length_of_last_word 
"""


"""
给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。

如果不存在最后一个单词，请返回 0 。

说明：一个单词是指由字母组成，但不包含任何空格的字符串。

示例:

输入: "Hello World"
输出: 5

"""


def lengthOfLastWord(s: str) -> int:

    if len(s) == 0:
        return 0

    word_list = s.split(' ')
    print(word_list)
    for word in word_list[::-1]:
        if len(word) != 0:
            return len(word)

    else:
        return 0


print(lengthOfLastWord(" "))