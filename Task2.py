# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
#
# 4 4 -> 2 2
# 5 6 -> 2 3

a = int(input("Enter the sum of numbers: "))
b = int(input("Enter the multiplication of numbers: "))
c = 0
for i in range(a + b):
    if c:
        break
    for j in range(a + b):
        if i + j == a and i * j == b:
            c = 1
            print(*sorted([i, j]))
            break

