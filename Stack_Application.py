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


class ESStack(SStack):
    def depth(self):
        return len(self._elems)


def check_parens(text):
    parens = "()[]{}"
    open_parens = "([{"
    opposite = {")": "(", "]": "[", "}": "{"}

    def parentheses(text):
        i, text_len = 0, len(text)
        while True:
            while i < text_len and text[i] not in parens:
                i += 1
            if i >= text_len:
                return
            yield text[i], i
            i += 1

    st = SStack()
    for pr, i in parentheses(text):
        if pr in open_parens:
            st.push(pr)
        elif st.pop() != opposite[pr]:
            print("Unmatching is found at", i, "for", pr)
            return False
    print("All parentheses are correctly matched.")
    return True


def suf_exp_evaluator(exp):
    operators = "+-*/"
    st = ESStack()

    for x in exp:
        if x not in operators:
            st.push(float(x))
            continue

        if st.depth() < 2:
            raise SyntaxError("Short of operand(s).")
        a = st.pop()
        b = st.pop()

        if x == "+":
            c = b+a
        elif x == "-":
            c = b-a
        elif x == "/":
            c == b/a
        elif x == "*":
            c == b*a
        else:
            break
        st.push(c)

    if st.depth() == 1:
        return st.pop()
    raise SyntaxError("Extra operand(s).")


def suffix_exp_evaluator(line):
    return suf_exp_evaluator(line.split())


text = "(1+1=2)"
check_parens(text)
