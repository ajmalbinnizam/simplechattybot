# c1 = int(input())
# c2 = int(input())
# c3 = int(input())
# avg = (c1+c2+c3)// 2
# total = avg + (c1 % 2 +c2 % 2 + c3 % 2)
# print(total)
class_1 = int(input())
class_2 = int(input())
class_3 = int(input())
tables_1 = (class_1 // 2) + class_1 % 2
tables_2 = (class_2 // 2) + class_2 % 2
tables_3 = (class_3 // 2) + class_3 % 2
total = (tables_1 + tables_2 + tables_3)
print(total)
