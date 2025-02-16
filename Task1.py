total=float(input("Введите значение общей стоимости часов: "))
pricegold=round((total - 96 * 48) / (96 / 16))
print(f"Стоимость золотых часов: {pricegold}")