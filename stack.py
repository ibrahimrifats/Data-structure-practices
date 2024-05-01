class Stack:
    def __init__(self):
        self.top = -1
        self.stack = [0] * 5

    def push(self, x) -> int:
        if self.top < 4:
            self.top += 1
            self.stack[self.top] = x
        else:
            print("Alert! Stack is Full")

    def pop(self):
        if self.top >= 0:
            self.top -= 1
        else:
            print("Pop()! Stack is empty")

    def peek(self):
        if self.top >= 0:
            value = self.stack[self.top]
            return value
        else:
            print("Peek is empty")


if __name__ == "__main__":
    stack = Stack()
    stack.push(21)
    stack.push(10)
    stack.push(34)
    stack.push(45)
    stack.push(32)
    stack.push(56)  
    print(stack.peek()) 
    stack.pop()
    print(stack.peek())
