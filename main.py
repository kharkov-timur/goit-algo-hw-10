from pulp import *


# Створення змінних
limonad = LpVariable("Лимонад", lowBound=0)
frukt_sik = LpVariable("Фруктовий_сік", lowBound=0)

# Ініціалізація моделі
model = LpProblem("Максимізація_виробництва", LpMaximize)

# Обмеження ресурсів
model += 2 * limonad + frukt_sik <= 100, "Обмеження_на_воду"
model += limonad + frukt_sik <= 50, "Обмеження_на_цукор"
model += limonad <= 30, "Обмеження_на_лимонний_сік"
model += 2 * frukt_sik + limonad <= 40, "Обмеження_на_фруктове_пюре"

# Функція максимізації
model += limonad + frukt_sik

# Вирішення моделі
model.solve()

# Виведення результатів
print("Кількість виробленого лимонаду:", value(limonad))
print("Кількість виробленого фруктового соку:", value(frukt_sik))
