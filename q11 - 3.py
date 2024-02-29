def evaluate_expression(s):
    stack = []
    operand = 0
    result = 0
    sign = 1

    for ch in s:
        if ch.isdigit():
            operand = (operand * 10) + int(ch)
        elif ch == '+':
            result += sign * operand
            operand = 0
            sign = 1
        elif ch == '-':
            result += sign * operand
            operand = 0
            sign = -1
        elif ch == '*':
            operand = operand * sign
            sign = 1
        elif ch == '/':
            operand = operand * sign
            sign = 1
            result //= operand
            operand = 0

    result += sign * operand
    return result

# Test the function with an example input
s = "3 + 2 * 2"
result = evaluate_expression(s)
print("Result of evaluating the expression:", result)
