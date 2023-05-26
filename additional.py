num_rows = int(input('Введите количество строк: '))
num_columns = int(input('Введите количество столбцов: '))
def operation (rows, columns):
    i = 0
    num = 1
    while(i < rows):
        m = 0
        mass = []
        j = 0
        while(j < columns):
            m = m + num
            mass.append(m)
            j += 1
        print(*mass)
        i += 1
        num += 1
def print_operation_table(operation, num_rows, num_columns):
    print(operation (num_rows, num_columns))
print_operation_table(operation, num_rows, num_columns)