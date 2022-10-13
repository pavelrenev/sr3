name=input("Введите имя студента: ")
surname=input("Введите фамилию студента: ")
god=int(input("Введите год рождения: "))

print(name, "_", surname, "_", god)

a=name
name=surname
surname=a
god+=60

print(name, "_", surname, "_", god)