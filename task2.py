# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random
qyant=int(input(" Enter qyantity elemenst of list: "))
number_list=[random.randint(0, 100) for _ in range(qyant)]
diap_max=int(input("Enter max of diaposon: "))
diap_min=int(input("enter min of diaposon: "))
index_list=[]
for _ in range(len(number_list)):
    if diap_min<number_list[_]<diap_max:
        index_list.append(_)
print(f"List = {number_list}")
print(f"Index of elements in diaposon are {index_list}")