def isBalanced(exp):
    stack = []
    matching_bracket = {')': '(', '}': '{', ']': '['}

    for char in exp:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            # If the stack is empty or top of the stack does not match, return False
            if not stack or stack[-1] != matching_bracket[char]:
                return False
            # Otherwise, pop the matching opening bracket from the stack
            stack.pop()

    # In the end, if the stack is empty, the expression is balanced
    return not stack


exp1 = "(({[]})){}()"


if (isBalanced(exp1)):
    print("Balanced")
else:
    print("Not Balanced")

exp2 = "()["

if (isBalanced(exp2)):
    print("Balanced")
else:
    print("Not Balanced")