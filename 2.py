print("Данная программа считает площадь и переметр\nпрямоугольного треугольника\n(катет - положительное целое число)")

a=int(input("введите длинну первого катета: "))
b=int(input("введите длинну второго катета: "))

print("Площадь равна = ", a*b//2, "\nПериметр равен = ", (a**2+b**2)**0.5+a+b)