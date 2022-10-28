"""Tree drawing."""


class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from turtle import *
reset()
color("pink")
speed(-1)
seth(90)


def tree(size):
    if size < 5:
        return
    forward(size)
    left(60)
    tree(size * (3/5))
    right(120)
    tree(size * (3/5))
    left(60)
    back(size)


tree(200)
