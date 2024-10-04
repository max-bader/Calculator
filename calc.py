
class RpnCalculator:
    def __init__(self):
        self.stack = []

    def rpn(self, line):
        try:
            expression = line.split()
        except FileNotFoundError as e:
            print(f"Error! {e} doesn't exist.")
        try:
            for i in expression:
                if i.isdigit():
                    self.stack.append(int(i))
                else:
                    num_1 = self.stack.pop()
                    num_2 = self.stack.pop()

                    if i == '+':
                        self.stack.append(num_1 + num_2)
                    elif i == '-':
                        self.stack.append(num_1 - num_2)
                    elif i == '*':
                        self.stack.append(num_1 * num_2)
                    elif i == '/':
                        self.stack.append(num_1 / num_2)
    
        except ValueError:
            print("Error!")
        
        return self.stack[0]
                    