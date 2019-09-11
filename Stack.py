class StackUnderflow(ValueError):
    pass


class StackOverflow(ValueError):
    pass


class SStack():
    def __init__(self, maxsize=100):
        self._elems = []
        self.maxsize = maxsize

    def is_empty(self):
        return self._elems == []

    def is_full(self):
        return len(self._elems) == self.maxsize

    def top(self):
        if self.is_empty():
            raise StackUnderflow("The stack is empty.")
        return self._elems[-1]

    def push(self, elem):
        if self.is_full():
            raise StackOverflow("The Stack is full.")
        self._elems.append(elem)

    def pop(self):
        if self.is_empty():
            raise StackUnderflow("The stack is empty.")
        return self._elems.pop()

    def enlarge(self):
        self.maxsize *= 2

    def print_stack(self):
        if self.is_empty():
            raise StackUnderflow("The stack is empty.")
        for i in range(len(self._elems)):
            print(self._elems[i])

    def status(self):
        if self.is_empty():
            print("The stack is empty.")
        elif self.is_full():
            print("The stack is full.")
        else:
            print("The stack has room.")


S = SStack()
S.status()
for i in range(100):
    S.push(i)
print(S.top())
S.print_stack()
S.status()
S.enlarge()
S.status()
for i in range(100, 200):
    S.push(i)
S.status()
print(S.top())
for i in range(100):
    S.pop()
S.print_stack()
S.status()
for i in range(100):
    S.pop()
S.status()
