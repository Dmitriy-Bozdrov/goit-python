result = 0
operator = ' '
while operator != '=':
    try:
        number = float(input('Введите число: '))
    except ValueError:
        print('Error, try again')
        continue
    if operator == None:
        result = number
    elif operator == '+':
        result += number
    elif operator == "-":
        result -= number
    elif operator == "*":
        result *= number
    elif operator == "/":
        try:
            result /= number
        except ZeroDivisionError:
            print("Нельзя делить на ноль")
            continue
    operator = input('Введите оператор: ')
    while operator not in ('+-*/='):
        print('Error, try again1')
        operator = input('Введите оператор: ')
    if operator == '=':
        continue   
               
print(result)
