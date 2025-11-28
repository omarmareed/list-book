class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


def has_increasing_subsequence(stack, k):

    if k <= 1:
        return True
    if stack.size() < k:
        return False

    elements = stack.items.copy()
    n = len(elements)

    dp = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if elements[i] > elements[j]:
                dp[i] = max(dp[i], dp[j] + 1)
                if dp[i] >= k:
                    return True

    return False


def test_increasing_subsequence():
    stack1 = Stack()
    for num in [3, 10, 2, 1, 20]:
        stack1.push(num)
    print("Test 1 (k=3):", has_increasing_subsequence(stack1, 3))

    stack2 = Stack()
    for num in [3, 1, 2]:
        stack2.push(num)
    print("Test 2 (k=3):", has_increasing_subsequence(stack2, 3))

    stack3 = Stack()
    for num in [1, 2, 3, 4, 5]:
        stack3.push(num)
    print("Test 3 (k=4):", has_increasing_subsequence(stack3, 4))


if __name__ == "__main__":
    test_increasing_subsequence()
