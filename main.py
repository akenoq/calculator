op_dict = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '(': 0,
    ')': 0
}


def is_int(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


def calc_stack(op, num):
    p = False
    while not p:
        if op_dict[op[len(op) - 1]] == 1:  # если до этого в стеке +/-, то вычисляем
            if op[len(op) - 1] == '+':
                ans = num.pop() + num.pop()
                num.append(ans)
            elif op[len(op) - 1] == '-':
                op_2 = num.pop()
                op_1 = num.pop()
                ans = op_1 - op_2
                num.append(ans)
            op.pop()
        elif op_dict[op[len(op) - 1]] == 2:  # если до этого в стеке *//, то вычисляем
            if op[len(op) - 1] == '*':
                ans = num.pop() * num.pop()
                num.append(ans)
            elif op[len(op) - 1] == '/':
                op_2 = num.pop()
                op_1 = num.pop()
                ans = op_1 / op_2
                num.append(ans)
            op.pop()
            print('POP = ', op)
        if len(op) != 0:
            p = False
        else:
            p = True
        print('P = ', p)
        print('POP = ', op)

        print('NUM 4 = ', num)
        print('OP 4 = ', op)
    return num


def calc(arr):
    num = []
    op = []
    len_arr = len(arr)
    print('lol')

    for i in range(0, len_arr):
        print('\nNEXT  I = {}, ARR[I] = {}'.format(i, arr[i]))
        if is_int(arr[i]):
            num.append(int(arr[i]))
            print('NUM 1 = ', num)
            print('OP 1 = ', op)
        elif arr[i] == '+' or arr[i] == '-':
            print("+/-")
            if len(op) != 0:
                if op_dict[op[len(op) - 1]] == 1:  # если до этого в стеке +/-, то вычисляем
                    if op[len(op) - 1] == '+':
                        ans = num.pop() + num.pop()
                        op.pop()
                    else:
                        op_2 = num.pop()
                        op_1 = num.pop()
                        ans = op_1 - op_2
                        op.pop()
                    num.append(ans)
                elif op_dict[op[len(op) - 1]] == 2:
                    if op[len(op) - 1] == '*':
                        ans = num.pop() * num.pop()
                        op.pop()
                    else:
                        op_2 = num.pop()
                        op_1 = num.pop()
                        ans = op_1 / op_2
                        op.pop()
                    num.append(ans)
            op.append(arr[i])
            print('NUM 2 = ', num)
            print('OP 2 = ', op)
        elif arr[i] == '*' or arr[i] == '/':
            print('*//')
            if op[len(op) - 1] == '-' or op[len(op) - 1] == '+':  # or arr[i] == '(':
                op.append(arr[i])
            elif op[len(op) - 1] == '(':
                op.append(arr[i])
            elif op[len(op) - 1] == '*' or op[len(op) - 1] == '/':
                if op[len(op) - 1] == '*':
                    ans = num.pop() * num.pop()
                    op.pop()
                else:
                    op_2 = num.pop()
                    op_1 = num.pop()
                    ans = op_1 / op_2
                    op.pop()
                num.append(ans)
                op.append(arr[i])
            else:
                op.append(arr[i])
            print('NUM 3 = ', num)
            print('OP 3 = ', op)
        elif arr[i] == '(':
            op.append(arr[i])
        elif arr[i] == ')':
            p = False
            while not p:
                if len(op) != 0:
                    if op_dict[op[len(op) - 1]] == 1:  # если до этого в стеке +/-, то вычисляем
                        if op[len(op) - 1] == '+':
                            ans = num.pop() + num.pop()
                            num.append(ans)

                        elif op[len(op) - 1] == '-':
                            op_2 = num.pop()
                            op_1 = num.pop()
                            ans = op_1 - op_2
                            num.append(ans)

                    if op[len(op) - 1] == '*' or op[len(op) - 1] == '/':  # если до этого в стеке *//, то вычисляем
                        if op[len(op) - 1] == '*':
                            ans = num.pop() * num.pop()
                            num.append(ans)

                        elif op[len(op) - 1] == '/':
                            op_2 = num.pop()
                            op_1 = num.pop()
                            ans = op_1 / op_2
                            num.append(ans)
                    op.pop()
                    # print('POP = ', op)
                if len(op) != 0:
                    p = op[len(op) - 1]
                    if p == '(':  # если дошли до левой скобки, выходим из цикла
                        op.pop()
                        p = True
                    else:
                        p = False
                else:
                    p = True
                print('P = ', p)
                print('POP = ', op)
                print('NUM 4 = ', num)
                print('OP 4 = ', op)
        else:
            pass

    if len(op) != 0:
        calc_stack(op, num)

    return num[0]


def processing(arr):
    # n_mul = arr.count('*')
    # add_brackets(arr, n_mul, '*')
    # n_div = arr.count('/')
    # add_brackets(arr, n_div, '/')

    ans = calc(arr)
    print('\nANS = ', ans)


def make_arr(s):
    import re
    arr = []
    len_s = len(s)
    i = 0
    while i < len_s:
        elem = ''
        while re.match(r'\d', s[i]):
            elem += s[i]
            i += 1
            if i >= len_s:
                break
        if elem == '':
            elem = s[i]
            i += 1
        arr.append(elem)
    return arr


def start():
    s = str(input("input your statement \n format (a*b)+c+n*m+z/w => "))
    s = s.replace(' ', '')
    arr = make_arr(s)

    print("arr = ", arr)

    processing(arr)


start()

# def add_brackets(arr, n_mul, op):
#     index = 0
#     for i in range(0, n_mul):
#         for j in range(index + 1, len(arr)):
#             print('INDEX TWO = ', index)
#             if arr[j] == op:
#                 print("INDEX = ", index)
#                 index = j
#                 a = arr[j - 1]
#                 b = arr[j + 1]
#                 if b != '(' and a != ')':
#                     arr.insert(j - 1, '(')
#                     arr.insert(j + 3, ')')
#                 print('INDEX = ', index)
#                 break
#                 # arr.insert(0, '(')
#                 # arr.append(')')
