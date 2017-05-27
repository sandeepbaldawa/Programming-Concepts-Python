'''
Bracket Match

A string of brackets is considered correctly matched if every opening bracket in the string can be paired up with a later closing bracket, and vice versa. For instance, “(())()” is correctly matched, whereas “)(“ and “((” aren’t. For instance, “((” could become correctly matched by adding two closing brackets at the end, so you’d return 2.

Given a string that consists of brackets, write a function bracketMatch that takes a bracket string as an input and returns the minimum number of brackets you’d need to add to the input in order to make it correctly matched.

Explain the correctness of your code, and analyze its time and space complexities.

Examples:

input:  text = “(()”
output: 1

input:  text = “(())”
output: 0

input:  text = “())(”
output: 2
'''

def bracketMatch(text):
  result = 0
  bracket_correct = 0
  for each in text:
    if each == "(":
      result += 1
    else:
      result -= 1
      # everytime closing more than opening,
      # correct "1" bracket
      if result < 0:
        bracket_correct += 1
        result += 1
  return bracket_correct + result

print bracketMatch('())(')

# Can also use stack, but requires extra space, above is O(1)
def bracketMatch(word):
  stack = []
  for each in word:
    if each == ")" and len(stack) > 0 and stack[0] == "(":
       stack.pop()[0]
    else:
       stack.append(each)
  return len(stack)
print bracketMatch('())(')                           



