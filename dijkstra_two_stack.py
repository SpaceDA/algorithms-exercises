import math

class Evaluate:

    def main(self, string):
        """Python implementation of Dijkstra's Two-Stack Algorithm for Expression Evaluation"""
        ops = []
        vals = []

        list_of_possible_ops = ["+", "-", "*", "/", "sqrt"]

        for s in string:
            if s == "(":
                pass
            elif s in list_of_possible_ops:
                ops.append(s)
            elif s == ")":
                op = ops.pop()
                val = int(vals.pop())

                if op == "+":
                    val += int(vals.pop())
                elif op == "-":
                    val -= int(vals.pop())
                elif op == "/":
                    val /= int(vals.pop())
                elif op == "*":
                    val *= int(vals.pop())
                elif op == "sqrt":
                    val = math.sqrt(val)
                vals.append(val)
            else:
                vals.append(s)

        return vals[0]


a = Evaluate()
print(a.main("(1+((3+4)*(2+1)))"))
