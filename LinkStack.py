class StackUnderflow(ValueError):
    pass


class LNode:
    def __init__(self, elem=None, next_=None):
        self.elem = elem
        self.next = next_


class LinkStack:
    def __init__(self):
        self.root = LNode()
        self.length = 0

    def __len__(self):
        return self.length

    def is_empty(self):
        return self.length is 0

    def top(self):
        if self.is_empty():
            raise StackUnderflow("The stack is empty.")
        return self.root.next.elem

    def push(self, elem):
        node = LNode(elem)
        node.next = self.root.next
        self.root.next = node
        self.length += 1

    def pop(self):
        if self.is_empty():
            raise StackUnderflow("The stack is empty.")
        q = self.root.next
        self.root.next = q.next
        self.length -= 1

    def print_all(self):
        if self.is_empty():
            raise StackUnderflow("The stack is empty.")
        p = self.root.next
        while p is not None:
            print(p.elem)
            p = p.next

    def status(self):
        if self.is_empty():
            print("The stack is empty.")
        else:
            print("The stack has room.")


LS = LinkStack()
LS.status()
for i in range(10):
    LS.push(i)
print(len(LS))
LS.status()
print(LS.top())
LS.print_all()
for i in range(10):
    LS.pop()
LS.status()
