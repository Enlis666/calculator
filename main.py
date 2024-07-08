from calculator import Calculator


def main(expression: str) -> str:
    """
    Функция производит расчет запроса пользователя.
    Принимает строку выражения в формате 'число : оператор : число'
    Возвращает результат выражение в виде строки
    """

    result_expression = expression.split()  # Разбиваем строку в список

    # Проверяем данные по указанным в ТЗ требованиям
    if len(result_expression) != 3:
        raise ValueError('Формат данных некорректный!')

    try:
        num1, operator, num2 = int(result_expression[0]), result_expression[1], int(result_expression[2])
    except ValueError:
        raise ValueError('Формат данных некорректный!')

    if not (1 <= num1 <= 10) or not (1 <= num2 <= 10):
        raise ValueError('Целые числа должны быть введены в дипапазоне от 0 до 10!')

    # Выбираем подходящий метод и возвращаем результат работы в виде числа
    # Если оператор не подходит под требования - выдаем ошибку
    cal = Calculator()

    if operator == '+':
        return f'Результат: {cal.add(num1, num2)}'
    elif operator == '-':
        return f'Результат: {cal.sub(num1, num2)}'
    elif operator == '*':
        return f'Результат: {cal.mul(num1, num2)}'
    elif operator == '/':
        return f'Результат: {cal.div(num1, num2)}'

    raise ValueError('Введенный оператор явялется некорректным! \nДопускаются операторы: +, -, /, *')


if __name__ == '__main__':

    print('Добро пожаловать в калькулятор 1.0 ^_^')

    while True:
        try:
            user = input('\nВведите данные для расчета в формате (number_one operator number_two): ')
            result = main(user)
            print(result)

        except ValueError as error:
            print(f'Ошибка: {error}')
