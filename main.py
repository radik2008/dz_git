# print(a, b, c)
# print(a, "-", b, "-", c)
# print(F"{a} - {b} - {c}")
# print("{} - {} - {}".format(a, b, c))

print('Введите первое число: ')
m = int(input())
n =int(input('Введите второе число: '))
print(m, "+", n, "=", m+n)

# c=5.89
# print(c)
# print(type(c))
# c=int(c)
# print(c+1)
# print(type(c))
# c=str(c)
# print(c+'123')
# print(type(c))

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ)')
# else:
#     print('Привет, ', username)


r = range(100, 0, -20)  # range(100, 0, -20)
for i in r:  # цикл for
    print(i)

# a = 'qwerty'
for i in 'qwerty':  # цикл for для строки
    print(i)

line = ""      #Можно использовать вложенные циклы:
for i in range(5):
    line = ""
    for j in range(5):
        line += "*"
    print(line)