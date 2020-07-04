"""
The question is if you have a string of brackets,
can you determine if the brackets are balanced

eg.
({[]}) is balanced
((()) is not balanced
(((} is not balanced

The solution is to use a stack
Every time there is an open parenthesis, you add to the stack
When you encounter a closed parenthesis, two things must be checked
1) if the stack is empty, this means there is an odd one out
2) if the open parenthesis in the stack corresponding one you are checking
If any of the above is True, the string is not balanced
Otherwise, open = close, and you pop the last bracket out of the stack
Once that is done,

"""


# def check_paren(array):
#     open_paren = {"[", "(", "{"}
#     paren_dict = {"[": "]", "(": ")", "{": "}"}
#
#     stack = []
#
#     for element in array:
#         if element in open_paren:
#             stack.append(element)
#         else:
#             if not stack or paren_dict[stack[-1]] != element:
#                 return False
#             else:
#                 stack.pop(-1)
#     if stack:
#         return False
#     else:
#         return True

def check_paren(arr):
    dict_ = {")": "(", "}": "{", "]": "["}
    stack = []

    for bracket in arr:
        if bracket not in dict_:
            stack.append(bracket)
        else:
            if not stack or stack[-1] != dict_[bracket]:
                return False
            else:
                stack.pop(-1)

    if stack:
        return False
    return True



"""
test cases
"""
# balanced
array = "(({{}}))"
print(check_paren(array))

# one more open
array = "((({{}}))"
print(check_paren(array))

# one more closed
array = "(({{}})))"
print(check_paren(array))

# not the closed parenthesis expected
array = "(((}"
print(check_paren(array))
