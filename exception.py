#1.Напишите код где есть TypeError,IndexError,NameError.


try:
    weight = int(input("Ваш вес:"))
    dream_weight = input("Желаемый вес:")
    howmuch = weight - dream_weight

    dream_weight[33535]

    print(age)

except TypeError:
    print("Ошибка типов")
except IndexError:
    print("Ошибка индекса")
except NameError:
    print("Ошибка имен")


#2.Возьмите код #1 и создайте для него try... except... Создайте несколько except выражений для разных типов ошибок.


try:
    at = 10
    iin = 15
    wo = 20



    for e in range(-at, at):
        print(wo / e)
        if at > '5':
            print("at > 5")
except TypeError:
    print("Ошибка типов")


#3.Перенесите к себе код #2 и исправьте все ошибки, сделайте так чтобы работал. Если не знаете как исправить ошибку создайте для неё except выражение.


try:
    lst = []

    for i in range(10):
        lst.append(i)



    a = list(reversed(lst))

    sls_obj = slice('0','8')

    print(а[sls_obj])
except NameError:
    print("Ошибка имен")

#4.Перенесите к себе код #3 и исправьте все ошибки, сделайте так чтобы код работал. Если не знаете как исправить ошибку создайте для неё except выражение.


try:
    a = (0)
    b = (1)
    numbers = []

    while b > a:
        numbers += b
        b += 1
except TypeError:
    print("Ошибка типов")
