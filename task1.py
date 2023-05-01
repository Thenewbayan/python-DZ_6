# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

first_number=(int(input("Enter first number: ")))
difference=(int(input("Enter difference: ")))
qyantity=(int(input("Enter quantity of progression: ")))
progres_elements=[first_number]
for i in range(1, qyantity):
    progres_elements.append(first_number+difference)
    first_number=progres_elements[i]
print(progres_elements)