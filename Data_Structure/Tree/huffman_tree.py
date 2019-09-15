"""
Description:
Author:qxy
Date: 2019-07-11 17:42
File: huffman_tree 
"""


class TreeNode(object):
    """
    1.树结点类的构建：
　　 共有5个属性：结点的值，结点的优先度，结点的左子结点，结点的右子结点，
    结点值的编码（这个没有什么好说的，这些属性都是被需要的）
    """
    def __init__(self, data):
        self.val = data[0]
        self.priority = data[1]
        self.leftChild = None
        self.rightChild = None
        self.code = ""


# 创建树节点队列函数
def creatnodeQ(codes):
    """
    2.创建树结点队列函数：
　　 对于所有的字母结点，我们将其组成一个队列，这里使用list列表来完成队列的功能。
    将所有树节点够放进列表中，当然传进来的是按优先度从小到大已排序的元素列表
    """
    q = []
    for code in codes:
        q.append(TreeNode(code))
    return q


# 为队列添加节点元素，并保证优先度从大到小排列
def addQ(queue, nodeNew):
    """
    3.为队列添加节点元素，并保证优先度从大到小排列：
　　 当有新生成的结点时，需将其插入列表，并放在合适位置，使队列依然时按优先度从小打到排列的。
    """
    if len(queue) == 0:
        return [nodeNew]
    for i in range(len(queue)):
        if queue[i].priority >= nodeNew.priority:
            return queue[:i] + [nodeNew] + queue[i:]
    return queue + [nodeNew]


# 节点队列类定义
class nodeQeuen(object):
    """
    4.结点队列类定义：
　　　　创建类初始化时需要传进去的是一个列表，列表中的每个元素是由字母与优先度组成的元组。元组第一个元素是字母，第二个元素是优先度（即在文本中出现的次数）

　　　　类初始化化时，调用“创建树结点队列函数”，队列中的每个元素都是一个树结点。

　　　　类中还包含一个队列规模属性以及另外两个操作函数：添加结点函数和弹出结点函数。

　　　　添加结点函数直接调用之前定义的函数即可，输入的参数为队列和新结点，并且队列规模加一

　　　　弹出第一个元素则直接调用列表的pop(0)函数，同时队列规模减一
    """
    def __init__(self, code):
        self.que = creatnodeQ(code)
        self.size = len(self.que)

    def addNode(self, node):
        self.que = addQ(self.que, node)
        self.size += 1

    def popNode(self):
        self.size -= 1
        return self.que.pop(0)


# 各个字符在字符串中出现的次数，即计算优先度
def freChar(string):

    """
    5.计算文本中个字母的优先度，即出现的次数：
　　 定义一个字典，遍历文本中的每一个字母，若字母不在字典里说明是第一次出现，则定义该字母为键，另键值为1，
    若在字典里有，则只需将相应的键值加一。 遍历后就得到了每个字母出现的次数。
    """
    d ={}
    for c in string:
        if not c in d:
            d[c] = 1
        else:
            d[c] += 1
    return sorted(d.items(),key=lambda x: x[1])


# 创建哈夫曼树
def creatHuffmanTree(nodeQ):

    """
    6.由哈夫曼树得到编码表：
　　　这里定义了两个全局字典，用于存放字母编码，一个字典用于编码，另一个字典用于解码，这样程序操作起来比较方便。
　　　这里主要就是遍历，运用的是二叉树的中序遍历。如果明白中序遍历的化，就能看懂这里的代码，每递归到深一层的时候，就在后面多加一个‘0’（左子树）或‘1’（右子树）。
　　　中序遍历我在上一篇博客中讲的还算可以吧，不懂的可以参考一下，否则就可以略过这一段。
　　 这一段是哈夫曼编码的关键，也是难点，希望能够好好理解一下，也是对递归的一个理解。这一点没问题的话，我觉得哈夫曼树真的挺简单的！！！

    """
    while nodeQ.size != 1:
        node1 = nodeQ.popNode()
        node2 = nodeQ.popNode()
        r = TreeNode([None, node1.priority+node2.priority])
        r.leftChild = node1
        r.rightChild = node2
        nodeQ.addNode(r)
    return nodeQ.popNode()





