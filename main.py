def add_brackets(arr, n_mul, op):
    index = 0
    for i in range(0, n_mul):
        for j in range(index + 1, len(arr)):
            if arr[j] == op:
                # a = arr[j - 1]
                b = arr[j + 1]
                # print(a, '+', b)
                if b != '(':
                    arr.insert(j - 1, '(')
                    arr.insert(j + 3, ')')
                index = j
                break


def processing(arr):
    num = []
    op = []

    # можно одним пробегом по arr
    n_mul = arr.count('*')
    add_brackets(arr, n_mul, '*')
    print("MUL = ", arr)

    n_div = arr.count('/')
    add_brackets(arr, n_div, '/')
    print("DIV = ", arr)

    print('ADDED BRACKETS = ', ''.join(arr))


def start():
    digits = '1234567890'
    arr = []
    s = str(input("input your statement \n format (a*b)+c+n*m+z/w => "))
    # убрать пробелы strip
    len_s = len(s)
    i = 0
    while i < len_s:
        elem = ''
        while s[i] in digits:
            elem += s[i]
            i += 1
            if i >= len_s:
                break
        if elem == '':
            elem = s[i]
            i += 1
        arr.append(elem)

    print("arr = ", arr)

    processing(arr)


start()
