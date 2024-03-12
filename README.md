# goit-algo-hw-10

### Ефективність методу Монте-Карло

У цьому проекті ми досліджували обчислення визначеного інтеграла за допомогою методу Монте-Карло.
Використовуючи цей метод, ми знайшли наближене значення інтеграла функції f(x)=x^2 на інтервалі від 0 до 2.
Результати були порівняні з аналітичним розв'язком, отриманим за допомогою функції quad з бібліотеки SciPy.


#### Висновки:
- Ефективність методу Монте-Карло: Метод Монте-Карло продемонстрував свою ефективність у вирішенні задачі обчислення визначеного інтеграла. Наближене значення інтеграла, отримане методом Монте-Карло, було дуже близьким до аналітичного результату.
- Точність результатів: Різниця між наближеним значенням інтеграла методом Монте-Карло та аналітичним результатом була дуже мала. Це підтверджує, що метод Монте-Карло може бути ефективним і точним для обчислення визначених інтегралів, навіть у складних випадках.
- Стійкість до складних функцій: Метод Монте-Карло не вимагає аналітичного вирішення інтегралу, тому він може бути застосований до обчислення інтегралів складних функцій, які можуть бути важко або навіть неможливо інтегрувати аналітично.
- Випадковий характер методу: Оскільки метод Монте-Карло ґрунтується на випадковому виборі точок, його точність може коливатися в залежності від кількості згенерованих точок. Зазвичай збільшення кількості точок призводить до більш точних результатів.


Отже, можна зробити висновок, що метод Монте-Карло є потужним і ефективним інструментом для обчислення визначених інтегралів, зокрема у випадку складних функцій, і може бути використаний для отримання точних результатів в числових обчисленнях.