"""
Given a string s of '(' , ')' and lowercase English characters.
Remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.
Formally, a parentheses string is valid if and only if:
It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
"""

def is_balanced_parentheses(s: str):
    """
    docstring
    """
    balance = 0
    for ch in s:
        if ch == '(':
            balance += 1
        elif ch == ')':
            balance -= 1
        if balance < 0:
            return False
    return balance == 0


def make_string_valid(s: str) -> str:
    stack = []
    for i, ch in enumerate(s):
        if ch not in '()':
            continue
        elif ch == '(' or not stack:
            stack.append(i)
        else:
            stack.pop()

    skip = set(stack)
    sb = []
    for i, ch in enumerate(s):
        if i in skip:
            continue
        sb.append(ch)
    
    return ''.join(sb)


def make_string_valid_2(s: str) -> str:
    sb = list(s)
    skip_indexes = []
    for i, ch in enumerate(s):
        if ch == '(':
            skip_indexes.append(i)
        elif ch == ')':
            if skip_indexes:
                skip_indexes.pop()
            else:
                # remove invalid close brackets
                sb[i] = ''
    while skip_indexes:
        sb[skip_indexes.pop()] = ''
    return ''.join(sb)

if __name__ == '__main__':
    s = 'a)b(c)d'
    s_valid = make_string_valid(s)
    print(s_valid)
    print(make_string_valid_2(s))