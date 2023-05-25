
# list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list_2[0:len(list_2):2])
# print(type(list_2))

# t = (2, 4, 7, 9)
# print(type(t))
# t = list(t)
# print(type(t))
# a, b, c, d = t
# print(a,b,c,d)

# t = (2, 4, 7, 9)
# for i in t:
#     print(i)

# for i in range(len(t)):
#     print(t[i])


# dictionary = {}
# dictionary ={'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# dictionary['left'] = '⇐'
# del dictionary['left'] # удаление элемента
# for item in dictionary: # for (k,v) in dictionary.items
#     print(dictionary[item])
#     print(item)

# for (k,v) in dictionary.items():
#     print(k,v,v,k)

# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# print(type(colors))

# f=tuple()
# print(type(f))

new_list = [i for i in range(10, 100, 5) if i % 2 == 0]
print(new_list)
