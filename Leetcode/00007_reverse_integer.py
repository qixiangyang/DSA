"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
"""

# 自己的写法
def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    if x < -2 ** 31 or x > 2 ** 31 - 1:
        return 0

    if x == 0:
        return x

    if x > 0:
        x = list(str(x))
        z = x[::-1]
        reversed_x = int(''.join(z))
        return reversed_x

    if x < 0:
        x = -x
        x = list(str(x))
        z = x[::-1]
        reversed_x = int(''.join(z))
        return -reversed_x


# 别人的写法
def reverse1(x: int) -> int:
    flag = -1 if x < 0 else 1
    res = flag * int(str(abs(x))[::-1])
    return res if (-2 ** 31) <= res <= (2 ** 31 - 1) else 0