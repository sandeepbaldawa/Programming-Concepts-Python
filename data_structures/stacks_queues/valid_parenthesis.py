'''
If the code in S uses brackets correctly, output “Success” (without the quotes). Otherwise,
output the 1-based index of the first unmatched closing bracket, and if there are no unmatched
closing brackets, output the 1-based index of the first unmatched opening bracket.

# Strings which are paren, brackets and braces matched i.e. PBB matched
# "(){}[]"

# Answer:-
# Stack is best suited for parsing and matching operations
# "([{" => Left characters
# "]})" => Right characters
# Push if matching left characters
# Pop if matching right characters
# After Pop compare if left and right character matches

"""


BRACKETS =['(',')','{','}','[',']']
OPENING = ['(','{','[']
CLOSING = [')','}',']']

def check_match(open, close):
    '''Check bracket open/close bracket match'''
    #print open, close
    if open == "(" and close == ")":
        return True
    if open == "{" and close == "}":
        return True
    if open == "[" and close == "]":
        return True
    return False

def bracket_check(input):
    stack = []
    idx = 0

    while(idx < len(input)):
        if input[idx] not in BRACKETS:
            idx += 1
            continue
        if input[idx] in OPENING:
            stack.append(input[idx])
        else:  # If closing bracket compare with last opening bracket in stack
            if not check_match(stack.pop(),input[idx]):
                return False
        idx += 1

    return len(stack) == 0

print bracket_check('[dklf(df(kl))d]{}')
print bracket_check('{[[[]]]}')
print bracket_check('{3234[fd')
