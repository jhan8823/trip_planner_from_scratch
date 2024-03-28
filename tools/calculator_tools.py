from langchain.tools import tool

class CalculatorTools():
    @tool('Calculate the budget')
    def calculate(operation):
        """
        Useful to perform any mathematical operation, such as addition, subtraction, multiplication, division, etc.
        The input to this tool should be a mathematical operation in the form of a string, such as "2 + 2", "5 * 3", etc.
        """
        try:
            return eval(operation)
        except SyntaxError:
            return "Invalid operation. Please provide a valid mathematical operation in the form of a string, such as '2 + 2', '5 * 3', etc."
