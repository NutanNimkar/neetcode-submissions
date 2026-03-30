class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #we iterate through the list
        #when we encounter nums we add them to a stack and when we see a sign we pop() until the stack is empty and 
        #then we apply that sign to those elements

        stack = []
        for i in range(len(tokens)):
            if tokens[i] == "+":
               stack.append(stack.pop() + stack.pop())
            elif tokens[i] == "-":
                a = stack.pop()
                b = stack.pop() 
                stack.append(b - a)
            elif tokens[i] == "*":
                stack.append(stack.pop() * stack.pop())
            elif tokens[i] == "/":
                a = stack.pop()
                b = stack.pop() 
                stack.append(int(float(b) / a))
            else:
                stack.append(int(tokens[i]))
        res = stack.pop()

        return res

