"""
Solution to balanced
Use a stack, the moment the value popped doesnt match, it is not balanced
({[]}) = balanced
({[) = unbalanced
"""
from stack import Stack


def is_match(pop_char, char):
    if pop_char == "(" and char == ")":
        return True
    elif pop_char == "{" and char == "}":
        return True
    elif pop_char == "[" and char == "]":
        return True
    else:
        return False


def balance_parenthesis(bracket):
    solution_stack = Stack()
    open_brace = "{(["
    for paren in bracket:
        if paren in open_brace:
            solution_stack.add_item(paren)
        else:
            if solution_stack.is_empty() or not is_match(solution_stack.remove_item(), paren):
                return False
    if solution_stack.is_empty():
        return True
    else:
        return False


if __name__ == "__main__":
    test_string = "(())"
    print(balance_parenthesis(test_string))
