"""
Description:
Author:qxy
Date: 2019-06-09 15:11
File: 00066_plus_one 
"""


"""
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/plus-one
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


def plusOne(digits):

    data_len = len(digits)
    num = 0

    for i in range(data_len):
        num += digits[i] * pow(10, data_len-i-1)

    num += 1

    result_list = []
    now_len = len(str(num))
    for i in range(now_len):
        m = int(num / pow(10, now_len-i-1))
        result_list.append(m)
        num = num % pow(10, now_len-i-1)

    return result_list


print(plusOne([9]))
