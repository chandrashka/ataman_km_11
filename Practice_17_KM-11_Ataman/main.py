from logarithm import logarithm
from exp_root import root, exponentiation
from factorial import factorial

def check(n):
    try:
        int(n)
    except:
        return False
    return int(n)
def main():
    while 1:
        print("Меню програми")
        print("1.Запустити модуль 'factorial';")
        print("2.Запустити модуль 'exp_root';")
        print("3.Запустити модуль 'logarithm';")
        n = input("Введіть пункт з меню програми: ")
        while not n == '1' and not n =='2' and not n =='3':
            print("Неправильне введення")
            n = input("Введіть пункт з меню програми: ")
        print("Доступні функції:")

        if n == '1':
            print("1) fact(n) - рахує факторіал числа n.")
            inp = input("Введіть функцію, яку потрібно запустити: ")
            while not inp == '1':
                print("Неправильне введення")
                inp = input("Введіть функцію, яку потрібно запустити: ")
            q = input("Введіть Ваше число: ")
            res = factorial.fact(check(q))

            while not check(q) and not factorial.fact(check(q)):
                print("Неправильне введення")
                q = input("Введіть Ваше число: ")
                res = factorial.fact(check(q))

            print("Факторіал числа", q, '=', res)
        elif n == '2':
            print("1) exp2(n) - підносить число n до квадрату;\n2) exp3(n) - підносить число n до третього степеня;\n3) root2(n) - рахує квадратний корень для числа n;\n4) root3(n) - рахує корень третього степеня для числа n.")
            inp = input("Введіть функцію, яку потрібно запустити: ")
            while not inp == '1' and not inp == '2' and not inp == '3' and not inp == '4':
                print("Неправильне введення")
                inp = input("Введіть функцію, яку потрібно запустити: ")
            q = input("Введіть Ваше число: ")
            if inp == '1':

                    while not check(q):
                        print("Неправильне введення")
                        q = input("Введіть Ваше число: ")
                    res = exponentiation.exp2(check(q))

                    print("Піднесення до квадрату числа", q, '=', res)
            elif inp == '2':
                    
                    while not check(q):
                        print("Неправильне введення")
                        q = input("Введіть Ваше число: ")
                    res = exponentiation.exp3(check(q))

                    print("Піднесення до третього степеня числа", q, '=', res)
            elif inp == '3':

                    while not check(q) and not root.root2(check(q)):
                        print("Неправильне введення")
                        q = input("Введіть Ваше число: ")
                    res = root.root2(check(q))

                    print("Корень квадратний числа", q, '=', res)
            else:

                while not check(q):
                    print("Неправильне введення")
                    q = input("Введіть Ваше число: ")
                res = root.root3(check(q))

                print("Корень третього степеня числа", q, '=', res)
        else:
            print("1) log(a,b) - рахує логарифм числа b за основою а;\n2) ln(b) - рахує натуральний логарифм числа b;\n3) lg(b) - рахує логарифм числа b за основою 10.")
            inp = input("Введіть функцію, яку потрібно запустити: ")
            while not inp == '1' and not inp == '2' and not inp == '3':
                print("Неправильне введення")
                inp = input("Введіть функцію, яку потрібно запустити: ")
            if inp == '1':
                while 1:
                    try:
                        a,b = input("Введіть числа а та b: ").split()
                        res = logarithm.log(check(a),check(b))
                        if not res:
                            raise Exception
                        else:
                            break
                    except:
                        print("Неправильне введення")
                print("Логарифм за основою", a, "числа", b, '=', res)
            elif inp == '2':
                q = input("Введіть Ваше число: ")
                res = logarithm.ln(check(q))
                while not check(q) and not logarithm.ln(check(q)):
                    print("Неправильне введення")
                    q = input("Введіть Ваше число: ")
                    res = logarithm.ln(check(q))

                print("Натуральний логарифм числа", q, '=', res)
            else:
                q = input("Введіть Ваше число: ")
                res = logarithm.lg(check(q))
                while not check(q) and not logarithm.lg(check(q)):
                    print("Неправильне введення")
                    q = input("Введіть Ваше число: ")
                    res = logarithm.lg(check(q))

                print("Натуральний логарифм за основою 10 числа", q, '=', res)
        ok = input("Якщо, хочете повернутися до меню програми введіть 1, якщо хочете закінчити, введіть будь-який інший символ: ")
        if ok != '1':
            break

if __name__ == '__main__':
    main()

