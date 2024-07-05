from calculator import Calculator


def working_with_calculator(expression: str) -> float:
    """
    Функция производит расчет запроса пользователя.
    Принимает строку выражения в формате 'число оператор число'
    Возвращает результат выражение в виде числа
    """
    result_expression = expression.split()

    if len(result_expression) != 3:
        raise ValueError('Формат данных некорректный!')

    try:
        num1, operator, num2 = float(result_expression[0]), result_expression[1], float(result_expression[2])
    except ValueError:
        raise ValueError('Формат данных некорректный!')

    cal = Calculator()

    if operator == '+':
        return cal.add(num1, num2)
    elif operator == '-':
        return cal.sub(num1, num2)
    elif operator == '*':
        return cal.mul(num1, num2)
    elif operator == '/':
        return cal.div(num1, num2)
    raise ValueError('Введенный оператор явялется некорректным! \nДопускаются операторы: +, -, /, *')


if __name__ == '__main__':
    print('Добро пожаловать в калькулятор 1.0')

    while True:
        try:
            user = input('\nВведите данные для расчета в формате (number operator number): ')
            print(f'Ответ: {working_with_calculator(user)}')
        except ValueError as error:
            print(f'Ошибка: {error}')
