""" Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов 
(т.е. число гласных букв)в каждой фразе стихотворения одинаковое. 
Фраза может состоять из одного слова, если во фразе несколько слов,
 то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, 
если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

Ввод:
пара-ра-рам рам-пам-папам па-ра-па-да
Вывод:
Парам пам-пам """

#            Решение:

# #vinni = list(input("Введите текст: " ))
# vinni = ('пара-ра-рам рам-пам-папам па-ра-па-да')
# vinni = vinni. split(' ')
# n1 = vinni[0].count('а')    
# n2 = vinni[1].count('а')
# n3 = vinni[2].count('а')
# print("Количество буквы 'а' в фразах: ", n1, n2, n3)
# if n1 % 2 == 0 and n2 % 2 == 0 and n3 % 2 == 0:
#     print("Парам пам-пам")
# else:
#     print("Пам парам")



""" #Черновик

n = int(input('Сколько будет строк? '))
gls = sgl=0
vse_gls = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
count = 0
while n > count:
    ls=gl=0
    vinni = input("Введите фразу: ")
    for i in vinni:
        if i.isalpha():
            if i in vse_gls:
                ls += 1
            else:
                gl += 1
    print('Кол-во гласных:', ls,'Кол-во согласных:', gl)
    gls+=ls
    sgl+=gl
    count += 1
print('Кол-во гласных во всем тексте:', gls,'Кол-во согласных во всем тексте:', sgl) """



""" Задача 36:
 Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. 
Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, 
у операции умножения.

Ввод:     
print_operation_table(lambda x, y: x * y)

 Вывод:
1 2 3 4 5 6
2 4 6 8 10 12
3 6 9 12 15 18
4 8 12 16 20 24
5 10 15 20 25 30
6 12 18 24 30 36 """

#                    Решение:

# def printOperationTable(operation, num_rows, num_columns):
#   for i in range(1, num_rows+1):
#     print(*(operation(i, k) for k in range(1, num_columns+1)))
# print(printOperationTable(lambda x,y: x*y, 6, 6))