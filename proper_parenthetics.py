u"""Your assignment is to build a quick Python function incorporating one of this week’s data structures that takes a unicode string (text) as input and returns one of three possible values:

Return 1 if the string is “open” (there are open parens that are not closed)
Return 0 if the string is “balanced” (there are an equal number of open and closed parentheses in the string)
Return -1 if the string is “broken” (a closing parens has not been proceeded by one that opens)
For the purposes of this assignment, open and closed parens must match. As an example, consider this string:

')))((('
Although there are an equal number of open and closed parens, they are not properly paired. This string is “broken”.

"""


class Node(object):

    def __init__(self, data, next_node=None):
        """Initialize the Node instance."""
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        """Display the data in this node."""
        if self.next_node is not None:
            return str(self.data) + u', ' + str(self.next_node)
        else:
            return str(self.data)


class LinkedList(object):

    def __init__(self, params=None):
        """Initialize the linked list instance."""
        self.head = Node(None)
        self.length = 0

        if hasattr(params, '__iter__'):
            for node in params:
                self.push(node)
        elif params:
            self.push(params)

    def __repr__(self):
        """Display the linked list."""
        return u'(' + str(self.head) + u')'

    def __len__(self):
        return self.length

    def display(self):
        """Return a unicode string representing the linked list as if it were a Python tuple."""
        return u'(' + str(self.head) + u')'

    def push(self, val):
        """Insert the value val at the head of the list."""
        self.head = Node(val, self.head)
        self.length += 1
        return self

    def pop(self):
        """Pop the first value off the head of the linked list and return it."""
        if self.length > 0:
            popped_node = self.head
            self.head = self.head.next_node
            self.length -= 1
            return popped_node.data
        else:
            return None

    def size(self):
        """Return the length of the list."""
        return self.length

    def search(self, val):
        """Return the node containing val in the list, if exists, else None."""
        current = self.head
        while current.data is not None:
            if current.data == val:
                return current
            elif current.next_node is None:
                return None
            current = current.next_node

    def remove(self, node):  # if last node --> set Node to None
        """Remove the given node from the list, wherever it might be."""
        if node.next_node is not None:
            node.data = node.next_node.data
            node.next_node = node.next_node.next_node
        else:
            node.data = None
            node.next_node = None

        self.length -= 1
        return self


def proper_parenthetics(input):
    """Return 1 if string is open,-1 if closed, and 0 if balanced."""
    l = []
    for char in input:
        if char == ')' or char == '(':
            l.append(char)

    ll = LinkedList(l[::-1])

    while True:
        if ll.head.data == ')':
            return -1
        if ll.length == 0:
            return 0
        if ll.search('(') is None:
            return -1
        if ll.search(')') is None:
            return 1

        current = ll.head
        while current.data is not None:
            if current.data == '(' and current.next_node.data == ')':
                ll.remove(current.next_node)
                ll.remove(current)
                continue
            current = current.next_node
