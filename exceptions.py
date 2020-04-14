
def actions(arithmetic_operation, num1, num2):
    if arithmetic_operation == '+':
        summary = num1 + num2
        print(summary)
    elif arithmetic_operation == '-':
        difference = num1 - num2
        print(difference)
    elif arithmetic_operation == '*':
        multiplication = num1 * num2
        print(multiplication)
    elif arithmetic_operation == '/':
        division = num1 / num2
        print(division)


def define_exceptions(operation, arithmetic_operation, num1, num2):

    assert len(operation) == 3, 'Вы ввели больше аргументов, чем нужно.'
    try:
        num1 = int(num1)
        num2 = int(num2)
        division = num1 / num2
        actions(arithmetic_operation, num1, num2)
    except ValueError:
        print('Невозможно проводить арифметические операции со строками.')
    except ZeroDivisionError:
        print('На ноль делить нельзя!')


def our_input():
    operation = input('Введите операцию и два положительных числа через пробелы:')
    operation = operation.split()
    arithmetic_operation = operation[0]
    assert arithmetic_operation in ['+', '-', '*', '/'], 'Такая операция недоступна.'
    try:
        num1 = operation[1]
        num2 = operation[2]
    except IndexError:
        print('Вы ввели недостаточно аргументов.')
    try:
        define_exceptions(operation, arithmetic_operation, num1, num2)
    except UnboundLocalError:
        print('Вы не ввели второй аргумент.')


our_input()




