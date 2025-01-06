def is_balance(s):
    bracket_matching = {'[': ']', '{': '}', '(': ')'}
    stack = []

    for char in s:
        if char in bracket_matching.keys():  # If it's an opening bracket
            stack.append(char)
        elif char in bracket_matching.values():  # If it's a closing bracket
            if not stack or bracket_matching[stack[-1]] != char:
                return "Not Balanced"
            stack.pop()  # Remove the matched opening bracket

    return "Balanced" if not stack else "Not Balanced"


# Test case
s = "[[[[]]]]"
print(is_balance(s))





