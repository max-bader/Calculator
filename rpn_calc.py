import sys

class RPNCalculator:
    def __init__(self):
        self.stack = []

    def evaluate_rpn(self, expression):
        tokens = expression.split()
        for token in tokens:
            if token.isdigit():
                self.stack.append(int(token))
            else:
                if len(self.stack) < 2:
                    raise ValueError("Invalid RPN expression")
                operand2 = self.stack.pop()
                operand1 = self.stack.pop()
                if token == '+':
                    self.stack.append(operand1 + operand2)
                elif token == '-':
                    self.stack.append(operand1 - operand2)
                elif token == '*':
                    self.stack.append(operand1 * operand2)
                elif token == '/':
                    self.stack.append(operand1 / operand2)
                else:
                    raise ValueError("Invalid operator: {}".format(token))

        if len(self.stack) != 1:
            raise ValueError("Invalid RPN expression")

        return self.stack[0]

def evaluate_instructions(input_filename, output_filename):
    with open(input_filename, 'r') as input_file:
        instructions = input_file.read().replace('\n', '')

    calculator = RPNCalculator()
    result = calculator.evaluate_rpn(instructions)

    with open(output_filename, 'w') as output_file:
        output_file.write(str(result))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python wp5.py input_filename output_filename")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    try:
        evaluate_instructions(input_filename, output_filename)
        print("Result written to", output_filename)
    except Exception as e:
        print("An error occurred:", e)
