class Calculator:
    """
    Данный класс состоит из статичных методов
    Методы принимают два числа и возвращают результат выражение
    """
    @staticmethod
    def add(num1: int, num2: int) -> int:
        return num1 + num2

    @staticmethod
    def sub(num1: int, num2: int) -> int:
        return num1 - num2

    @staticmethod
    def mul(num1: int, num2: int) -> int:
        return num1 * num2

    @staticmethod
    def div(num1: int, num2: int) -> int:
        if num2 == 0:
            raise ValueError('На ноль делить нельзя!')

        return int(num1 / num2)
