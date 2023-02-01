# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.
#
# 5 -> 1 0 1 1 0
# 2
print("Enter number of coins: ")
n = int(input())
eagle = 0
nut = 0
for i in range (n):
    x = int(input("Enter side of coins:"))
    if x == 0:
        eagle += 1
    if x > 0:
        nut += 1
if eagle > nut:
    print("You need to flip over:"f'{nut} coins')
else:
    print("You need to flip over:"f'{eagle}')
