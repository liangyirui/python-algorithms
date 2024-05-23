"""
Given a string s of '(' , ')' and lowercase English characters.
Remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.
Formally, a parentheses string is valid if and only if:
It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
"""

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


if __name__ == '__main__':
    s = 'a)b(c)d'
    s_valid = make_string_valid(s)
    print(s_valid)