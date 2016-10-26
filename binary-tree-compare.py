"""Code Wars kata

https://www.codewars.com/kata/binary-tree-compare
"""

# return True if the two binary trees rooted and a and b are equal in value and structure
# return False otherwise
def compare(a, b):
    # take care of NoneTypes

    if a is None and b is None:
        return True
    if a is None and b is not None:
        return False
    if a is not None and b is None:
        return False

    if a.val is None and b.val is None:
        return True
    if a.val is None and b.val is not None:
        return False
    if a.val is not None and b.val is None:
        return True
    if a.val != b.val:
        return False

    if a.val == b.val:            # values match
        if type(a.left) != type(b.left):    # take care of = types
            return False
        if type(a.right) != type(b.right):
            return False

        if type(a.left) == int:    # if int, compare, else recursive
            if a.left == b.left:
                left = True
            else:
                left = False
        else:
            left = compare(a.left, b.left)

        if type(a.right) == int:
            if a.right == b.right:
                right = True
            else:
                right = False
        else:
            right = compare(a.right, b.right)

        if right and left:
            return True
        else:
            return False
