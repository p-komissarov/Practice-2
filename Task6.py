weight=float(input("Введите вес тела в фунтах: "))
height=float(input("Введите высоту тела в дюймах: "))
bmi=round(weight*703/(height**2), 2) # Формула ИМТ для дюймов и футов
print(f"ИМТ составляет: {bmi}")
