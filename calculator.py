class Calculator:

    @staticmethod
    def add(num1: float, num2: float) -> float:
        return num1 + num2

    @staticmethod
    def sub(num1: float, num2: float) -> float:
        return num1 - num2

    @staticmethod
    def mul(num1: float, num2: float) -> float:
        return num1 * num2

    @staticmethod
    def div(num1: float, num2: float) -> float:
        if num2 == 0:
            raise ValueError('На ноль делить нельзя!')
        return num1 / num2
