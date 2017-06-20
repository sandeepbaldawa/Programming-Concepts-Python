'''
Two stack algorithm
   operand and operator stacks
   1. Value push on the value stack
   2. Operator push on operator stack
   3. Left paranthesis ignore
   4. Right paranthesis
     pop operator and two values 
     push the result of applying that operator to those values on the operand stack
'''

class InfixCalc():
    def __init__(self):
        self.operator_stack = []
        self.operand_stack = []
    def eval(self, operation):
        for each in operation:
            #print self.operator_stack
            #print self.operand_stack
            if each == "+":
                self.operator_stack.append(each)
            elif each == "*":
                self.operator_stack.append(each)
            elif each == ")":
                op = self.operator_stack.pop()
                if op == "+":
                    self.operand_stack.append(int(self.operand_stack.pop()) + int(self.operand_stack.pop()))
                elif op == "*":
                    self.operand_stack.append(int(self.operand_stack.pop()) * int(self.operand_stack.pop()))
            elif each != "(":
                self.operand_stack.append(each)
        return self.operand_stack.pop()

infix = InfixCalc()
assert infix.eval("(1+((2+3))*(4*5))") == 120
assert infix.eval("(1+2)") == 3
assert infix.eval("(1+(2*3))") == 7
assert infix.eval("(1+(2*0))") == 1
assert infix.eval("(0*8)") == 0
assert infix.eval("(1*8)") == 8
