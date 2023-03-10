# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

# пример
# 5
# 1 2 3 4 5
# 3
# -> 1


# import random
# N = int(input("Размер массива: ")) 
# print("Элементы массива:")
# A = [random.randint(0,10) for _ in range(N)] # Ввод генир.
# print(*A)
# # A = [int(input()) for i in range(N)] # Вводим элементы массива клавиатуры
# x = int(input("Число x:")) 
# n = 0
# # Проверяем наличие числа в массиве
# for i in range(N):
#     if A[i] == x:
#         n += 1
# print("Число х встречается:", n)


# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

# пример
# 5
# 1 2 3 4 5
# 6
# -> 5


# n = int(input('Количество элементв N: '))
# a=[int(input('Введите число: ')) for i in range(n)]
# x=int(input('Заданное число X:'))
# b=[abs(a[i]-x) for i in range(len(a))]
# print(a[b.index(min(b))])

    



# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, 
# которое содержит либо только английские, либо только русские буквы.

# пример

# Ввод:
# ноутбук
# Вывод:
# 12


# import re
# print("Введите текст: ")
# def isCyrillic(text):
# 	return bool(re.search('[а-яА-Я]', text))
# points_en = {1:'AEIOULNSTR',
#       	2:'DG',
#       	3:'BCMP',
#       	4:'FHVWY',
#       	5:'K',
#       	8:'JX',
#       	10:'QZ'}
# points_ru = {1:'АВЕИНОРСТ',
#       	2:'ДКЛМПУ',
#       	3:'БГЁЬЯ',
#       	4:'ЙЫ',
#       	5:'ЖЗХЦЧ',
#       	8:'ШЭЮ',
#       	10:'ФЩЪ'}
# text = input().upper()
# if isCyrillic(text):
# 	print(sum([k for i in text for k, v in points_ru.items() if i in v]))
# else:
# 	print(sum([k for i in text for k, v in points_en.items() if i in v]))